# Arquitetura — Bootcamp.Automation.Mobile

**Objetivo:** Automação de testes de interface Android/iOS com fluxos Maestro em YAML.

**Tecnologias:** Maestro CLI, Android Studio, APK de demonstração.

Fluxo: entrada → validação → execução do cenário → saída/relatório. Integrações externas são dependências, não são simuladas como fatos operacionais.

Decisões: preservar stack e fontes didáticas, isolar dependências onde viável, manter documentação e testes separados de implementação, validar comportamento em ambiente real antes de publicação.

Limite: Requer APK instalado em dispositivo/emulador, não testado via conector GitHub.
