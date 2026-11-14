# Plano de testes — automação mobile Wikipedia

Versão 1.1.0 — 14/11/2026

## CI estático, executado em GitHub Actions

```bash
python -m pip install PyYAML==6.0.2
python -m unittest discover -s tests -p 'test_*.py' -v
```

| ID | Validação | Resultado esperado |
| --- | --- | --- |
| YAML-01 | Analisar todos os `.yaml` e `.yml` | Metadados `appId`, separador e comandos bem formados |
| YAML-02 | Resolver `runFlow` e `runScript` | Referência aponta para arquivo existente dentro de `samples/` |
| YAML-03 | Verificar `android-flow` e `ios-flow` | `clearState` e `assertVisible` estão definidos |
| YAML-04 | Inspecionar fluxos avançados | Nenhum toque fictício em `Non existent view` |
| FILE-01 | Verificar binários | Mantém `wikipedia.apk/zip`, remove `sample.apk/zip` duplicados |

## Execução E2E manual obrigatória

- Android: `maestro test samples/android-flow.yaml`, depois `maestro test samples/android-advanced-flow.yaml`.
- iOS em macOS com simulador/app apropriado: `maestro test samples/ios-flow.yaml`, depois `maestro test samples/ios-advanced-flow.yaml`.
- Wikipedia Android composta: `maestro test samples/wikipedia-android-advanced/run-test.yml`.

Critérios: app instalado, versão identificada, comandos `tapOn` e `assertVisible` aprovados, erros e evidências capturados. **Esses testes não estão cobertos pelo workflow atual**, e seu resultado não deve ser indicado como aprovado antes de execução em dispositivo.
