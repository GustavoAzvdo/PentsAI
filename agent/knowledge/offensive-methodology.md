# Base de Conhecimento: TryHackMe & Metodologia Ofensiva

Este documento serve como referência de conhecimento do **PentsAI** sobre as trilhas de aprendizado, salas do TryHackMe e o fluxo clássico de um Teste de Intrusão.

---

## 1. Mapeamento de Trilhas TryHackMe

O PentsAI guia o operador correlacionando desafios práticos com as principais trilhas do TryHackMe:

### A. Pre Security & Introdução
- **Fundamentos de Redes:** Modelo OSI, TCP/IP, Three-Way Handshake, DNS, DHCP, Subnetting.
- **Fundamentos Web:** Requisições/Respostas HTTP/S, Métodos (GET, POST, PUT, DELETE), Cookies, Sessões, Headers de segurança.
- **Linux & Windows Fundamentals:** Permissões de arquivos, usuários/grupos, processos, CLI e navegação.

### B. Jr Penetration Tester (Trilha Central)
- **Metodologias:** Ciclos de Pentest (OSSTMM, PTES, NIST SP 800-115).
- **Network Security:**
  - Varreduras com Nmap (`-sC`, `-sV`, `-p-`, `-sU`, `--script`).
  - Análise de tráfego com Wireshark e tcpdump.
  - Enumeração de SMB (`enum4linux`, `smbclient`, `crackmapexec`), SNMP, FTP, SSH, RPC.
- **Web Hacking Fundamentals:**
  - Injeções: SQL Injection (In-band, Error-based, Blind, Time-based), Command Injection.
  - Falhas de Inclusão de Arquivos: LFI (*Local File Inclusion*), RFI (*Remote File Inclusion*), Directory Traversal.
  - SSRF (*Server-Side Request Forgery*), CSRF (*Cross-Site Request Forgery*), XSS (Reflected, Stored, DOM).
  - Quebra de Autenticação, IDOR (*Insecure Direct Object References*).
- **Escalação de Privilégios (PrivEsc):**
  - **Linux:** Binários SUID/SGID, sudo rules (`sudo -l`), Cron jobs mal configurados, Capabilities (`getcap`), Kernel exploits, senhas em arquivos de configuração / history.
  - **Windows:** Privilégios de Token (`SeImpersonatePrivilege`, `SeBackupPrivilege`), Unquoted Service Paths, Serviços vulneráveis, DLL Hijacking, AlwaysInstallElevated.

### C. Web Fundamentals
- Foco aprofundado na metodologia OWASP Top 10.
- Uso cirúrgico do Burp Suite (Proxy, Repeater, Intruder, Decoder, Comparer).
- Enumeração de diretórios e vhosts (`gobuster`, `feroxbuster`, `ffuf`).

### D. Red Teaming
- Foco em evasão, persistência e movimentação lateral.
- C2 (*Command and Control*) frameworks.
- Active Directory Attacks: Kerberoasting, AS-REP Roasting, BloodHound / SharpHound, Golden/Silver Ticket, DCSync, Pass-the-Hash / Pass-the-Ticket.
- Evasão de defesas: Bypass de AMSI, ofuscação de payloads, DLL side-loading.

---

## 2. Ciclo Metodológico de Pentest (PTES / TryHackMe Flow)

```
[ Reconhecimento / OSINT ]
           ↓
[ Varredura & Enumeração de Serviços ]
           ↓
[ Análise de Vulnerabilidades / Mapeamento de Superfície ]
           ↓
[ Exploração (PoC / Acesso Inicial) ]
           ↓
[ Pós-Exploração (Enumeração Local & PrivEsc) ]
           ↓
[ Movimentação Lateral / Pivoting (Se aplicável) ]
           ↓
[ Documentação, Mapeamento MITRE e Relatório Técnico/Executivo ]
```

---

## 3. Toolkit de Referência do PentsAI

| Categoria | Ferramentas Preferenciais | Casos de Uso Recomendados |
|-----------|---------------------------|---------------------------|
| **Recon & Port Scanning** | `nmap`, `masscan`, `rustscan` | Identificação de portas e serviços ativos |
| **Web Enumeration** | `ffuf`, `gobuster`, `feroxbuster` | Brute force de rotas, arquivos, parâmetros e subdomínios |
| **Web Proxy & Tampering** | `Burp Suite`, `OWASP ZAP`, `caido` | Interceptação, repetição e teste de injeções |
| **SQL Injection** | `sqlmap`, manual payload crafting | Verificação e automação de injeções em bancos SQL |
| **Password & Hashes** | `john the ripper`, `hashcat`, `hydra` | Quebra de hashes offline e ataques de dicionário online |
| **Linux PrivEsc** | `linpeas.sh`, `pspy`, `lse.sh` | Scripts de enumeração de vetores locais |
| **Windows PrivEsc** | `winPEAS.bat/.exe`, `PowerUp.ps1` | Enumeração de privilégios e serviços em Windows |
| **Active Directory** | `BloodHound`, `Impacket`, `NetExec (nxc)` | Mapeamento de rotas de ataque e abuso de protocolos AD |
| **Pivoting & Tunneling**| `chisel`, `sshuttle`, `socat`, `ligolo-ng` | Acesso a redes internas e sub-redes isoladas |
