# Base de Conhecimento: Mapeamento MITRE ATT&CK® & Métricas CVSS

Este documento instrui o **PentsAI** na correlação de vulnerabilidades, técnicas de ataque e cálculo de risco para elaboração de documentações de nível profissional.

---

## 1. Táticas Principais do MITRE ATT&CK (Enterprise Matrix)

O PentsAI correlaciona cada achado de segurança com uma das táticas e técnicas da matriz:

| ID Tática | Nome da Tática | Descrição Tática | Exemplos Típicos de Pentest |
|-----------|----------------|------------------|------------------------------|
| **TA0043** | Reconnaissance | Obtenção de informações sobre o alvo | Port Scanning (`T1046`), Active Scanning (`T1595`) |
| **TA0042** | Resource Development | Criação ou compra de recursos para o ataque | Compilação de payloads, obtenção de infraestrutura |
| **TA0001** | Initial Access | Como o atacante entra na rede ou sistema | Exploit Public-Facing App (`T1190`), Phishing (`T1566`), Valid Accounts (`T1078`) |
| **TA0002** | Execution | Execução de código no alvo | Command and Scripting Interpreter (`T1059`), WMI, PowerShell |
| **TA0003** | Persistence | Garantir acesso mesmo após reinicialização | Scheduled Task/Job (`T1053`), Create Account (`T1136`), Web Shell (`T1505.003`) |
| **TA0004** | Privilege Escalation | Elevação para privilégios de ROOT / SYSTEM | Abuse Elevation Control (`T1548` - SUID, Sudo), Exploitation for Privilege Escalation (`T1068`) |
| **TA0005** | Defense Evasion | Desviar de detecções e filtros de segurança | Impair Defenses (`T1562`), Obfuscated Files (`T1027`), Deobfuscate/Decode (`T1140`) |
| **TA0006** | Credential Access | Obtenção de senhas, hashes e tokens | OS Credential Dumping (`T1003` - SAM, LSASS, `/etc/shadow`), Brute Force (`T1110`), Steal Web Session (`T1539`) |
| **TA0007** | Discovery | Reconhecimento pós-acesso do ambiente interno | System Information Discovery (`T1082`), Network Service Discovery (`T1046`), File Discovery (`T1083`) |
| **TA0008** | Lateral Movement | Movimentação entre sistemas da mesma rede | Remote Services (`T1021` - SSH, SMB, RDP), Use Alternate Authentication Material (`T1550` - Pass the Hash) |
| **TA0009** | Collection | Coleta de dados de valor e alvos sensíveis | Data from Local System (`T1005`), Archive Collected Data (`T1560`) |
| **TA0011** | Command and Control | Comunicação com o agente instalado no alvo | Ingress Tool Transfer (`T1105`), Application Layer Protocol (`T1071`) |
| **TA0010** | Exfiltration | Envio de dados confidenciais para fora da rede | Exfiltration Over C2 Channel (`T1041`), Exfiltration Over Web Service (`T1567`) |
| **TA0040** | Impact | Destruição, alteração ou indisponibilidade de serviços | Data Encrypted for Impact (`T1486`), Service Stop (`T1489`) |

---

## 2. Padrão de Classificação de Risco (CVSS v3.1 / v4.0)

Para determinar a severidade dos achados, o PentsAI avalia:

| Severidade | Score CVSS | Critérios de Avaliação |
|------------|------------|------------------------|
| **Crítico (Critical)** | 9.0 - 10.0 | RCE sem autenticação, SQLi que permite escrita/leitura total com shell, comprometimento direto do Domain Controller / Root. |
| **Alto (High)** | 7.0 - 8.9 | RCE com autenticação de baixo privilégio, SQLi com extração de credenciais, Elevação de Privilégio local (LPE) direta. |
| **Médio (Medium)** | 4.0 - 6.9 | IDOR com vazamento de dados pontuais, SSRF cego, CSRF em ações críticas, Stored XSS. |
| **Baixo (Low)** | 0.1 - 3.9 | Reflected XSS de baixo impacto, Enumeração de usuários, Vazamento de informações e versões em banners. |
| **Informativo (Info)** | 0.0 | Boas práticas, cabeçalhos de segurança ausentes (CSP, HSTS) sem exploração comprovada. |

---

## 3. Matriz de Severidade (Impacto vs Probabilidade)

```
       Probabilidade →
Impacto ↓     |  Baixa    |  Média    |  Alta
-------------|-----------|-----------|-----------
Crítico      |  Alto     |  Crítico  |  Crítico
Alto         |  Médio    |  Alto     |  Crítico
Médio        |  Baixo    |  Médio    |  Alto
Baixo        |  Info     |  Baixo    |  Médio
```

---

## 4. Estrutura Padrão de Vulnerability Finding (Padrão PentsAI)

Cada vulnerabilidade relatada pelo PentsAI deve seguir a seguinte estrutura:

```markdown
### [VULN-ID] Nome da Vulnerabilidade
- **Severidade:** [ Crítica | Alta | Média | Baixa | Informativa ] (Score CVSS estimado)
- **Tática MITRE ATT&CK:** [Nome da Tática - ex: Initial Access]
- **Técnica MITRE ATT&CK:** [ID e Nome - ex: T1190 - Exploit Public-Facing Application]
- **Alvo / Endpoint Afetado:** [URL / IP / Arquivo / Parâmetro]

#### 1. Descrição Técnica
Explicação concisa do defeito lógico ou falha de validação identificada.

#### 2. Prova de Conceito (PoC) / Passo a Passo de Reprodução
Comandos e requisições exatas para reproduzir o achado em laboratório.

#### 3. Impacto no Negócio / Sistema
O que um agente malicioso consegue obter com a exploração (confidencialidade, integridade, disponibilidade).

#### 4. Remediação & Mitigação
Código corrigido, configuração recomendada ou regras de detecção defensiva (Sigma/Suricata/WAF).
```
