# Versionamento — Bootcamp.Automation.Mobile

## MOBILE-QA 1.2.0 · 14/11/2026

- Troca a consulta pública ao JSONPlaceholder por fixture local determinística de usuário inexistente.
- O subfluxo de login exercita entrada no formulário, **sem enviar credenciais falsas ao serviço Wikipedia**.
- Testes estruturais verificam que o fluxo usa fixture offline, sem `http.get` e sem submeter formulário.
- Documentação específica de teste e README atualizados.

**Evidência exigida:** CI Python/PyYAML. Nenhuma execução Maestro em Android/iOS é declarada concluída; os testes de dispositivo permanecem pendentes.

## Histórico

As versões anteriores usam a fixture remota didática. Este commit não modifica APKs, ZIPs, outras telas ou a configuração de dispositivos.
