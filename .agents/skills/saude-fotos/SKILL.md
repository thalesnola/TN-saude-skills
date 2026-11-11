---
name: saude-fotos
description: Analisar fotos e vídeos corporais padronizados do projeto Saúde (pasta FOTOS/MES_EXEMPLO) e correlacioná-los com antropometria, cintura, peso e composição no Registro Mestre. Use quando houver novos registros visuais padronizados para comparar entre períodos.
---

# Avaliação Fotográfica Corporal → Registro Mestre

> **Nota de Privacidade:** Todos os parâmetros, datas e valores citados são **100% sintéticos e fictícios**.

Registro: leia o núcleo `<PASTA_SAUDE>/Registro_Mestre_Demo.md` (§4 protocolo de fotos, Regra 4) + `REGISTRO/07_Fotos.md` (§7.9) e `REGISTRO/07_Cintura_Antropometria.md` (§7.2, §7.6) antes. Documentação fotográfica é tabulada em `07_Fotos.md` (§7.9).

## Fluxo de Processamento

1. **Preparação Local de Imagens:**
   - Executar: `python <PASTA_SAUDE>/.claude/skills/saude-fotos/prepara_fotos.py <PASTA_SAUDE>/FOTOS/<pasta>`
   - O script padroniza formatos (HEIC para JPG), ajusta rotações, extrai quadros relevantes de vídeos e compõe pranchas com registro de data/hora EXIF e hash de integridade SHA256 em diretório temporário isolado.
   - Os arquivos de trabalho temporários devem ser excluídos ao final do procedimento de análise.
2. **Critérios Estritos de Padronização:**
   - Conferência de horário matinal em jejum, distância focal padronizada, iluminação homogênea, enquadramento corporal completo e quatro poses neutras relaxadas (frente, perfil direito, costas e perfil esquerdo).
   - Registros com variações relevantes de distância ou ângulo devem ser catalogados como fotos informativas preliminares, não como pontos de série longitudinal estrita.
3. **Contextualização Fisiológica do Dia:**
   - Correlacionar com a pesagem matinal padronizada mais próxima na balança doméstica, com a média da circunferência abdominal em 3 níveis e com o cronograma ativo de intervenções clínicas.
4. **Análise Morfológica Comparativa:**
   - Inspeção por regiões anatômicas (tronco, abdômen, membros superiores e inferiores) correlacionada com as grandezas métricas correspondentes (espessura de dobras em mm e circunferências).
5. **Gravação Estruturada:**
   - Registrar nova seção em §7.9; atualizar Cronologia (§10), Pendências (§11), Agenda (§12), Painel Geral (§1) e Log de Versão (§16).

## Princípios Metodológicos e de Sigilo

- **Caráter Estritamente Educacional:** A inspeção fotográfica serve como conferência de plausibilidade morfológica, não constituindo avaliação diagnóstica. Quaisquer observações anatômicas pertinentes devem ser discutidas com os profissionais assistentes (Profissional Assistente A e Profissional Assistente B).
- **Preservação de Privacidade:** Imagens corporais são processadas exclusivamente na máquina local, com omissão de feições faciais e sem inclusão de qualquer dado pessoal identificável nos relatórios.
- **Limitações da Avaliação Visual:** Fotografias isoladas não mensuram massa magra ou gordura visceral de forma direta; variações de iluminação, hidratação ou postura exercem influência substancial sobre a impressão visual.
