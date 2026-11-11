---
name: saude-antropometria
description: Conduzir e registrar a sessão de antropometria do projeto Saúde (circunferências, dobras cutâneas, cintura de 3 níveis, %G por JP7/Navy, RCQ, cintura/estatura) e a sessão periódica completa (antropometria + fotos + bioimpedância). Use quando o usuário trouxer medidas novas, pedir para calcular ou comparar com sessões anteriores.
---

# Antropometria → Registro Mestre §7.6 (e §7.2 cintura)

> **Nota de Privacidade:** Todos os parâmetros, datas e medidas neste documento são **100% sintéticos e fictícios**.

Registro: núcleo `<PASTA_SAUDE>/Registro_Mestre_Demo.md` (§4 protocolo, Regra 4, pendências) + `REGISTRO/07_Cintura_Antropometria.md` (§7.2, §7.6). Leia os dois antes. Sem planilhas avulsas.

## Sessão periódica completa

Ordem recomendada, ao acordar, após urinar, em jejum matinal, sem treino nas horas anteriores:
1. **Balança BIA Doméstica** (peso e composição corporal) e **cintura de 3 níveis** (média de 3 níveis).
2. **Circunferências** (3 medidas por ponto, registrar a média; variação > 1 cm = técnica instável): pescoço, tórax, cintura mínima, abdômen (3 níveis), quadril, braço relaxado D/E, braço flexionado D/E, antebraço D/E, coxa D/E, panturrilha D/E.
3. **Dobras cutâneas** (adipômetro 0,1 mm, pinçamento de 4 s, 3 medidas, **mediana**): peitoral, abdominal, supra-ilíaca, coxa (autoaplicáveis, Σ4); axilar, tricipital, subescapular (Σ7).
4. **Fotos corporais padronizadas** — skill `saude-fotos`.
5. **Bioimpedância pareada** — Balança BIA Academia e Balança Doméstica em sequência na mesma manhã; protocolo na skill `saude-balancas`.
6. Registrar o **cronograma de intervenções** (dias desde a última dose de Medicação A ou fase do Protocolo B).

## Ficha digital de medição

Registro via formulário digital (artefato de medição com tipos `diaria`, `completa`, `reteste`).
- Parâmetros documentados: voltas brutas (`circ.<ponto>.voltas`, `dobras.<ponto>.voltas`), mediana do dia, Σ3/Σ4/Σ7, JP7, Navy, RCQ, cintura/estatura. **Recalcular** com o script `calcula_antropometria.py` antes de gravar.
- Condição registrada em campos de controle: jejum, repouso prévio, fase de protocolo ativo. Fora do padrão → marcar como leitura não-padronizada (`N`).
- Teste-reteste: cálculo de ETM (Erro Técnico de Medição) e MMD para controle de qualidade da técnica.

## Protocolo de continuidade longitudinal

Dados de medições novas somam-se às séries históricas:
- Cintura em 3 níveis: continuação da série histórica de acompanhamento.
- Dobras cutâneas: acompanhamento prioritário da espessura bruta em milímetros (Σ4 e Σ7), evitando conclusões baseadas unicamente em conversões matemáticas percentuais.

## Cálculo Automatizado

`python <PASTA_SAUDE>/.claude/skills/saude-antropometria/calcula_antropometria.py sessao.json` (sem argumentos executa o self-check com perfil sintético). Calcula Σ4/Σ7, %G JP7 e Navy, RCQ, cintura/estatura, CMB e AMA corrigida. O formato do JSON está documentado no cabeçalho do script.

## Regras Metodológicas

- **Acompanhar Σ em mm, nunca apenas o %G convertido**; métodos distintos (dobras, Navy, bioimpedância) apresentam premissas e equações diferentes. Comparar tendências dentro de cada método isolado.
- Cintura em 3 níveis com fita métrica profissional; média de 3 níveis padronizados.
- Estatura fixa sintética de referência: 175 cm; idade pela data de referência sintética (nasc. fictício 15/05/1990).
- Assimetria D×E: massa muscular vs gordura periférica avaliada por CMB (circunferência muscular do braço), isolando a espessura da dobra.
- Orientação estritamente educacional. Resultados fora do padrão devem ser avaliados com o profissional assistente.

## Gravação

Registrar a nova tabela de sessão em §7.6; atualizar pontos da série em §7.2, Cronologia §10, Painel §1, Pendências §11 e Log §16 conforme diretrizes da skill `saude-registro`.
