---
name: recon-enumeration
description: Guia o planejamento e a interpretação de varreduras de rede, enumeração de serviços, web fuzzing e mapeamento de superfície de ataque conforme a metodologia TryHackMe.
---

# Skill: Recon & Enumeration

Esta skill orienta o **PentsAI** a conduzir ou analisar atividades de reconhecimento ativo e passivo, varredura de portas e enumeração de serviços.

---

## Processo Passo a Passo

### Etapa 1: Definição do Escopo e Nível de Furtividade
- Pergunte sobre as restrições do engajamento: ambiente de lab TryHackMe (onde o ruído não é restritivo) ou simulação Red Team evasiva?
- Identifique o alvo: endereço IP único, faixa de rede CIDR ou hostname/domínio.

### Etapa 2: Varredura de Portas e Serviços
- Recomende o fluxo padrão do TryHackMe:
  1. Varredura rápida para descobrir portas abertas: `rustscan` ou `nmap -p- --min-rate 1000 -T4`.
  2. Varredura profunda com scripts e versões: `nmap -sC -sV -p<portas> -oN scan_results.txt <IP>`.
- Explique o propósito de cada flag recomendada.

### Etapa 3: Enumeração Específica por Serviço
Para cada porta identificada, selecione o checklist de enumeração:
- **Porta 80/443 (HTTP/HTTPS):** Identificação de tecnologias (Wappalyzer / WhatWeb), enumeração de diretórios e arquivos (`ffuf -u http://ALVO/FUZZ -w wordlist.txt`), inspeção de código-fonte e comentários.
- **Porta 445/139 (SMB):** Verificação de sessões nulas e compartilhamentos anônimos (`smbclient -L //ALVO/ -N`, `nxc smb <IP> -u '' -p '' --shares`).
- **Porta 21 (FTP):** Teste de login anonymous e verificação de arquivos residuais.
- **Porta 22 (SSH):** Identificação de banners e versões antigas (ex: libssh bugs).
- **Porta 88/389 (Kerberos/LDAP - Active Directory):** Enumeração de usuários via Kerbrute, consultas anônimas LDAP.

### Etapa 4: Interpretação de Resultados e Superfície de Ataque
- Analise os outputs fornecidos pelo operador.
- Destaque versões de serviços desatualizadas com CVEs conhecidas ou configurações permissivas.
- Mapeie a técnica correspondente: `TA0043 - Reconnaissance / T1595 - Active Scanning` e `TA0007 - Discovery / T1046 - Network Service Discovery`.

### Etapa 5: Próximos Passos Táticos
- Formule hipóteses de ataque baseadas nas evidências encontradas.
- Aponte a sala correspondente no TryHackMe para aprofundar (ex: *Nmap*, *Content Discovery*, *Network Services*).
