---
name: saude-treino
description: Transcrever e analisar registros e relatórios de treino físico para o Registro Mestre §7.7 — tonelagem por sessão e semana, frequência, exercícios âncora de força e correlações com recuperação e biomarcadores. Use ao analisar dados de treinamento ou progressão de força.
---

# Treinamento Físico e Força → Registro Mestre §7.7

> **Nota de Privacidade:** Todos os parâmetros, exercícios e séries citados são **100% sintéticos e fictícios**.

Registro: núcleo `<PASTA_SAUDE>/Registro_Mestre_Demo.md` (§7.7 e Padrões) + `REGISTRO/07_Treino.md` (§7.7); ler antes. Registros em `DADOS_TREINO/`.

## Fluxo de Processamento

1. **Ingestão e Estruturação de Dados:**
   - Registrar as sessões no arquivo estruturado de treino (`DADOS_TREINO/treino_aulas_transcrito.csv`), contendo: identificador da sessão, data, grupamento muscular, semana do ciclo, intensidade percentual prescrita, séries/repetições, carga total consolidada e status.
2. **Prioridade de Totais Consolidados:**
   - Os totais finais registrados ao término da sessão prevalecem sobre anotações parciais de exercícios isolados.
3. **Classificação de Status da Sessão:**
   - Classificar como `ok` (sessão cumprida integralmente) ou `incompleta`. Sessões incompletas não devem distorcer médias comparativas semanais.
4. **Métricas de Volume e Frequência:**
   - Calcular tonelagem semanal por grupamento e frequência de dias distintos de estímulo.
5. **Correlações com Marcadores Fisiológicos:**
   - Cruzar o volume de treino com registros de frequência cardíaca de repouso e qualidade do sono, bem como com enzimas musculares (CPK, transaminases) coletadas em até 48 horas após esforços de alta intensidade.

## Interpretação Metodológica

- Cargas registradas devem refletir a resistência efetiva do implemento ou aparelho.
- Variações normais de exercícios ao longo de periodizações não devem ser interpretadas como perda de força; recomenda-se eleger **3 a 5 exercícios âncora fixos** para acompanhar progressão de sobrecarga ao longo do tempo.
- Qualquer queixa musculoesquelética ou dor articular atípica deve ser registrada em pendências para avaliação com profissionais de ortopedia ou fisioterapia.
- O caráter deste acompanhamento é informativo e educacional, cabendo a prescrição e a progressão de cargas a profissionais habilitados de educação física e ao médico assistente (Profissional Assistente A).

## Gravação

Registrar a tabela semanal em §7.7, Painel Resumo, Pendências e Log conforme as diretrizes da skill `saude-registro`.
