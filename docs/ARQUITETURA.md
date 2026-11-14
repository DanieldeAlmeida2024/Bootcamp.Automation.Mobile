# Arquitetura — automação Wikipedia com Maestro

Versão 1.1.0 — 14/11/2026

## Componentes

- **Maestro CLI** interpreta YAML e interage com aplicativo instalado no dispositivo/emulador.
- **Smokes** (`samples/android-flow.yaml`, `samples/ios-flow.yaml`) iniciam o aplicativo com `clearState` e verificam controles da tela.
- **Fluxos avançados** coordenam onboarding, interação com a busca e subfluxos.
- **Scripts auxiliares** em `samples/scripts/` e `samples/wikipedia-android-advanced/scripts/` preparam textos e dados fictícios; parte dos exemplos avançados usa rede externa.
- **CI Python** valida os arquivos de fluxo e as referências entre eles, com PyYAML. Não inicializa dispositivos.

## Decisões

Os apps reais dos exemplos são Wikipedia Android `org.wikipedia` e Wikipedia iOS `org.wikimedia.wikipedia`. Seletores são específicos da versão do aplicativo e podem falhar se a interface mudar.

Foram removidos passos opcionais que tocavam em um elemento declarado inexistente. Nos testes básicos, o simples lançamento foi substituído por verificações de onboarding. Cópias binárias idênticas foram eliminadas sem reescrever o histórico do Git.

## Limites

Não há CI E2E com emulador, atestado de funcionamento das versões atuais dos aplicativos nem cobertura de todos os caminhos. Uma falha de seletor é um problema funcional real a ser investigado manualmente, não motivo para enfraquecer asserts.
