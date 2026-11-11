---
name: saude-receitas
description: Incorporar prescrições e orientações clínicas (PDF em DADOS_GERAIS/receitas) ao Registro Mestre do projeto Saúde — compostos, posologias didáticas, quantidades, calendário de término e aplicações — e correlacionar com exames, wearables, composição e treino. Use quando houver novas orientações clínicas a catalogar.
---

# Prescrições e Orientações Clínicas → Registro Mestre

> **Nota de Privacidade:** Todos os parâmetros, datas e posologias citados são **100% sintéticos e fictícios**.

Registro: leia o núcleo `<PASTA_SAUDE>/Registro_Mestre_Demo.md` (§11 pendências) e `REGISTRO/06_Medicacao.md` (§6) antes; para correlações, o arquivo temático em `REGISTRO/`; gravar com a skill `saude-registro`. Modelo de análise: `<PASTA_SAUDE>/Analise_Receitas_Exemplo.md`.

## Fluxo de Processamento

1. **Leitura do Documento Original** (`pdftotext -layout -enc UTF-8`):
   - Extrair a relação de itens prescritos, vias de administração, posologias e quantitativos totais.
   - Atentar para vias de controle especial para não duplicar contagens de itens repetidos por exigência regulatória.
2. **Estruturação da Tabela por Item:**
   - Composto ou princípio ativo didático, dose diária, posologia, **quantidade prescrita** e data da orientação.
   - Diferenciar itens iniciados, itens mantidos e itens descontinuados em relação ao ciclo anterior.
3. **Cálculo de Duração por Quantitativo:**
   - Calcular a estimativa de término com base na relação matemática: `embalagens (ou doses unitárias) ÷ posologia diária`.
   - Distinguir término natural de quantitativo dispensado de suspensão terapêutica deliberada.
4. **Alinhamento com o Relato do Usuário:**
   - Registrar datas reais de início, conclusão de ciclos ou ajustes posológicos conforme informado, diferenciando datas registradas em receituário de datas efetivas de adesão.
5. **Atualizações de Controle:**
   - Atualizar tabelas em §6, Cronologia (§10), Pendências (§11), Agenda (§12), Painel Geral (§1) e Log de Versão (§16).

## Correlações Clínicas Recomendadas

- **Exames Laboratoriais (§8):** Verificar a fase de exposição farmacológica na data da coleta (tempo decorrido desde a última dose, estado de equilíbrio ou vale terapêutico). Distinguir alterações laboratoriais induzidas por fármacos de variações puramente dietéticas ou ponderais.
- **Dispositivos Wearables (§7.8):** Acompanhar frequência cardíaca basal de repouso, sono e variabilidade da frequência cardíaca durante diferentes fases de protocolos clínicos ou suplementares.
- **Composição Corporal e Bioimpedância (§7.1–7.6):** Considerar que substâncias que promovem retenção hidroeletrolítica intracelular ou extracelular influenciam leituras de bioimpedância, sendo lidas temporariamente como oscilação de massa isenta de gordura.
- **Treinamento Físico (§7.7):** Correlacionar capacidade de esforço e recuperação com as fases de suporte nutricional ou ergogênico.
- **Interações e Farmacovigilância:** Observar potenciais interações metabólicas e necessidade de monitoramento de enzimas e marcadores de segurança.

## Diretrizes de Segurança e Privacidade

- **Caráter Estritamente Educacional:** Análises e correlações têm finalidade de documentação e suporte informativo. Decisões clínicas, prescrições, ajustes de dosagem ou descontinuação de terapias cabem exclusivamente ao médico assistente (Profissional Assistente A) e à nutricionista assistente (Profissional Assistente B).
- **Sigilo Absoluto:** Nenhum dado pessoal de identificação, CPF, endereço, telefone, código de rastreamento ou token eletrônico de receituário deve constar no Registro Mestre ou em relatórios.
- **Armazenamento Local:** Informações e documentos de saúde permanecem restritos ao ambiente local do usuário.
