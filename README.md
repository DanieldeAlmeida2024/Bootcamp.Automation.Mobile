# Testes mobile com Maestro — laboratório Wikipedia

Exercícios de automação de interface para Android e iOS usando **Maestro**. Os fluxos que estão neste repositório usam o aplicativo **Wikipedia** — `org.wikipedia` no Android e `org.wikimedia.wikipedia` no iOS —, não o aplicativo iFood.

## Primeiro teste

Pré-requisitos: Maestro CLI instalado, app Wikipedia instalado no dispositivo ou emulador e um ambiente Android/iOS compatível.

```bash
maestro test samples/android-flow.yaml
```

O fluxo Android limpa o estado do aplicativo e verifica a presença dos controles de onboarding `Continue` e `Skip`. Esses controles podem variar conforme a versão/idioma da Wikipedia. Para iOS:

```bash
maestro test samples/ios-flow.yaml
```

Os exemplos avançados ficam em `samples/android-advanced-flow.yaml`, `samples/ios-advanced-flow.yaml` e `samples/wikipedia-android-advanced/run-test.yml`. Eles exercitam navegação, busca e subfluxos. O último contém exemplos de cadastro e login **didáticos**, não uma autenticação homologada.

## Validação automática no GitHub Actions

```bash
python -m pip install PyYAML==6.0.2
python -m unittest discover -s tests -p 'test_*.py' -v
```

A CI confere estrutura YAML, identificadores de aplicativos, integridade das referências a scripts e subfluxos, presença de verificações no smoke test e ausência de binários redundantes. **Não executa Maestro em Android/iOS:** não há emulador configurado no pipeline. A aprovação desse CI não deve ser apresentada como teste mobile E2E aprovado.

## Organização dos exemplos

- `samples/android-flow.yaml` e `samples/ios-flow.yaml`: smoke tests com asserts.
- `samples/*-advanced-flow.yaml`: navegação e busca em Wikipedia.
- `samples/subflows/`: onboarding e limpeza de estado.
- `samples/wikipedia-android-advanced/`: cenário composto de demonstração.
- `samples/wikipedia.apk` e `samples/wikipedia.zip`: artefatos de exemplo para execução dos fluxos em ambiente controlado.

Estes arquivos incluem conteúdo de demonstração; use contas e dados fictícios. A execução em dispositivo exige conferir a versão do aplicativo e os seletores dos fluxos.

## Documentação

[Arquitetura](docs/ARQUITETURA.md) · [Requisitos](docs/REQUISITOS.md) · [Plano de testes](docs/PLANO_TESTES.md) · [UML](docs/UML.puml)

*Laboratório didático com Maestro e aplicativo Wikipedia. A autoria do framework e dos aplicativos testados pertence aos respectivos mantenedores.*

## Fluxo de login sem dependência externa

O exemplo composto em `samples/wikipedia-android-advanced/` utiliza agora um usuário fictício da fixture local JavaScript, sem acessar o JSONPlaceholder nem compartilhar dados de terceiros. O subfluxo `auth/login.yml` demonstra **apenas o preenchimento do formulário**: não envia senha ou tentativa de autenticação ao serviço público da Wikipedia.

Isso evita depender da disponibilidade e do conteúdo de uma API externa e não tenta representar login real como aprovado. O teste estrutural verifica a fixture local, o domínio `example.invalid` e a ausência de submissão automática. Ainda é necessário executar Maestro manualmente num dispositivo/emulador para validar seletores e navegação.
