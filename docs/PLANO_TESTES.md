# Plano de testes

T01: cenário válido com ambiente preparado.

T02: dados inválidos / aplicativo ausente.

T03: falha ou indisponibilidade de dependência externa.

T04: estrutura da documentação.

Execução funcional:
```bash
maestro test samples/android-flow.yaml
```

Execução documental:
```bash
python -m unittest discover -s tests -p test_documentacao.py -v
```

**Importante:** o teste documental não garante aprovação de testes funcionais.
