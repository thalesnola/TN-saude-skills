---
name: saude-balancas
description: Incorporar leituras de balança e bioimpedância (BIA Doméstica, Bioimpedância Clínica Octapolar e BIA de Academia) ao Registro Mestre e interpretar o que é válido metodologicamente em cada aparelho. Use quando receber leituras de balança ou laudos de bioimpedância.
---

# Balanças e Bioimpedância → Registro Mestre

> **Nota de Privacidade:** Todos os parâmetros, datas e valores citados são **100% sintéticos e fictícios**.

Registro: núcleo `<PASTA_SAUDE>/Registro_Mestre_Demo.md` (Regras 1 e 3, §5) + `REGISTRO/07_Balancas.md` (§7.1, §7.3–7.5) + `REGISTRO/09_Padroes_e_Licoes.md`; ler antes.

## Interpretação Metodológica por Equipamento (§5)

- **Balança BIA Doméstica Atual:** Referência primária de peso corporal e tendência de composição doméstica diária. Pesagens padronizadas seguem a Regra 3 (manhã, jejum). Valores de percentual de gordura e massa magra são interpretados prioritariamente como curva de tendência interna do aparelho.
- **Balança BIA Doméstica Antiga (Histórico):** Série mantida para continuidade longitudinal de médias semanais em condições padronizadas.
- **Bioimpedância Clínica Octapolar (S/N DEMO-0001):** Âncora clínica de composição corporal. Fatores de hidratação e retenção hídrica sistêmica devem ser considerados para não confundir variações de água extracelular com hipertrofia muscular real.
- **Balança BIA de Academia:** Útil para peso e direção da gordura visceral; valores de impedância segmentar devem ser registrados como dado primário quando disponíveis.
- **Comparação entre Aparelhos:** Aparelhos com tecnologias, frequências e equações distintas não devem ser convertidos diretamente entre si; comparações são feitas exclusivamente lado a lado como desvio relativo ou curva de tendência individual.

## Protocolo de Leitura Doméstica

1. Extrair data, hora, peso, IMC estimado, %G, massa muscular, água corporal, taxa metabólica basal e índice visceral.
2. Registrar como Leitura Padrão (`P`) apenas medições matinais em jejum completo e após esvaziamento vesical (Regra 3); leituras em outros horários recebem marcador de leitura não padronizada (`N`).
3. Variações agudas de peso corporal (1 a 2 kg em 24 a 48 horas) refletem primariamente balanço hídrico e conteúdo de glicogênio muscular.
4. Ritmo de perda ou ganho ponderal deve ser calculado sobre intervalos médios com pontos estritamente padronizados (`P`).

## Bioimpedância Clínica e Multifrequencial: Novo Laudo

- Registrar número de série do equipamento (ex.: S/N DEMO-0001), data, horário e conformidade com o preparo clínico prévio.
- Registrar a impedância bruta por frequência e segmento corporal quando fornecida pelo equipamento (frequências de 5, 50 e 250 kHz).
- Conferência de plausibilidade biológica: variações extremas de massa gorda em janelas temporais curtas sugerem variações de condutividade ou hidratação, não alteração tecidual pura.

## Sessão de Pareamento Matinal entre Aparelhos

Objetivo: mensurar o **desvio instrumental relativo** entre dois equipamentos no mesmo indivíduo, sem tentar forçar equivalência absoluta de fórmulas proprietárias.
1. Condições de preparo estritamente idênticas (Regra 3): ao acordar, em jejum matinal completo, sem ingestão de água ou alimentos e sem exercício prévio.
2. Ordem de subida e intervalo em minutos entre os aparelhos devidamente documentados.
3. Repetições na balança doméstica para obtenção de mediana estável.
4. Análise de desvio de calibração em quilogramas (peso na balança A vs peso na balança B) e comparação lado a lado dos indicadores de composição.

## Gravação Estruturada

Registrar a nova leitura na tabela temática em §7; atualizar Cronologia §10, Painel §1, Pendências §11 e Log §16 conforme os padrões da skill `saude-registro`.
