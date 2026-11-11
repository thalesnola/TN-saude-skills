# Projeto Saúde — Mapa de Pastas e Governança de Skills

> **Nota de Privacidade:** Todos os parâmetros, diretórios e exemplos são **100% sintéticos e fictícios**.

**Antes de qualquer análise, ler o núcleo `Registro_Mestre_Demo.md` inteiro** (painel, regras, perfil sintético, protocolo, pendências abertas, agenda) e **só o arquivo do tema** em `REGISTRO/` (séries, exames, medicação, cronologia, padrões, log). Não ler a pasta inteira por hábito. Dado novo entra **só no Registro** (núcleo + `REGISTRO/`); não criar planilhas paralelas. Conteúdo estritamente educacional, não diagnóstico; orientações clínicas dependem de avaliação profissional assistente.

## Estrutura de Diretórios Recomendada

| Pasta | Conteúdo | Observação |
|---|---|---|
| `DADOS_GERAIS/exames/` | PDFs e fotos de laudos laboratoriais | Padrão: `Exames_AAAA-MM-DD_<lab>.pdf`. O texto extraído fica em `_texto/` (gerado automaticamente) |
| `DADOS_GERAIS/receitas/` | Prescrições e orientações clínicas | |
| `DADOS_GERAIS/nutricao/` | Planejamento dietético e nutricional | |
| `DADOS_ANTROPOMETRIA/` | Medidas de sessões antropométricas | `medidas-antropometricas-AAAA-MM-DD.md`; valores validados localmente |
| `DADOS_BALANCAS/balanca_domestica/` | Registros da balança doméstica de acompanhamento | Pesar conforme protocolo matinal em jejum |
| `DADOS_BALANCAS/balanca_clinica/` | Bioimpedância clínica octapolar | Âncora clínica periódica |
| `DADOS_BALANCAS/balanca_academia/` | Bioimpedância de academia | Leitura comparativa complementar |
| `DADOS_TREINO/prints/` | Capturas do aplicativo de treinamento | Totais de sessões consolidadas |
| `DADOS_TREINO/` | Relatórios de treino em CSV | |
| `DADOS_DISPOSITIVO_A/` | Exportação de dados do Smartwatch A | Substituir periodicamente pelo arquivo mais recente |
| `DADOS_DISPOSITIVO_B/` | Exportação de dados do Rastreador B | Idem |
| `FOTOS/MES_EXEMPLO/` | Registros fotográficos corporais padronizados | Posições neutras: frente, costas, perfis |
| `REGISTRO/` | Arquivos temáticos do Registro Mestre | Lidos sob demanda |
| raiz | `Registro_Mestre_Demo.md` (núcleo), relatórios `Analise_Exemplo_DDmmmAA.md`, painéis locais | |

## Skills Especializadas
- `saude-exames` — ingestão e leitura de laudos laboratoriais.
- `saude-fotos` — preparação de pranchas comparativas e conferência visual.
- `saude-antropometria` — circunferências, dobras cutâneas e fórmulas científicas (JP7, Navy, RCQ, CMB, AMA).
- `saude-balancas` — tratamento de bioimpedâncias e pareamento metodológico.
- `saude-treino` — tonelagem e progressão de exercícios âncora.
- `saude-wearables` — tendências de repouso, sono e atividade física.
- `saude-receitas` — gestão de cronogramas e posologias didáticas.
- `saude-registro` — governança e atualização estruturada do Registro Mestre.
