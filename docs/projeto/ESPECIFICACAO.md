# Fluxos de teste mobile Maestro — Wikipedia Android/iOS

**v1.0.0**, 11/11/2026. `main` auditada @ `8f80fc71bd461eb35215ca7ee459932e0bd40389`; casos não executados aqui.

## Missão e abordagem
Maestro YAML para automação de interface Android e iOS, com appId org.wikipedia nos fluxos Android e exemplos separados de onboarding, autenticação e navegação.

## Arquivos de teste e comportamento real
| Arquivo/cenário | Ação/contrato | Verificação técnica |
|---|---|---|
| `samples/wikipedia-android-advanced/run-test.yml` | Executa launchApp clearState, onboarding/main.yml, dashboard/main.yml, auth/signup.yml e auth/login.yml em sequência. | Validar ordem das subflows e estado do aplicativo. |
| `samples/wikipedia-android-advanced/auth/login.yml` | Navega More → LOG IN, busca usuário por fetchTestUser.js e insere senha de exemplo No provided. | Não afirmar que esta senha efetua login válido; testar comportamento de erro. |
| `samples/wikipedia-android-advanced/onboarding/*` | Fluxos de adição/remoção de idioma e primeira inicialização. | Testar permissão e variações de locale. |
| `samples/wikipedia-android-advanced/dashboard/*` | Fluxos de feed, busca, cópia/colagem e itens salvos. | Executar com app Wikipedia compatível. |
| `samples/android-advanced-flow.yaml e samples/ios-advanced-flow.yaml` | Exemplos de fluxos mobile das duas plataformas. | Marcar casos por OS e versão da aplicação. |

## Fluxo de execução
```bash
maestro test samples/wikipedia-android-advanced/run-test.yml
```

## Riscos, isolamento e limitações
O pacote contém APKs de amostra e scripts de dados de teste; isso não comprova cobertura iOS/Android. IDs de elementos, gestos e idioma dependem da versão do app e dispositivo/emulador. Não executar autenticação real com credenciais de terceiros.

Os arquivos são scripts de automação, não uma aplicação de negócio. Os critérios precisam identificar versão da ferramenta, URL/appId e resultado observável; não inventar banco ou backend interno.
