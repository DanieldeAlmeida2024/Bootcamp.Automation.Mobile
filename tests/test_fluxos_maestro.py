"""Validação estrutural do catálogo Maestro (não emula Android/iOS)."""
import pathlib
import unittest
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "samples"

def referencias(objeto):
    if isinstance(objeto, list):
        for item in objeto:
            yield from referencias(item)
    elif isinstance(objeto, dict):
        for chave, valor in objeto.items():
            if chave in ("runFlow", "runScript"):
                if isinstance(valor, str):
                    yield valor
                elif isinstance(valor, dict) and isinstance(valor.get("file"), str):
                    yield valor["file"]
            yield from referencias(valor)


class TestesMaestro(unittest.TestCase):
    def test_todos_fluxos_tem_documentos_yaml_validos(self):
        caminhos = sorted(SAMPLES.rglob("*.yaml")) + sorted(SAMPLES.rglob("*.yml"))
        self.assertGreaterEqual(len(caminhos), 10)
        for caminho in caminhos:
            with self.subTest(fluxo=str(caminho.relative_to(ROOT))):
                documentos = list(yaml.safe_load_all(caminho.read_text(encoding="utf-8")))
                self.assertGreaterEqual(len(documentos), 2)
                self.assertIsInstance(documentos[0], dict)
                self.assertIn("appId", documentos[0])
                self.assertIn(documentos[0]["appId"],
                              ("org.wikipedia", "org.wikimedia.wikipedia"))
                self.assertIsInstance(documentos[1], list)
                self.assertGreater(len(documentos[1]), 0)

    def test_subfluxos_e_scripts_referenciados_existem(self):
        for caminho in list(SAMPLES.rglob("*.yaml")) + list(SAMPLES.rglob("*.yml")):
            documentos = list(yaml.safe_load_all(caminho.read_text(encoding="utf-8")))
            for referencia in referencias(documentos[1]):
                if "${" in referencia:
                    continue  # fluxo dinâmico: não pode ser resolvido estaticamente
                destino = (caminho.parent / referencia).resolve()
                with self.subTest(arquivo=str(caminho.relative_to(ROOT)), ref=referencia):
                    self.assertTrue(destino.is_relative_to(SAMPLES.resolve()))
                    self.assertTrue(destino.is_file(), f"Não encontrado: {destino}")

    def test_smoke_realiza_assert_de_tela_apos_iniciar_app(self):
        for nome in ("android-flow.yaml", "ios-flow.yaml"):
            with self.subTest(nome=nome):
                conteudo = (SAMPLES / nome).read_text(encoding="utf-8")
                self.assertIn("clearState: true", conteudo)
                self.assertIn("- assertVisible:", conteudo)
                self.assertNotIn("  - passing", conteudo)

    def test_nao_existem_taps_ficticios_em_fluxos_avancados(self):
        for nome in ("android-advanced-flow.yaml", "ios-advanced-flow.yaml",
                     "subflows/onboarding-android.yaml", "subflows/onboarding-ios.yaml"):
            with self.subTest(nome=nome):
                conteudo = (SAMPLES / nome).read_text(encoding="utf-8")
                self.assertNotIn("Non existent view", conteudo)

    def test_login_didatico_e_offline_nao_envia_credenciais(self):
        script = (SAMPLES / "wikipedia-android-advanced/scripts/fetchTestUser.js").read_text(
            encoding="utf-8"
        )
        login = (SAMPLES / "wikipedia-android-advanced/auth/login.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn('output.test_user', script)
        self.assertIn('example.invalid', script)
        self.assertNotIn('http.get(', script)
        self.assertNotIn('fetch(', script)
        self.assertNotIn('jsonplaceholder', script.lower())
        self.assertIn('runScript: "../scripts/fetchTestUser.js"', login)
        self.assertIn('"${output.test_user.username}"', login)
        # Use the form only; sending invented credentials to Wikipedia is not a valid E2E login.
        self.assertNotIn('- tapOn: "LOG IN"', login)
        self.assertNotIn('- tapOn: "Create account"', login)

    def test_cadastro_gera_identidade_apenas_ficticia(self):
        fixture = SAMPLES / "wikipedia-android-advanced/scripts/generateCredentials.js"
        code = fixture.read_text(encoding="utf-8")
        self.assertIn("@example.invalid", code)
        self.assertEqual(1, code.count("Date.now()"))
        self.assertIn("output.credentials =", code)
        self.assertNotIn("@test.com", code)
        self.assertNotIn("fetch(", code)
        self.assertNotIn("http.post(", code)

    def test_remocao_de_binarios_duplicados_preserva_referencia(self):
        self.assertTrue((SAMPLES / "wikipedia.apk").is_file())
        self.assertTrue((SAMPLES / "wikipedia.zip").is_file())
        self.assertFalse((SAMPLES / "sample.apk").exists())
        self.assertFalse((SAMPLES / "sample.zip").exists())


    def test_fixture_login_offline(self):
        fixture = SAMPLES / "wikipedia-android-advanced/scripts/fetchTestUser.js"
        texto = fixture.read_text(encoding="utf-8")
        self.assertIn("example.invalid", texto)
        self.assertIn("maestro_demo_not_a_real_account", texto)
        for proibido in ("http.get(", "http.post(", "fetch(", "axios.", "jsonplaceholder.typicode.com"):
            self.assertNotIn(proibido, texto)

    def test_login_e_cadastro_nao_enviam_credenciais(self):
        checks = (
            ("auth/login.yml", "../scripts/fetchTestUser.js"),
            ("auth/signup.yml", "../scripts/generateCredentials.js"),
        )
        for relative_path, script in checks:
            path = SAMPLES / "wikipedia-android-advanced" / relative_path
            docs = list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
            commands = docs[1]
            self.assertIn(script, [item.get("runScript") for item in commands if isinstance(item, dict)])
            self.assertEqual(commands[-2:], ["back", "back"])
            for item in commands:
                if isinstance(item, dict) and "tapOn" in item:
                    target = str(item["tapOn"]).casefold()
                    self.assertFalse(any(label in target for label in ("submit", "sign up", "sign in", "create your account")))



if __name__ == "__main__":
    unittest.main()
