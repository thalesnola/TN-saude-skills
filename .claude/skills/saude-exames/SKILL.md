---
name: saude-exames
description: Incorporar laudos de exames laboratoriais (PDF ou imagem) ao Registro Mestre do projeto Saúde. Use quando surgir arquivo novo em DADOS_GERAIS/exames, ou para tabular, comparar e correlacionar biomarcadores laboratoriais.
---

# Exames Laboratoriais → Registro Mestre

> **Nota de Privacidade:** Todos os parâmetros, datas e valores citados são **100% sintéticos e fictícios**.

Registro: leia o núcleo `<PASTA_SAUDE>/Registro_Mestre_Demo.md` e `REGISTRO/08_Exames.md` (§8), `REGISTRO/06_Medicacao.md` (§6) e `REGISTRO/09_Padroes_e_Licoes.md` (§13) antes. Exames são tabulados em `08_Exames.md` (§8.1 tabela, §8.2 análise clínica); sem planilhas paralelas. Documento de referência contextual: `Analise_Historico_Exames_Exemplo.md`.

## Fluxo de Processamento

1. **Extração de Texto do Laudo:**
   - Executar: `python <PASTA_SAUDE>/.claude/skills/saude-exames/extrai_exame.py <PASTA_SAUDE>/DADOS_GERAIS/exames`
   - O utilitário gera os arquivos estruturados em `exames/_texto/<nome>.txt` (via extração UTF-8 ou OCR automatizado para páginas digitalizadas em imagem).
   - Imagens ou fotos de laudos devem ser conferidas com o documento original e marcadas para verificação.
2. **Estruturação de Dados do Laudo:**
   - Mapear analito, valor medido, unidade de medida, intervalo de referência do próprio laudo emissor, método analítico, data da coleta e laboratório responsável.
3. **Inclusão na Série Histórica:**
   - Adicionar uma nova coluna datada na tabela §8.1 sem sobrescrever lançamentos prévios.
   - Sinalizar analitos fora da faixa recomendada utilizando marcadores visuais padronizados (🔴 para desvios significativos, ⚠️ para valores limítrofes, ✅ para conformidade).
4. **Conferência Prévia:**
   - Validar se a unidade de medida confere com a série histórica (aplicar conversão formal quando houver mudança de unidade entre laboratórios).
   - Registrar eventuais mudanças de metodologia analítica em notas de rodapé.
5. **Atualizações de Governança:**
   - Atualizar a Cronologia (§10), o quadro de Pendências (§11), a Agenda (§12), o Painel Geral (§1) e o Log de Versão (§16).

## Princípios Metodológicos e de Segurança

- **Primazia do Laudo Original:** Em caso de divergência com anotações manuais ou resumos, prevalece sempre a leitura estrita do laudo oficial emitido pelo laboratório.
- **Comparabilidade Metodológica:** Comparar prioritariamente resultados obtidos sob a mesma metodologia e, preferencialmente, pelo mesmo laboratório.
- **Correlação com o Contexto Fisiológico:** Registrar o intervalo de tempo decorrido desde a última dose de intervenções clínicas ativas (Medicação A ou Protocolo B), bem como esforço muscular extenuante recente (≤ 48 horas) e suplementação de suporte.
- **Caráter Estritamente Educacional:** A interpretação diagnóstica e a conduta terapêutica de qualquer alteração cabem exclusivamente aos profissionais de saúde assistentes: médico assistente (Profissional Assistente A) e nutricionista assistente (Profissional Assistente B).
- **Sigilo de Dados Pessoais:** Nenhum número de documento de identificação pessoal, endereço, telefone ou código de acesso de laudo deve constar no Registro Mestre.
- **Processamento Local:** Arquivos e laudos médicos são processados estritamente na estação de trabalho local.
