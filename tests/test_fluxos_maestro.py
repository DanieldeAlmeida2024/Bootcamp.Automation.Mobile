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

    def test_remocao_de_binarios_duplicados_preserva_referencia(self):
        self.assertTrue((SAMPLES / "wikipedia.apk").is_file())
        self.assertTrue((SAMPLES / "wikipedia.zip").is_file())
        self.assertFalse((SAMPLES / "sample.apk").exists())
        self.assertFalse((SAMPLES / "sample.zip").exists())


if __name__ == "__main__":
    unittest.main()
