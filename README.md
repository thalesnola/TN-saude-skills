> **Nota de Privacidade:** Todos os parâmetros fisiológicos, medidas, datas e registros de exemplo neste repositório são **100% sintéticos e fictícios**, criados exclusivamente para demonstrar o funcionamento dos scripts, fórmulas antropométricas e skills.

---

# saude-skills

Repositório público demonstrativo das skills especializadas do projeto Saúde (Claude Code e OpenAI Codex): ingestão de exames laboratoriais, balanças de bioimpedância, antropometria, fotos corporais, treinos, wearables e prescrições didáticas integradas num Registro Mestre local.

- `.claude/skills/` — skills estruturadas para o Claude Code (`saude-antropometria`, `saude-balancas`, `saude-exames`, `saude-fotos`, `saude-receitas`, `saude-registro`, `saude-treino`, `saude-wearables`).
- `.agents/skills/` — espelho correspondente para o OpenAI Codex CLI.
- `CLAUDE.md` / `AGENTS.md` — mapeamento recomendado de diretórios e regras de governança documental.

## Princípios de Operação

- **Processamento Local:** Registros e laudos brutos permanecem na máquina local. O repositório contém exclusivamente os scripts de cálculo, rotinas de pré-processamento e regras de governança das skills.
- **Caráter Educacional:** As ferramentas executam funções de cálculo e tabulação informativa; todas as interpretações clínicas cabem aos profissionais de saúde assistentes.
