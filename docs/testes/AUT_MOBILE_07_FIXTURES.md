# AUT-MOBILE-07 — Fixtures de cadastro e arquivos de IDE

14/11/2026 · Testes Maestro do aplicativo Wikipedia em dispositivo de estudo.

## Achado
O script de cadastro de demonstração usava um endereço @test.com (domínio real) e gerava timestamps separadamente para usuário, e-mail e senha, podendo formar identificadores inconsistentes se o relógio avançasse entre funções. Arquivos específicos de IntelliJ/IDE também estavam versionados.

## Ação
- Os três campos agora compartilham um único sufixo local; e-mail usa domínio reservado example.invalid, explicitamente não entregável.
- O CI estático verifica que o script não possui chamadas HTTP nem usa domínio real.
- Removidos seis arquivos .idea do Git e adicionadas regras de ignore, sem apagar APK/ZIP de referência usados no laboratório.

## Limites
Os fluxos continuam preenchendo apenas formulários, sem submeter cadastro real. GitHub Actions não executa Android/iOS emulador; os seletores visuais permanecem sem homologação em dispositivos.
