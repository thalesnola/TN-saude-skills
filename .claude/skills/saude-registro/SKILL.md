---
name: saude-registro
description: Regras para editar o Registro Mestre do projeto Saúde (núcleo Registro_Mestre_Demo.md + REGISTRO/*.md) com segurança — versão, log, cronologia, pendências, agenda, codificação e integridade. Use sempre que for gravar qualquer dado novo no Registro, junto com a skill do tipo de dado correspondente.
---

# Governança e Edição do Registro Mestre

> **Nota de Privacidade:** Todos os parâmetros, nomes e arquivos citados são **100% sintéticos e fictícios**.

O Registro Mestre é composto pelo **núcleo** `<PASTA_SAUDE>/Registro_Mestre_Demo.md` (painel geral, regras operacionais, perfil sintético, protocolos, pendências abertas, agenda e versões recentes de log) e pelos **arquivos temáticos** em `<PASTA_SAUDE>/REGISTRO/`. O mapa temático detalhado encontra-se no cabeçalho do arquivo núcleo. Fonte única de verdade documental (evitando dispersão em planilhas paralelas).

## Fluxo Padronizado de Atualização

1. **Leitura Prévia do Cabeçalho e do Log:**
   - Conferir a versão atual no cabeçalho do núcleo e a entrada superior em `REGISTRO/16_Log.md` imediatamente antes de aplicar qualquer alteração.
2. **Adição Não-Destrutiva de Dados:**
   - Inserir novas medições ou eventos em novas linhas nas tabelas de séries (§7 e §8) **sem sobrescrever o histórico consolidado**.
   - Eventuais correções de lançamentos pretéritos devem ser sinalizadas com marcação de revisão e justificativa formal nas seções de auditoria (§13 e §16).
3. **Sincronização em Cadeia:**
   - Atualizar a Cronologia (`REGISTRO/10_Cronologia.md`), o Painel Resumo (§1), o quadro de Pendências (§11) e a Agenda (§12).
   - Ao resolver uma pendência, transferir o item concluído da seção ativa para `REGISTRO/11_Pendencias_Resolvidas.md`.
   - Incrementar a versão documental e registrar o sumário executivo no topo de `REGISTRO/16_Log.md`.
4. **Governança de Padrões e Lições:**
   - Novos comportamentos confirmados são registrados em Padrões (§9); lições aprendidas e prevenções de inconsistências em Lições (§13).
5. **Geração de Painéis Informativos:**
   - Atualizar relatórios e painéis locais de visualização gráfica para acompanhamento longitudinal das curvas de tendência corporal.
   - Parâmetros individuais e registros detalhados devem permanecer sempre preservados no ambiente local.

## Padrões de Formatação e Integridade

- Os arquivos do Registro Mestre utilizam codificação **UTF-8 com quebras de linha CRLF**.
- Modificações em lote automatizadas via script devem validar a unicidade dos blocos de substituição antes da gravação.
- Cópias de segurança devem ser mantidas em pastas temporárias isoladas durante operações de manutenção estrutural.

## Convenções de Notação

- `P`: Leitura realizada sob condições estritamente padronizadas (protocolo matinal em jejum).
- `N`: Leitura realizada fora das condições ideais de protocolo (uso apenas informativo de tendência).
- `?`: Dado não recuperado ou pendente de confirmação.
- `*`: Valor derivado ou calculado matematicamente.
- Formato de datas padronizado: `DD/MM/AAAA`.

## Diretrizes Finais

Ao concluir qualquer atualização no Registro Mestre, sintetizar ao usuário:
1. Os novos dados que foram incorporados.
2. A nova versão do documento.
3. As eventuais pendências clínicas ou laboratoriais em aberto, cuja orientação técnica cabe sempre aos profissionais de saúde assistentes (Profissional Assistente A e Profissional Assistente B).
