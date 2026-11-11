# Plano de testes — Bootcamp.Automation.Mobile

**v1.0.0**, 11/11/2026. `main` auditada @ `8f80fc71bd461eb35215ca7ee459932e0bd40389`; casos não executados aqui.

## Matriz rastreável
| ID | Arquivo/cenário | Expectativa | Situação |
|---|---|---|---|
| QA-01 | `samples/wikipedia-android-advanced/run-test.yml` | Validar ordem das subflows e estado do aplicativo. | Requer execução |
| QA-02 | `samples/wikipedia-android-advanced/auth/login.yml` | Não afirmar que esta senha efetua login válido; testar comportamento de erro. | Requer execução |
| QA-03 | `samples/wikipedia-android-advanced/onboarding/*` | Testar permissão e variações de locale. | Requer execução |
| QA-04 | `samples/wikipedia-android-advanced/dashboard/*` | Executar com app Wikipedia compatível. | Requer execução |
| QA-05 | `samples/android-advanced-flow.yaml e samples/ios-advanced-flow.yaml` | Marcar casos por OS e versão da aplicação. | Requer execução |

## Riscos e regressão
- QA-N01: indisponibilidade de site/aplicativo; distinguir falha de infraestrutura de defeito de produto.
- QA-N02: selectors/elementos alterados; salvar vídeo/screenshot e identificar plataforma.
- QA-N03: limpar estado de sessão antes de cada repetição, não modificar contas reais.
- QA-N04: repetir em versão atualizada da ferramenta e comparar resultados.

## Execução e evidências
```bash
maestro test samples/wikipedia-android-advanced/run-test.yml
```

Salvar logs, capturas, tempo, versão de navegador/emulador, commit, resultado e taxa de intermitência. Testes de documentação Python existentes não são testes E2E reais.
