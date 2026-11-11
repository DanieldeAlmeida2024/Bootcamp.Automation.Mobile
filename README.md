# Bootcamp.Automation.Mobile

Automação de testes de interface Android/iOS com fluxos Maestro em YAML.

## Tecnologias
Maestro CLI, Android Studio, APK de demonstração.

## Executar
```bash
maestro test samples/android-flow.yaml
```

**Pré-condições:** Requer APK instalado em dispositivo/emulador, não testado via conector GitHub.

## Documentos
- [Requisitos](docs/REQUISITOS.md)
- [Arquitetura](docs/ARQUITETURA.md)
- [UML](docs/UML.puml)
- [Testes](docs/PLANO_TESTES.md)
- [Instruções para IA](AGENTS.md)

## README original preservado

## Automação de testes Mobile com Maestro
- Neste projeto é feito a automação de teste de qualidade de uma aplicação android parecida com a plataforma do ifood, para fins didáticos

#### Requisitos
- Android Studio
- Maestro Dev
- Terminal / CMD
- Um computador que suporte os requisitos do emulador

#### Execução
  - Executar o comando maestro download-samples no projeto para baixar a biblioteca
  - Abrir pasta do projeto no Android Studio e emular um dispositivo android.
  - Instalar a aplicação a ser testada no emulador
  - Ao emular será executado o comando maestro studio que iniciará um serviço local web para configuração. Todos os testes e resultados são exibidos lá!.

## Documentação detalhada (v1.0.0)

[Projeto](docs/projeto/ESPECIFICACAO.md) · [UML](docs/uml/README.md) · [Plano QA](docs/testes/PLANO_DE_TESTES.md) · [Versões](docs/controle/VERSIONAMENTO.md)
