---
name: saude-wearables
description: Extrair e analisar dados de dispositivos vestíveis (wearables) do projeto Saúde — smartwatches e rastreadores de atividade — correlacionando frequência cardíaca de repouso, sono, variabilidade da FC (VFC), passos e métricas cardiorrespiratórias. Use ao processar dados de dispositivos vestíveis.
---

# Dispositivos Vestíveis (Wearables) → Registro Mestre §7.8

> **Nota de Privacidade:** Todos os parâmetros, datas e métricas citados são **100% sintéticos e fictícios**.

Registro: núcleo `<PASTA_SAUDE>/Registro_Mestre_Demo.md` (§7.8) + `REGISTRO/07_Wearables.md` (§7.8); ler antes. Relatório de referência: `Analise_Wearables_Exemplo.md`. Scripts em `<PASTA_SAUDE>/analise_wearables/`.

## Fluxo de Processamento

1. Armazenar as exportações periódicas nas pastas dedicadas de dados brutos (`DADOS_DISPOSITIVO_A/` e `DADOS_DISPOSITIVO_B/`).
2. Processar os arquivos de dados em streaming para extrair séries de frequência cardíaca em repouso, qualidade do sono e sessões de exercício.
3. Analisar tendências por blocos temporais ou fases de protocolo:
   - Fase 1: Período basal de condicionamento inicial.
   - Fase 2: Período de adaptação e intensificação.
   - Fase 3: Período sob intervenção ativa com Medicação A ou Protocolo B.
   - Fase 4: Período pós-intervenção e consolidação.

## Cuidados Metodológicos e Armadilhas Conhecidas

- **Prevenção de Dupla Contagem:** Empregar exclusivamente os dados provenientes do dispositivo de pulso principal para evitar sobreposição de contagens geradas por sensores integrados secundários do telefone.
- **Incompatibilidade Direta entre Métricas de VFC:** Algoritmos de fabricantes diferentes utilizam estimativas matemáticas distintas (ex.: SDNN versus rMSSD). Não converter nem comparar valores brutos entre marcas distintas; acompanhar curvas de tendência exclusivamente dentro do mesmo ecossistema.
- **Registros Eletrocardiográficos Pontuais:** Registros de ritmo sinusal ou alertas de frequência cardíaca elevada devem ser documentados com data, horário e circunstância de repouso ou estresse.
- **Recuperação de Pesagens:** Dados de peso transmitidos via integração de balanças inteligentes devem ser conferidos com as diretrizes do protocolo matinal da skill `saude-balancas`.

## Diretrizes de Interpretação e Privacidade

- **Foco Estritamente Informativo:** Métricas de frequência cardíaca de repouso, VFC e arquitetura de sono constituem parâmetros de acompanhamento geral de bem-estar. Eventuais sintomas cardiovasculares (palpitações, desconforto torácico, tonturas) demandam avaliação médica imediata junto ao profissional assistente (Profissional Assistente A).
- **Tratamento Local:** Informações fisiológicas de sensores pessoais permanecem no ambiente local do usuário, sem transmissão para serviços externos de processamento.

## Gravação

Registrar a nova linha de síntese em §7.8, Painel Resumo, Padrões e Log conforme as diretrizes da skill `saude-registro`.
