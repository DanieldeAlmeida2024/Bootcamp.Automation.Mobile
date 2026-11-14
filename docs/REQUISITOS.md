# Requisitos — laboratório de automação mobile Wikipedia

Versão 1.1.0 — 14/11/2026

- **RF01:** executar um fluxo básico por plataforma que inicia a Wikipedia e confirma elementos visíveis de onboarding.
- **RF02:** executar fluxos avançados com navegação, busca e subfluxos independentes.
- **RF03:** declarar o `appId` correto de cada plataforma em todos os arquivos YAML.
- **RF04:** manter referências válidas de scripts e subfluxos.
- **RNF01:** executar os fluxos reais com Maestro e dispositivo/emulador preparado.
- **RNF02:** validar estrutura dos YAML em CI de forma offline.
- **RNF03:** preservar a integridade e a proveniência de arquivos de demonstração, sem cópias binárias idênticas na árvore corrente.
- **RNF04:** não tratar a validação estática como teste end-to-end nem afirmar que o aplicativo iFood foi testado.

Riscos: atualização da interface Wikipedia; variação de idioma; onboarding dependente de estado; dependências de rede em alguns exemplos avançados; configuração de simulador Apple em macOS para iOS.
