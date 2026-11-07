---
name: reporting-mitre
description: Estrutura relatórios técnicos e executivos de testes de penetração, incluindo sumário executivo, matriz de risco, tabela de achados com evidências e mapeamento completo na matriz MITRE ATT&CK.
---

# Skill: Reporting & MITRE

Esta skill orienta o **PentsAI** a formatar e consolidar relatórios de pentest de nível profissional, garantindo clareza técnica e impacto de negócio.

---

## Processo Passo a Passo

### Etapa 1: Coleta de Informações do Engajamento
- Solicite ou compile os seguintes dados básicos:
  - Alvo / Organização avaliada.
  - Período e Tipo de Teste (Black Box, Grey Box, White Box).
  - Escopo autorizado (IPs, URLs, domínios excluídos).

### Etapa 2: Estruturação do Sumário Executivo
- Redija um resumo voltado para a liderança e gestores (sem jargões excessivos):
  - Visão geral da postura de segurança encontrada.
  - Principais riscos identificados e impacto direto nas operações do negócio.
  - Gráfico ou tabela resumida com a contagem de vulnerabilidades por severidade (Crítica, Alta, Média, Baixa, Informativa).

### Etapa 3: Mapeamento Global na Matriz MITRE ATT&CK
- Gere uma tabela consolidada correlacionando as táticas observadas no teste:
  
| Tática MITRE | Técnica | ID MITRE | Vulnerabilidade / Ação Associada |
|--------------|---------|----------|----------------------------------|
| Reconnaissance | Active Scanning | T1595.002 | Varredura de portas com Nmap |
| Initial Access | Exploit Public-Facing Application | T1190 | SQL Injection na tela de login |
| Privilege Escalation | Abuse Elevation Control Mechanism: Sudo | T1548.003 | Abuso de sudo sem senha para binário de backup |

### Etapa 4: Detalhamento Técnico dos Achados
Para cada vulnerabilidade, aplique o modelo formal:
- **Título & Severidade (CVSS score)**
- **Classificação (OWASP / CWE / MITRE ATT&CK)**
- **Descrição Detalhada do Problema**
- **Evidências e PoC com capturas ou logs**
- **Impacto Real Demonstrado**
- **Recomendação de Remediação (Curto e Longo Prazo)**

### Etapa 5: Plano de Ação e Roadmap de Remediação
- Priorize as correções com base na relação Risco vs Esforço de Implementação (correções rápidas imediatas vs revisões de arquitetura).
