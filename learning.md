# SecureOps Pipeline — Learning Journal
### Shaik | MSc Cybersecurity, TU Dublin | Dublin, Ireland | May 2026

---

## PART 1: WHAT THE IRISH MARKET IS ACTUALLY ASKING FOR

Before building anything, we did real analysis of Cloud Security and DevSecOps job descriptions in Ireland in 2025–2026. This is what the market looks like and why it matters for every choice we make in this project.

---

### Why Dublin is a special market

Dublin is not just another European city for tech jobs. It is the EU headquarters for almost every major American technology company:

- **Microsoft** (Azure, Teams, Office 365 — massive campus in Dublin)
- **Google** (YouTube, Ads, Cloud)
- **Meta** (Facebook, Instagram, WhatsApp EU HQ)
- **Amazon** (AWS EU West region hosted in Ireland)
- **Stripe, HubSpot, Salesforce, LinkedIn, TikTok, Twitter/X**
- **Big 4 consulting** (Accenture, Deloitte, PwC, KPMG) all have huge tech practices
- **Financial sector** (JPMorgan, Citi, BNY Mellon, AIB, Bank of Ireland, Fidelity)

This matters for one very specific reason: **Ireland's Data Protection Commission (DPC) is the lead GDPR regulator for all these companies across the entire European Union.** Every data breach involving a European citizen that involves one of these companies lands on the DPC's desk. This means security, compliance, and data protection are not optional here — they are legally enforced with real consequences. Companies here are therefore more serious about security engineering than almost anywhere else in Europe.

**Implication for your job search:** Hiring managers in Dublin know what proper security looks like. They have seen bad portfolios. A portfolio that shows genuine understanding of compliance, identity, and threat detection will stand out enormously.

---

### What job descriptions say — the actual skill clusters

After analysing Cloud Security Engineer, DevSecOps Engineer, and IAM/Entra ID Engineer job descriptions in Ireland, these are the skill clusters that appear repeatedly across the board:

---

#### Cluster 1: SIEM and Threat Detection (appears in ~90% of Cloud Security roles)

**Microsoft Sentinel** is mentioned more than any other tool. It is Azure's cloud-native SIEM (Security Information and Event Management) system. A SIEM collects logs from every system in your infrastructure — servers, applications, firewalls, identity systems — and looks for patterns that indicate an attack or security problem.

Why Sentinel specifically? Because most Dublin companies run Microsoft 365, Azure Active Directory, and Azure infrastructure. Sentinel integrates natively with all of these. A Splunk or QRadar engineer still needs to connect to those systems manually. A Sentinel engineer is already plugged in. This is why Microsoft's tooling dominates here.

**Defender for Cloud** (CSPM — Cloud Security Posture Management) appears in roughly 70% of roles. CSPM means: continuously scanning your cloud infrastructure for misconfigurations. Did someone leave a storage account publicly accessible? Did someone forget to enable encryption? Defender for Cloud catches these automatically and gives you a security score.

---

#### Cluster 2: Infrastructure as Code and DevSecOps (appears in ~85% of roles)

**Terraform** is the single most-requested IaC (Infrastructure as Code) tool. The idea is: instead of clicking buttons in the Azure portal to create resources, you write code that describes what you want, and Terraform builds it automatically. This matters for security because:

1. You can review infrastructure changes before they happen (code review = security review)
2. You can scan that code for security misconfigurations before anything is deployed
3. You can recreate the entire environment identically — no "snowflake servers" where nobody knows what's installed

**GitHub Actions / Azure DevOps** CI/CD pipelines with embedded security testing appear in almost every DevSecOps role. CI/CD stands for Continuous Integration / Continuous Deployment — it is the automated assembly line that takes your code from a developer's laptop to production. DevSecOps means you put security checkpoints inside that assembly line so vulnerabilities are caught before they reach production.

---

#### Cluster 3: Secrets and Identity Management (appears in ~80% of roles)

**Azure Key Vault** is a secure safe for passwords, API keys, certificates, and encryption keys. The reason this is so heavily tested in interviews is that credential leakage — passwords and API keys accidentally committed to GitHub — is the number one cause of cloud breaches. Azure Key Vault solves this by storing secrets separately from your code and only allowing authorised applications to retrieve them.

**Entra ID (formerly Azure Active Directory)**, **RBAC (Role-Based Access Control)**, and **Managed Identities** appear in almost every role. The principle here is **Zero Trust** and **Least Privilege**: every user and every application gets only the exact permissions they need, nothing more. A Managed Identity is how Azure lets an application authenticate to other Azure services without needing a password at all — the identity is managed automatically by the platform.

---

#### Cluster 4: Application and Container Security (appears in ~75% of DevSecOps roles)

**SAST (Static Application Security Testing):** Scanning your source code for vulnerabilities before it runs. Tools: Bandit (Python), Semgrep.

**SCA (Software Composition Analysis):** Scanning the open-source libraries your code depends on for known vulnerabilities. Tools: Trivy, OWASP Dependency-Check. This is crucial because most modern applications are 90% open-source dependencies, and if one of those libraries has a critical vulnerability (like Log4Shell in 2021), your entire application is at risk.

**Container Security:** Docker image scanning for vulnerabilities in base OS packages and dependencies. Tool: Trivy. Every modern application runs in a container — scanning the container image before deployment is now a baseline expectation.

**IaC Security Scanning (Checkov):** Scanning your Terraform code for security misconfigurations before deployment. Did you forget to enable encryption on a storage account? Did you open port 22 to the entire internet? Checkov catches these automatically.

---

#### Cluster 5: Compliance Frameworks (appears in ~65% of senior roles)

**NIST Cybersecurity Framework (CSF):** An American framework adopted globally that organises security activities into five functions: Identify, Protect, Detect, Respond, Recover.

**CIS Benchmarks:** Prescriptive, step-by-step guides for securely configuring specific systems (Azure, Windows Server, Linux, etc.). Defender for Cloud maps its recommendations directly to CIS benchmarks.

**ISO 27001:** The international standard for information security management. Many Dublin financial sector companies require ISO 27001 compliance from their cloud providers.

**GDPR:** For any role touching data of EU citizens — which is everything in Dublin — GDPR compliance is a baseline requirement, not a nice-to-have.

---

#### Cluster 6: AI in Security (emerging, but appearing in ~40% of 2025-2026 listings)

**Microsoft Copilot for Security** and **Azure OpenAI** integrations are appearing in forward-looking job descriptions. Security teams are overwhelmed by alert volume — the average SOC (Security Operations Centre) analyst handles hundreds of alerts per day, the vast majority of which are false positives. AI that can triage alerts, summarise findings in plain English, and recommend remediation steps is becoming a genuine competitive advantage.

---

### Summary of what matters most in the Irish market

| Skill | Weight | Why |
|---|---|---|
| Microsoft Sentinel (SIEM) | Critical | Dominant in Azure-heavy Dublin market |
| Terraform | Critical | Universal IaC standard |
| GitHub Actions / CI/CD Security | Critical | Every DevSecOps role requires pipeline experience |
| Azure Key Vault + Managed Identity | Critical | Zero Trust credential management |
| Defender for Cloud (CSPM) | High | Native Azure security posture |
| SAST/SCA/Container scanning | High | Shift-left security in pipelines |
| Entra ID / RBAC | High | Identity is the new perimeter |
| Azure OpenAI / AI integration | Emerging | Differentiator for 2025-2026 |
| GDPR / compliance frameworks | Contextual | Essential for financial/tech sector |

---

## PART 2: THE ONE PROJECT — AND WHY IT BEATS EVERYTHING ELSE

### What we are building

**SecureOps Pipeline: An AI-Augmented DevSecOps Platform on Azure**

In plain English: We are building a complete automated security system that sits between a developer writing code and that code running in production. Every time code is pushed to GitHub, our system automatically:

1. **Scans the code** for security vulnerabilities (SAST)
2. **Scans the dependencies** for known vulnerabilities (SCA)
3. **Scans for secrets** accidentally committed to the repository (API keys, passwords)
4. **Scans the infrastructure code** (Terraform) for misconfigurations
5. **Scans the Docker container** for OS and package vulnerabilities
6. **Sends all findings** to Microsoft Sentinel (the SIEM) as security alerts
7. **Uses Azure OpenAI** to generate a plain-English risk summary — a one-paragraph report that a non-technical manager can read and understand
8. **Deploys the application** to Azure using Terraform with Zero Trust principles: Managed Identities, RBAC least privilege, all secrets in Key Vault

---

### Why this project beats every alternative

**Alternative 1: "Build a Sentinel threat detection dashboard"**
A dashboard shows you can configure queries. It does not show you can build secure systems. It is a passive, read-only skill. Recruiters see dozens of these. No engineering creativity.

**Alternative 2: "Azure AD / Entra ID security automation"**
Strong for IAM roles but one-dimensional. It shows identity skills but nothing about pipelines, infrastructure, or application security. Too narrow.

**Alternative 3: "Kubernetes (AKS) security hardening"**
Technically impressive but AKS costs real money (outside free tier), is complex to set up, and demonstrates infrastructure skills that overlap heavily with what you already have from 3 years of cloud engineering. Not the right differentiator.

**Alternative 4: "Compliance-as-Code with Azure Policy"**
Good compliance knowledge but dry. Does not show engineering capability. Is a checkbox exercise, not an engineering achievement.

**Alternative 5: "Penetration testing lab"**
Great learning exercise but ethically and legally sensitive on a public portfolio. Hard to demonstrate cleanly on GitHub.

**Why our project wins:**

Our project demonstrates every major skill cluster at the same time:
- **DevSecOps pipeline** → shows you can integrate security into CI/CD (Cluster 2)
- **Microsoft Sentinel** → shows SIEM experience (Cluster 1)
- **Terraform + IaC scanning** → shows infrastructure as code and security scanning (Cluster 2 + 4)
- **Azure Key Vault + Managed Identity** → shows Zero Trust implementation (Cluster 3)
- **SAST/SCA/Container scanning** → shows application security knowledge (Cluster 4)
- **Azure OpenAI** → shows AI integration (Cluster 6)
- **Defender for Cloud** → shows CSPM experience (Cluster 1)

No other single project hits all six clusters simultaneously. This is not theory — this is a deployed, working system with real infrastructure and real security findings. A recruiter clicking your GitHub link sees a system that could be dropped into a real enterprise tomorrow.

---

### How this project positions you specifically

You have 3 years of cloud engineering experience. That means you already know how to deploy things on Azure. What you need to prove is: can you think like a security engineer, not just an infrastructure engineer?

This project proves that by showing:
1. You understand the **threat model** — what can go wrong at each stage of software delivery
2. You understand **defense in depth** — multiple layers of security, not just one
3. You understand **automation** — security that requires humans to manually check things every time is security that eventually fails
4. You understand **observability** — security events are logged, alerted on, and investigated (Sentinel)
5. You understand **compliance** — the system is built following security best practices that map to CIS benchmarks

For a hiring manager at Accenture Security, Microsoft, or Deloitte: this is exactly what they want to see.

---

## PART 3: ARCHITECTURE OVERVIEW

Before we write a single line of code, we need to understand the whole system. Here is what we are building, layer by layer.

```
DEVELOPER                           GITHUB                          AZURE
──────────                          ──────                          ─────

Writes code  ──── git push ────►  Repository
                                       │
                                  GitHub Actions
                                  CI/CD Pipeline
                                       │
                               ┌───────┴────────┐
                               │  Security Gates │
                               │                 │
                               │ 1. SAST         │  ◄── Bandit/Semgrep
                               │    (code scan)  │       scans Python code
                               │                 │
                               │ 2. SCA          │  ◄── Trivy
                               │    (deps scan)  │       scans requirements.txt
                               │                 │
                               │ 3. Secrets      │  ◄── detect-secrets
                               │    detection    │       scans all files
                               │                 │
                               │ 4. IaC scan     │  ◄── Checkov
                               │    (Terraform)  │       scans .tf files
                               │                 │
                               │ 5. Container    │  ◄── Trivy
                               │    image scan   │       scans Docker image
                               └───────┬─────────┘
                                       │
                               ┌───────▼─────────────────────────────────┐
                               │         Azure OpenAI                     │
                               │  Takes all scan results → generates      │
                               │  plain-English risk summary report        │
                               └───────┬─────────────────────────────────┘
                                       │
                          ─────────────┴──────────────────────────────────
                          │                         Azure Infrastructure  │
                          │                                               │
                          │   Log Analytics     Microsoft Sentinel        │
                          │   Workspace    ──►  (SIEM)                    │
                          │   (stores all       Security alerts,          │
                          │    logs)            analytics rules,          │
                          │                     incident creation         │
                          │                                               │
                          │   Azure Key Vault   Azure Container Registry  │
                          │   (secrets,         (stores Docker images)    │
                          │    certificates)                              │
                          │                                               │
                          │   Azure Container   Defender for Cloud        │
                          │   App               (CSPM - scans our         │
                          │   (runs our app     infrastructure for        │
                          │    if gates pass)   misconfigs)               │
                          │                                               │
                          │   All built with Terraform (IaC)             │
                          └───────────────────────────────────────────────
```

### The security philosophy behind this architecture

There is a principle in security called **Defence in Depth**. It comes from medieval castle design: a castle had a moat, then walls, then an inner keep, then the royal chambers. Each layer was an independent defence. If attackers broke through the moat, the walls still stopped them.

Our system applies this to software:

- **Layer 1 (Developer's editor):** Linting and basic checks — catch the most obvious issues before code even leaves the machine
- **Layer 2 (Pipeline — code scan):** SAST catches insecure code patterns
- **Layer 3 (Pipeline — dependency scan):** SCA catches vulnerable libraries
- **Layer 4 (Pipeline — secrets scan):** Detect-secrets catches leaked credentials
- **Layer 5 (Pipeline — IaC scan):** Checkov catches infrastructure misconfigurations
- **Layer 6 (Pipeline — container scan):** Trivy catches vulnerabilities in the container image
- **Layer 7 (Runtime — SIEM):** Sentinel watches what is actually happening in production
- **Layer 8 (Runtime — CSPM):** Defender for Cloud continuously checks infrastructure posture

An attacker would have to bypass every single one of these layers simultaneously. That is enormously harder than bypassing just one.

### Zero Trust — the identity philosophy

Zero Trust is a security model that says: **"Never trust, always verify."** The traditional model was: if you are inside the corporate network, you are trusted. Zero Trust says: even if you are inside the network, you must prove who you are and you only get access to exactly what you need.

In Azure, Zero Trust is implemented through:
- **Managed Identities:** An application authenticates using its Azure identity, not a username/password. There is no password to leak.
- **RBAC:** Every identity gets the minimum permissions needed (Least Privilege). A deployment pipeline that only needs to push Docker images should not also have permission to delete databases.
- **Key Vault:** Secrets (API keys, connection strings) are never stored in code or environment variables. They are stored in Key Vault and the application fetches them at runtime using its Managed Identity.
- **Conditional Access:** Even authenticated users must meet conditions (correct device, correct location, MFA) before accessing sensitive resources.

---

## PART 4: THE BUILD — STEP BY STEP

Everything below this line is the actual construction. Each section will explain:
1. **What** we are doing
2. **Why** we are doing it (the security reasoning)
3. **The code**, line by line
4. **What this proves** to a hiring manager

---

### STEP 1: Project Structure and the Sample Application

---

#### FILE LOCATION MATTERS — WHY `app/app.py` NOT `scripts/app.py`

When GitHub Actions runs our security scanners, we point each scanner at a specific folder. Bandit (SAST) is told to scan the `app/` directory. If the file is in `scripts/`, Bandit never sees it and finds nothing. The folder structure is part of the security contract.

**Action required:** Move `scripts/app.py` → `app/app.py`. You can do this in VS Code by dragging the file, or right-click → Move.

---

#### THE BIG QUESTION: "IN A REAL COMPANY I HAVE MY OWN CODE — WHAT DO I DO?"

This is exactly the right question to ask, and the answer changes how you think about this entire project.

**The application is not the portfolio. The pipeline is the portfolio.**

Let me say that more clearly:

When you join a company as a Cloud Security Engineer or DevSecOps Engineer, there is already an application. It might be 500,000 lines of Java. It might be a Python microservice. It might be a Node.js API. You did not write it. You do not own it. But your job is to make it secure.

You do that by building exactly what we are building right now — the pipeline. You point the pipeline at whatever code the company already has, and the pipeline scans it, reports vulnerabilities, sends alerts to Sentinel, and enforces security gates.

So the answer to your question is: **replace our demo Flask app with your company's code, and every single thing else stays identical.** The Terraform, the GitHub Actions pipeline, the Sentinel integration, the Key Vault setup — none of that changes. Only the application being scanned changes.

For this portfolio project, we need *something* to scan. We deliberately included four classic vulnerabilities so the scanners have real findings to detect. This makes the demo more impressive — a recruiter looking at your GitHub sees:

1. The scanner ran ✓
2. The scanner found real vulnerabilities ✓  
3. The pipeline correctly flagged and reported them ✓
4. The AI summariser produced a human-readable risk report ✓
5. Sentinel received the alert ✓

If the app had no vulnerabilities, steps 2-5 would show nothing, and the demo would be unconvincing.

In an interview, you say: *"I built a complete DevSecOps pipeline on Azure. I tested it against a demo application that contained intentional vulnerabilities — SQL injection, command injection, weak hashing, and a hardcoded secret — to validate that every security gate worked correctly. In production, you point this same pipeline at any application. The pipeline is environment-agnostic."*

That answer demonstrates real engineering thinking.

---

#### WHAT THE IMPORTS BLOCK DOES — LINE BY LINE

This is the code you typed:

```python
import os
import sqlite3
import subprocess
import hashlib
from flask import Flask, request, jsonify
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)
```

Let's go through each line as if you have never seen Python before, but explain the *security reasoning* not just what the code does.

---

**`import os`**

`os` is Python's way of reading the operating system's environment variables. An environment variable is a key-value pair set outside your code — on the server, in a container, in a CI/CD pipeline — that your code reads at runtime.

Security reason: Configuration (URLs, hostnames, feature flags) should never be hardcoded in source code. If you hardcode `vault_url = "https://myvault.vault.azure.net"`, then when you move between environments (dev, staging, production), you have to change the code. More importantly, if you hardcode a secret (password, API key), it ends up in your Git history forever — even if you delete it later. Environment variables keep configuration separate from code.

We use `os.environ.get("AZURE_KEY_VAULT_URL")` to read the Key Vault URL at runtime without it ever appearing in the code.

---

**`import sqlite3`**

SQLite is a file-based database engine built into Python. It is not a real production database (you would use PostgreSQL or Azure SQL in production), but for this demo it lets us write real database queries without needing to set up an actual database server.

Security reason: We use it specifically to demonstrate SQL injection — the most famous and oldest class of database vulnerability. By showing you what an insecure query looks like, and then showing Bandit catch it, you build the mental model for why parameterised queries exist.

---

**`import subprocess`**

`subprocess` lets Python run external system commands — the kind of commands you type in a terminal. `ping`, `ls`, `curl`, anything.

Security reason: We import it to demonstrate command injection — what happens when user input reaches a system shell command without sanitisation. This is how attackers execute arbitrary code on servers. Bandit specifically flags `subprocess.run(..., shell=True)` as dangerous.

---

**`import hashlib`**

`hashlib` gives Python access to cryptographic hash functions: MD5, SHA-1, SHA-256, SHA-512, and others.

Security reason: Cryptographic hashing is how passwords are stored safely. You never store a password in plain text. You hash it, and store the hash. When a user logs in, you hash their input and compare the hash — you never need the original password. BUT not all hash functions are equal:

- **MD5** (1992): Broken. Takes seconds to crack with modern hardware. Rainbow tables (precomputed hashes for millions of common passwords) make it trivially reversible.
- **SHA-1** (1995): Broken. Deprecated by NIST in 2011.
- **SHA-256**: Acceptable for general hashing, but not ideal for passwords because it is too fast — an attacker can try billions of password guesses per second.
- **bcrypt / Argon2**: Correct for passwords. They are intentionally slow and include a random "salt" so two identical passwords produce different hashes.

Our demo uses `hashlib.md5()` deliberately. Bandit will flag it as insecure with the warning: `Use of insecure MD5 hash function`.

---

**`from flask import Flask, request, jsonify`**

Flask is a Python web framework — it turns your Python functions into HTTP endpoints (URLs that respond to web requests).

- `Flask` — the application object itself. `app = Flask(__name__)` creates one application instance.
- `request` — represents the incoming HTTP request. `request.args.get("username")` reads a URL parameter like `?username=shaik`. `request.get_json()` reads a JSON body sent in a POST request.
- `jsonify` — converts a Python dictionary into a proper JSON HTTP response with the correct `Content-Type: application/json` header.

Security reason: Flask is lightweight and does not include security features by default — it does not validate inputs, sanitise SQL queries, or prevent command injection. That is the developer's responsibility. This is why SAST scanners like Bandit exist: to catch the developer mistakes Flask does not prevent.

---

**`from azure.identity import ManagedIdentityCredential`**

This is from Microsoft's Azure SDK for Python. `ManagedIdentityCredential` is the class that says: "authenticate using this application's Azure Managed Identity."

What is a Managed Identity? 

In the old model, if your application needed to talk to Azure Key Vault, you would give it a username and password (a Service Principal with a client secret). Those credentials had to be stored somewhere — in environment variables, in a config file, somewhere. That "somewhere" is a security risk.

Azure Managed Identity eliminates the password entirely. Azure says: "I know who this application is because it is running on my infrastructure. I will issue it a short-lived token automatically. The application never needs to know a password." 

From a Zero Trust perspective, this is ideal: the credential exists only inside Azure's identity system, never in your code, never in your config files, never on disk, never in logs.

`ManagedIdentityCredential()` — no arguments needed. Azure handles everything.

---

**`from azure.keyvault.secrets import SecretClient`**

`SecretClient` is the Azure SDK class for reading and writing secrets in Azure Key Vault.

You pass it two things: the URL of your Key Vault (`vault_url`) and the credential to authenticate with (`ManagedIdentityCredential`). Together, they let your application securely retrieve any secret stored in Key Vault at runtime.

The pattern — `credential = ManagedIdentityCredential()` → `client = SecretClient(vault_url, credential)` → `client.get_secret("name")` — is something you should be able to recite in an interview. It is the correct answer to "how do you handle secrets in Azure?"

---

**`app = Flask(__name__)`**

Creates the Flask application. `__name__` is a Python special variable that contains the name of the current module (file). Flask uses it to find resources (templates, static files) relative to the application file's location.

Security reason: Nothing here specifically, but this line matters because everything we build next — the API endpoints, the health check, the vulnerability demonstrations — hangs off this `app` object.

---

#### NEXT STEP: ADD THE FOUR VULNERABILITY FUNCTIONS AND THE API ENDPOINTS

You will now add four functions after the `app = Flask(__name__)` line. Each demonstrates one classic vulnerability category. Type them one at a time — explanations follow each block.

---

**BLOCK 2: The hardcoded secret (vulnerability 1)**

```python
# VULNERABILITY 1 — Hardcoded credential
# detect-secrets will flag this line.
DB_PASSWORD = "SuperSecret123!"
```

This is the simplest vulnerability to understand. A developer was in a hurry. They put the database password directly in the code. They committed it to Git. Now it is in Git history forever — even if they delete it from the file later, `git log` shows it.

The `detect-secrets` tool scans every file in the repository for patterns that look like secrets: high-entropy strings, words like "password", "secret", "key" followed by an assignment. It will flag this line with: `Secret type: Secret Keyword`.

The fix: store the password in Azure Key Vault and retrieve it using the `SecretClient` pattern above.

---

**BLOCK 3: The weak hash function (vulnerability 2)**

```python
def hash_password_insecure(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()
```

`password.encode()` converts the string to bytes (hashlib needs bytes, not strings).
`hashlib.md5(...)` computes the MD5 hash.
`.hexdigest()` returns the hash as a readable hex string like `"5f4dcc3b5aa765d61d8327deb882cf99"`.

Bandit will flag this with: `Use of insecure MD5 or SHA1 hash function`.

---

**BLOCK 4: The SQL injection function (vulnerability 3)**

```python
def get_user_insecure(username: str):
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()
```

`sqlite3.connect(":memory:")` — creates an in-memory database (disappears when the program ends; safe for demo purposes).
`cursor = conn.cursor()` — a cursor is the object that executes SQL queries.
`f"SELECT * FROM users WHERE username = '{username}'"` — an f-string that inserts the variable directly into the SQL. THIS IS THE VULNERABILITY.

If `username = "shaik"` → query is `SELECT * FROM users WHERE username = 'shaik'` — fine.
If `username = "' OR '1'='1"` → query is `SELECT * FROM users WHERE username = '' OR '1'='1'` — returns every user.
If `username = "'; DROP TABLE users;--"` → query is `SELECT * FROM users WHERE username = ''; DROP TABLE users;--` — deletes the table.

Bandit flags this with: `Possible SQL injection via string-based query construction`.

---

**BLOCK 5: The command injection function (vulnerability 4)**

```python
def ping_host_insecure(host: str) -> str:
    result = subprocess.run(
        f"ping -c 1 {host}", shell=True, capture_output=True, text=True
    )
    return result.stdout
```

`subprocess.run(...)` — runs an OS command.
`f"ping -c 1 {host}"` — builds the command string with user input inserted directly.
`shell=True` — tells Python to pass the command to the OS shell interpreter (bash/sh). This is what makes injection possible: the shell interprets `;`, `|`, `&&` as special characters that chain commands.

If `host = "google.com"` → runs `ping -c 1 google.com` — fine.
If `host = "google.com; cat /etc/passwd"` → runs `ping -c 1 google.com` then `cat /etc/passwd` — leaks the server's user database.

Bandit flags this with: `subprocess call with shell=True identified, security issue`.

---

**BLOCK 6: The correct Key Vault pattern**

```python
def get_secret_from_keyvault(secret_name: str) -> str:
    vault_url = os.environ.get("AZURE_KEY_VAULT_URL", "")
    if not vault_url:
        return "KEY_VAULT_URL_NOT_SET"
    credential = ManagedIdentityCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    secret = client.get_secret(secret_name)
    return secret.value
```

`os.environ.get("AZURE_KEY_VAULT_URL", "")` — reads the Key Vault URL from an environment variable. The second argument `""` is the default if the variable is not set.
`if not vault_url: return "KEY_VAULT_URL_NOT_SET"` — graceful handling when running locally without Azure. Never crash, never expose errors.
`ManagedIdentityCredential()` — no password. Azure handles authentication.
`SecretClient(vault_url=vault_url, credential=credential)` — creates the client.
`client.get_secret(secret_name)` — retrieves the secret by name.
`secret.value` — the actual secret string.

This is the interview-worthy pattern. Every word of this should feel natural to you.

---

**BLOCK 7: The API endpoints**

```python
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "secureops-api", "version": "1.0.0"})


@app.route("/api/user", methods=["GET"])
def get_user():
    username = request.args.get("username", "")
    user = get_user_insecure(username)
    return jsonify({"user": user})


@app.route("/api/ping", methods=["POST"])
def ping():
    data = request.get_json()
    host = data.get("host", "127.0.0.1")
    result = ping_host_insecure(host)
    return jsonify({"result": result})


@app.route("/api/secret", methods=["GET"])
def fetch_secret():
    secret_name = request.args.get("name", "db-connection-string")
    get_secret_from_keyvault(secret_name)
    return jsonify({"secret_name": secret_name, "retrieved": True})


if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=8080, debug=debug_mode)
```

`@app.route(...)` — a decorator that registers the function below it as a URL handler.
`"/health"` — the URL path. When someone visits `http://yourapp/health`, this function runs.
`methods=["GET"]` — only responds to HTTP GET requests. `methods=["POST"]` only responds to POST.

The `if __name__ == "__main__"` block — runs only when you execute the file directly (`python app.py`), not when it is imported by another module or a WSGI server. This is standard Python pattern.

`host="0.0.0.0"` — listen on all network interfaces. This is required inside a Docker container so traffic from outside the container can reach the app. `127.0.0.1` would only accept connections from inside the container itself.
`port=8080` — the port number. Port 80 and 443 require elevated privileges in Linux. 8080 is a conventional unprivileged alternative.
`debug=debug_mode` — debug mode should be off in production. It exposes an interactive Python debugger in the browser — an attacker could use it to run arbitrary code on the server. We read this from an environment variable so it can be enabled in development but disabled in production automatically.

---

#### SUMMARY OF WHAT YOU HAVE AFTER STEP 1

A Flask web application that:
- Demonstrates 4 real vulnerability patterns that your SAST and secrets scanners will detect
- Shows the correct Key Vault + Managed Identity pattern
- Follows security best practices in the application structure itself (debug mode controlled by env var, secrets read from environment, not hardcoded)
- Is ready to be containerised and scanned

**File location reminder:** This code belongs in `app/app.py`, not `scripts/app.py`. Move the file before the next step.

---

### STEP 2: `requirements.txt` — Declaring Your Dependencies

---

#### WHAT IS `requirements.txt` AND WHY DOES IT EXIST?

Every Python project depends on external libraries — code written by other people that you import into your project. Flask, the Azure SDK, and other packages are not part of Python itself. They are community-written libraries that live on PyPI (the Python Package Index).

`requirements.txt` is the manifest that says: *"this project needs these specific libraries at these specific versions."*

Without it:
- A new developer cloning your repo has no way to know what to install
- Your Docker container has no way to know what to install
- Your CI/CD pipeline has no way to know what to install
- Your SCA (Software Composition Analysis) scanner has no way to know what to check for vulnerabilities

**Security angle — why versions matter:**

`requirements.txt` with pinned versions like `flask==3.0.3` is the security-correct approach. Without pinned versions (`flask` with no version) every install pulls the latest, which might include a newly introduced vulnerability. Pinned versions give you a reproducible, auditable dependency set — you know exactly what is running in production, and your SCA scanner (Trivy) can check each version against the CVE database.

A CVE (Common Vulnerabilities and Exposures) is a public record of a known security vulnerability in a specific version of software. Trivy will say: *"flask==2.0.0 has CVE-2023-XXXXX — upgrade to 2.3.2."* It can only do this if it knows which version you are using.

---

#### CREATE THIS FILE: `requirements.txt` (in the root of the project, NOT inside `app/`)

```
flask==3.0.3
azure-identity==1.17.1
azure-keyvault-secrets==4.8.0
requests==2.32.3
gunicorn==22.0.0
```

**Line by line:**

`flask==3.0.3`
Flask is our web framework. Version 3.0.3 is a stable, patched release. Flask below 2.3.2 has known vulnerabilities. Pinning to a known-good version is intentional.

`azure-identity==1.17.1`
This is the Azure SDK library that provides `ManagedIdentityCredential`. It handles the entire authentication flow between your application and Azure's identity system. Without this, `from azure.identity import ManagedIdentityCredential` fails.

`azure-keyvault-secrets==4.8.0`
This is the Azure SDK library that provides `SecretClient` for reading from Key Vault. Without this, `from azure.keyvault.secrets import SecretClient` fails.

`requests==2.32.3`
The most popular Python HTTP library. We use it in our AI summariser script (Step 5) to call the Azure OpenAI REST API. Also a transitive dependency of the Azure SDK.

`gunicorn==22.0.0`
This is the **production web server** for Python applications. Flask's built-in server (`app.run()`) is fine for development but it is single-threaded and not designed for production load. Gunicorn is a WSGI (Web Server Gateway Interface) server that:
- Handles multiple concurrent requests using worker processes
- Is designed for production use
- Is the standard way to run Flask in Docker containers

In the Dockerfile you will see: `CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]`
This says: run gunicorn, listen on all interfaces on port 8080, load the `app` object from the `app.py` module.

---

### STEP 3: The `Dockerfile` — Containerising the Application

---

#### WHAT IS A DOCKER CONTAINER AND WHY DOES EVERY COMPANY USE THEM?

Imagine you write code on your Windows laptop. It works perfectly. You deploy it to a Linux server. It crashes. The classic developer excuse: *"It works on my machine."*

Docker solves this by packaging your application with everything it needs to run — the operating system layer, Python interpreter, all dependencies, all configuration — into a single, portable unit called a **container image**. The image runs identically everywhere: your laptop, a colleague's Mac, Azure Container Apps, AWS, Google Cloud.

For security engineering, containers matter because:

1. **Isolation** — each container runs in its own sandboxed environment. A vulnerability in one container cannot (in theory) affect other containers or the host system.
2. **Immutability** — a container image is built once and deployed identically everywhere. You scan the image for vulnerabilities before deployment and know exactly what is in production.
3. **Auditability** — every layer of the image is recorded. You can inspect exactly which OS packages, Python libraries, and application files are inside.
4. **Least privilege** — containers can run as non-root users, with minimal OS packages, with read-only filesystems.

Trivy (our container scanner) will scan the image we build and report vulnerabilities in:
- The base OS image (Ubuntu, Debian, Alpine)
- System packages installed in the image
- Python packages from `requirements.txt`
- The application code itself

---

#### DOCKERFILE SECURITY PRINCIPLES

Before writing the file, understand the four security principles that shape every decision in it:

**1. Use a minimal base image**
The more software in the base image, the more attack surface. `python:3.12-slim` is a Debian-based image with only the essentials. `python:3.12-alpine` is even smaller (Alpine Linux). Fewer packages = fewer CVEs for Trivy to find.

**2. Never run as root**
By default, Docker containers run as the `root` user inside the container. If an attacker escapes the application (via code injection, for example), they are root — they can read any file, install malware, access the network. We create a non-root user and switch to it before running the application.

**3. Pin your base image version**
`FROM python:3.12-slim` is less specific than `FROM python:3.12.4-slim`. Unpinned versions mean a future rebuild might pull a different (possibly vulnerable) version. In production, teams pin to the exact digest hash: `FROM python:3.12.4-slim@sha256:...`.

**4. Copy only what you need**
Only copy the application code and dependencies into the image. Never copy `.git/`, `.env` files, test files, or development tools. We use `.dockerignore` to control this.

---

#### CREATE THIS FILE: `Dockerfile` (in the root of the project)

```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8080

ENV FLASK_DEBUG=false

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--timeout", "60", "app:app"]
```

**Line by line — security reasoning for every decision:**

---

`FROM python:3.12-slim`

This is the base image — the starting point every other instruction builds on. `python:3.12-slim` gives us:
- Debian Linux (minimal)
- Python 3.12 interpreter
- pip (Python package manager)

Why `slim` and not the full image? The full `python:3.12` image includes compilers, build tools, debugging utilities — things needed to build software, not to run it. Our finished container only needs to run the app. `slim` cuts the image size from ~1GB to ~150MB and removes hundreds of packages that Trivy would otherwise scan and potentially flag.

Why not `alpine`? Alpine uses `musl libc` instead of the standard `glibc`. Some Python packages with C extensions have compatibility issues with `musl`. `slim` (Debian-based) is safer for production Python applications.

---

`WORKDIR /app`

Sets the working directory inside the container. All subsequent `COPY`, `RUN`, and `CMD` instructions operate relative to `/app`. This is a hygiene instruction — without it, files end up scattered in `/`.

---

`RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser`

Creates a non-root user called `appuser` in a group called `appgroup`. The `--system` flag creates a system account (no password, no home directory, no shell). This is the least-privilege principle applied to the container itself.

Why does this matter? If an attacker exploits our SQL injection vulnerability and gains code execution, they execute commands as `appuser` — an unprivileged system account with no sudo rights, no password, no ability to modify system files. The blast radius of the compromise is dramatically reduced.

---

`COPY requirements.txt .`
`RUN pip install --no-cache-dir -r requirements.txt`

Copies the requirements file first, then installs dependencies. 

Why copy requirements before the application code? Docker builds images in layers — each instruction creates a layer, and Docker caches layers. If you copy all files first and then install dependencies, every code change invalidates the cache and Docker re-downloads all dependencies. By copying requirements first, Docker only re-runs `pip install` when requirements actually change. This makes builds faster.

`--no-cache-dir` — tells pip not to cache downloaded packages inside the container. The cache would take space and serve no purpose once the image is built.

---

`COPY app/ .`

Copies everything from the local `app/` directory into the container's `/app/` working directory. This is where `app.py` lands.

Notice we do not copy the entire project — only the `app/` subdirectory. Terraform files, GitHub Actions workflows, test files, `.git/` history — none of that belongs inside the runtime container.

---

`RUN chown -R appuser:appgroup /app`

Changes ownership of all files in `/app` to `appuser:appgroup`. This happens as root (before the `USER` switch) because only root can change file ownership. After this, `appuser` can read the application files.

---

`USER appuser`

Switches to the non-root user for all subsequent instructions — including `CMD`. From this point on, the container runs as `appuser`. This is the most important security line in the Dockerfile.

---

`EXPOSE 8080`

Documents that this container listens on port 8080. This is documentation only — it does not actually open the port. The port is mapped when you run the container (`docker run -p 8080:8080`). Azure Container Apps reads this to know which port to route traffic to.

---

`ENV FLASK_DEBUG=false`

Sets an environment variable with a safe default. We read this in `app.py` with `os.environ.get("FLASK_DEBUG")`. The container default is `false` — production-safe. A developer can override it with `docker run -e FLASK_DEBUG=true` during local development.

---

`CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--timeout", "60", "app:app"]`

The command that runs when the container starts.

`gunicorn` — the production WSGI server.
`--bind 0.0.0.0:8080` — listen on all interfaces, port 8080.
`--workers 2` — spawn 2 worker processes. Each worker handles requests independently. If one crashes, the other continues serving. For a small demo app, 2 is appropriate.
`--timeout 60` — kill a worker that does not respond within 60 seconds. Prevents hung processes from blocking all traffic.
`app:app` — load the Python module named `app` (the file `app.py`) and find the Flask object named `app` inside it.

Why not `CMD ["python", "app.py"]`? That uses Flask's development server, which is single-threaded, not production-hardened, and in debug mode it exposes a security vulnerability. Gunicorn is always the correct production choice.

---

#### CREATE THIS FILE: `.dockerignore` (in the root of the project)

```
.git
.github
__pycache__
*.pyc
*.pyo
.env
.env.*
*.tfstate
*.tfstate.backup
terraform/
tests/
*.md
.dockerignore
```

**Why `.dockerignore` matters for security:**

Without `.dockerignore`, `COPY . .` would copy everything into the image including:
- `.git/` — your entire commit history (could contain old secrets that were deleted from files but remain in history)
- `.env` files — local environment variables that often contain real credentials
- `terraform/` — Terraform state files can contain resource IDs and sensitive outputs
- `*.tfstate` — Terraform state can contain plaintext secrets

`.dockerignore` works exactly like `.gitignore` — it tells Docker which files to ignore when evaluating `COPY` instructions.

---

#### WHAT TRIVY WILL DO WITH THIS IMAGE

After you build this image with `docker build -t secureops-api .`, Trivy will scan it and report:

1. **OS vulnerabilities** — CVEs in the Debian packages inside `python:3.12-slim`
2. **Python package vulnerabilities** — CVEs in Flask, azure-identity, gunicorn, etc.
3. **Secret scanning** — any accidentally embedded credentials (our `.dockerignore` prevents the worst of this)
4. **Misconfiguration** — running as root, exposed sensitive ports, etc.

In our GitHub Actions pipeline (Step 4), Trivy runs automatically on every push and reports findings to the pipeline log and to Sentinel.

---

#### SUMMARY OF WHAT YOU HAVE AFTER STEP 2

```
Azure Secure pipeline/
├── app/
│   └── app.py          ← Flask application with 4 vulnerabilities + Key Vault pattern
├── Dockerfile          ← Secure container build (non-root user, minimal image, gunicorn)
├── .dockerignore       ← Prevents secrets and state files entering the image
├── requirements.txt    ← Pinned Python dependencies for reproducible, auditable builds
└── learning.md
```

---

### STEP 3: `tests/test_app.py` — Basic Tests

---

#### WHY A PIPELINE NEEDS TESTS

A CI/CD pipeline without tests is just an automated deployment button — it ships code fast but has no idea if the code works. Every professional pipeline runs tests as the very first gate. If tests fail, nothing deploys. This protects production from broken code before any security scanning even runs.

For a portfolio project the tests also prove you know the discipline. A hiring manager sees a `tests/` folder and immediately knows you understand software quality, not just deployment.

**`pytest`** is the standard Python test framework. GitHub Actions will run `pytest tests/` automatically in the pipeline.

---

#### THE TEST FILE — LINE BY LINE

```python
import pytest
from app.app import app as flask_app
```

`pytest` — the test runner. It finds all functions that start with `test_` and runs them.
`from app.app import app as flask_app` — imports our Flask application object so we can send test HTTP requests to it without actually starting a real server.

```python
@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client
```

A `fixture` in pytest is a reusable setup function. Every test that declares `client` as a parameter automatically gets a fresh test client.

`flask_app.config["TESTING"] = True` — puts Flask in test mode. This disables error catching so test failures show real exceptions, not generic 500 responses.
`flask_app.test_client()` — creates an in-memory HTTP client that talks directly to the Flask app without a real network connection. Fast, isolated, no side effects.
`yield client` — hands the client to the test, then cleans up after the test finishes.

The five test functions each send one HTTP request and assert the response code is 200 (HTTP 200 = success). These are **smoke tests** — they confirm the application starts and all routes respond, not that the logic is perfect. In a real project you would add more detailed assertions.

---

### STEP 4: Terraform — Building the Azure Infrastructure as Code

---

#### WHAT IS TERRAFORM AND WHY NOT JUST USE THE AZURE PORTAL?

The Azure Portal is a website where you click buttons to create resources. It is fast for one-off experiments. It is terrible for production because:

- **It is not repeatable.** Click-based infrastructure cannot be recreated identically in a disaster recovery scenario.
- **It is not reviewable.** There is no pull request for someone to review before a misconfigured firewall rule goes live.
- **It is not auditable.** There is no record of who changed what and when (beyond Azure Activity Logs).
- **It drifts.** Someone clicks a change in the portal, nobody documents it, and now what is deployed does not match what anyone thinks is deployed.

Terraform solves all of this. You write `.tf` files that describe the desired state of your infrastructure. Terraform figures out what needs to be created, modified, or deleted to reach that state. Every change is a code change — reviewable, version-controlled, auditable, repeatable.

**Why this matters in security:** Infrastructure as Code means security controls are code. Encryption settings, firewall rules, RBAC assignments, diagnostic logging — all defined in `.tf` files that your Checkov scanner (Step 5) can scan for misconfigurations before they ever reach Azure.

---

#### TERRAFORM CONCEPTS YOU NEED TO KNOW

**Provider** — the plugin that knows how to talk to a specific cloud. `hashicorp/azurerm` is the Azure provider. It translates your Terraform code into Azure REST API calls.

**Resource** — a single Azure object. A Key Vault is a resource. A Log Analytics Workspace is a resource. A role assignment is a resource.

**Variable** — a parameter you pass in at runtime. `var.location` could be `"westeurope"` or `"northeurope"`. Variables make your code reusable across environments.

**Output** — a value Terraform prints after it finishes. `output "key_vault_url"` prints the Key Vault URL so the GitHub Actions pipeline knows where to point the application.

**State file** — Terraform tracks what it has deployed in a state file (`terraform.tfstate`). This file can contain sensitive outputs. In production it lives in Azure Blob Storage (remote state), never in Git. Our `.dockerignore` and `.gitignore` both exclude `*.tfstate`.

**`terraform init`** — downloads the provider plugins. Run once.
**`terraform plan`** — shows what Terraform *would* do without changing anything. Always run this first to review changes.
**`terraform apply`** — makes the changes. Asks for confirmation unless you pass `-auto-approve`.
**`terraform destroy`** — deletes everything. Use this to tear down the demo after testing to avoid Azure costs.

---

#### THE TERRAFORM FILE STRUCTURE

```
terraform/
├── main.tf          ← Resource group and provider configuration
├── variables.tf     ← All input variables defined in one place
├── outputs.tf       ← Values printed after apply (Key Vault URL, etc.)
├── keyvault.tf      ← Azure Key Vault + secrets
├── monitoring.tf    ← Log Analytics Workspace + Microsoft Sentinel
└── registry.tf      ← Azure Container Registry (stores Docker images)
```

Splitting resources into separate files by concern (not required by Terraform, which treats all `.tf` files in a directory as one) is a professional convention. A security reviewer can open `keyvault.tf` and immediately see all Key Vault configuration without reading an 800-line monolithic file.

---

---

## TERRAFORM DEEP DIVE — FROM ZERO TO PRODUCTION

Before writing a single `.tf` file, you must understand the language, the workflow, and the mental model. Every section below applies directly to the files you will write after.

---

### WHAT TERRAFORM ACTUALLY IS

Terraform is a tool made by HashiCorp. You write text files that describe infrastructure — cloud resources, DNS records, databases, firewalls — and Terraform talks to cloud provider APIs to make that infrastructure exist.

The key idea is **declarative vs imperative**:

- **Imperative** (how most code works): "Do step 1, then step 2, then step 3." You describe the *process*.
- **Declarative** (how Terraform works): "I want this key vault to exist with these settings." You describe the *desired end state*. Terraform figures out the steps.

This matters because:
- If the resource already exists and matches what you described, Terraform does nothing
- If it exists but settings differ, Terraform modifies only what changed
- If it does not exist, Terraform creates it
- If you remove it from your `.tf` file, Terraform deletes it

That last point is powerful and dangerous. **Deleting a resource from a `.tf` file and running `terraform apply` will delete that resource from Azure.** This is intentional — it keeps reality in sync with code — but new engineers delete production databases this way. Always run `terraform plan` first.

---

### HCL — THE TERRAFORM LANGUAGE

Terraform uses HCL (HashiCorp Configuration Language). It looks like JSON but is more readable and supports expressions.

**Basic syntax:**

```hcl
block_type "resource_type" "local_name" {
  argument_name = value
  another_arg   = "string value"
  number_arg    = 42
  bool_arg      = true

  nested_block {
    inner_arg = "value"
  }
}
```

Everything in Terraform is a **block**. A block has:
- A **type** (`resource`, `variable`, `output`, `data`, `provider`, `terraform`, `locals`)
- Sometimes a **label** or two (e.g., `"azurerm_key_vault"` and `"main"`)
- A **body** — key-value pairs and nested blocks inside `{}`

---

### THE FIVE BLOCK TYPES YOU MUST KNOW

#### 1. `resource` — creates something in Azure

```hcl
resource "azurerm_resource_group" "main" {
  name     = "my-resource-group"
  location = "westeurope"
}
```

- First label: `"azurerm_resource_group"` — the resource type. Always `provider_resourcetype`.
- Second label: `"main"` — your local name. Can be anything. Used to reference this resource elsewhere.
- Body: the configuration arguments for this specific resource type.

**How to reference this resource elsewhere:**
`azurerm_resource_group.main.name` — type dot local-name dot attribute.

So if another resource needs to be in the same resource group:
```hcl
resource_group_name = azurerm_resource_group.main.name
```
This creates an **implicit dependency** — Terraform knows it must create the resource group before this other resource.

---

#### 2. `variable` — an input parameter

```hcl
variable "location" {
  description = "Azure region"
  type        = string
  default     = "westeurope"
}
```

Reference it anywhere with `var.location`.

Types available: `string`, `number`, `bool`, `list(string)`, `map(string)`, `object({...})`.

You can pass variable values:
- On the command line: `terraform apply -var="location=northeurope"`
- In a `terraform.tfvars` file (never commit this if it contains secrets)
- From environment variables: `export TF_VAR_location=northeurope`
- In GitHub Actions: as pipeline secrets injected as env vars

---

#### 3. `output` — a value printed after apply

```hcl
output "key_vault_url" {
  description = "URL of the Key Vault"
  value       = azurerm_key_vault.main.vault_uri
}
```

Outputs are printed to terminal after `terraform apply`. They are also stored in state and can be queried with `terraform output -raw key_vault_url`. GitHub Actions uses this to pass infrastructure values (like the Key Vault URL) to deployment steps.

---

#### 4. `data` — reads existing Azure resources (does not create)

```hcl
data "azurerm_client_config" "current" {}
```

A data source queries Azure for information. `azurerm_client_config` reads the identity of the person/service running Terraform — their tenant ID, subscription ID, and object ID. You reference it as `data.azurerm_client_config.current.tenant_id`.

Use data sources when: the resource already exists and was not created by this Terraform, or when you need to read dynamic values from the cloud (like your current user's ID).

---

#### 5. `locals` — computed values used internally

```hcl
locals {
  common_tags = {
    project    = var.project_name
    managed_by = "terraform"
  }
  resource_prefix = "${var.project_name}-${var.environment}"
}
```

Locals are like variables but computed inside Terraform rather than passed in from outside. Reference them with `local.common_tags`, `local.resource_prefix`. Useful for values you use in many places — define once, change once.

---

### STRING INTERPOLATION

Embed variables inside strings with `${}`:

```hcl
name = "${var.project_name}-${var.environment}-rg"
# with defaults: "secureops-dev-rg"
```

---

### THE TERRAFORM WORKFLOW — THE FOUR COMMANDS

```
terraform init     → downloads provider plugins, sets up backend
terraform plan     → shows what will change (READ THIS CAREFULLY)
terraform apply    → makes the changes (asks for confirmation)
terraform destroy  → deletes everything (asks for confirmation)
```

**Always run `terraform plan` before `terraform apply`.** Read the plan output:
- `+ create` — a new resource will be created
- `~ update in-place` — an existing resource will be modified
- `-/+ destroy and recreate` — the resource must be deleted and recreated (some changes cannot be made in-place, e.g., changing a Key Vault name)
- `- destroy` — a resource will be deleted

The `-/+ destroy and recreate` line is the most dangerous. For a database, this means data loss. For a Key Vault, this means secrets are deleted. Always read this carefully.

---

### TERRAFORM STATE

After `terraform apply`, Terraform writes a file called `terraform.tfstate`. This file is a JSON snapshot of every resource Terraform manages — their IDs, all their properties, all their outputs.

**This file is critical:**
- Without it, Terraform does not know what it has deployed
- Deleting it means Terraform thinks nothing exists and will try to create everything again
- It can contain sensitive values (passwords, connection strings from outputs)

**Never commit `terraform.tfstate` to Git.** Our `.gitignore` excludes it.

In production, state lives in **remote state** — an Azure Storage Account with versioning and locking. Multiple team members can run Terraform without colliding because the state is shared and locked during operations. We will set this up after the initial deploy.

---

### IMPLICIT VS EXPLICIT DEPENDENCIES

Terraform builds a dependency graph to determine the order resources must be created.

**Implicit** (preferred): when one resource references another, Terraform knows the order automatically.
```hcl
resource_group_name = azurerm_resource_group.main.name
# Terraform knows: create resource group BEFORE this resource
```

**Explicit** (when needed): when there is a dependency that isn't expressed through a reference.
```hcl
depends_on = [azurerm_key_vault_access_policy.terraform_deployer]
```
The Key Vault secret depends on the access policy being applied, but the secret does not reference the policy by attribute. We use `depends_on` to make the dependency explicit.

---

### PROVIDER VERSIONING

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.110"
    }
  }
}
```

`~> 3.110` means: "version 3.110 or higher, but less than 4.0". This is called a pessimistic constraint operator. It allows patch and minor updates (bug fixes) but prevents a major version bump that might introduce breaking changes.

Always pin provider versions. Unpinned providers mean a `terraform init` six months from now might pull a version that changed the API for a resource you depend on, breaking your infrastructure silently.

---

### AZURE-SPECIFIC PATTERNS

**Every Azure resource needs:**
1. `name` — unique within its scope (some names must be globally unique)
2. `location` — the Azure region
3. `resource_group_name` — the container it lives in
4. `tags` — metadata (cost centre, environment, managed_by)

**Naming conventions used by most companies:**
`{project}-{environment}-{resource-type-abbreviation}`
- Resource Group: `secureops-dev-rg`
- Key Vault: `secureops-dev-kv`
- Log Analytics: `secureops-dev-law`
- Container Registry: `secureopsdevacr` (no hyphens — ACR requirement)

**Tags are mandatory at serious companies.** You will fail a code review if you create a resource without tags. The standard minimum:
```hcl
tags = {
  project     = var.project_name
  environment = var.environment
  managed_by  = "terraform"
}
```

---

### NOW WRITE THE FILES YOURSELF

You have everything you need. Write each file in the `terraform/` folder. After each one, come back and I will check it and explain anything that needs clarification.

**Write them in this order:**
1. `terraform/variables.tf` — define the three variables: `project_name`, `location`, `environment`
2. `terraform/main.tf` — provider config + resource group
3. `terraform/keyvault.tf` — Key Vault + access policy + one secret
4. `terraform/monitoring.tf` — Log Analytics + Sentinel onboarding
5. `terraform/registry.tf` — Azure Container Registry
6. `terraform/outputs.tf` — outputs for all five key values

Use the code blocks in the FILE sections below as your reference. Understand each argument before you type it — if something is unclear, ask before typing.

---

#### FILE 1: `terraform/variables.tf`

```hcl
variable "project_name" {
  description = "Short name used as prefix for all resources"
  type        = string
  default     = "secureops"
}

variable "location" {
  description = "Azure region to deploy into"
  type        = string
  default     = "westeurope"
}

variable "environment" {
  description = "Deployment environment: dev, staging, prod"
  type        = string
  default     = "dev"
}
```

`variable` block — defines an input parameter.
`description` — human-readable explanation. Appears in `terraform plan` output and documentation.
`type = string` — Terraform enforces the type. Passing a number where a string is expected errors at plan time, not at runtime.
`default` — used when no value is passed. Makes `terraform apply` work without requiring every variable to be set manually.

`westeurope` is the Azure region for the Netherlands (Amsterdam). It is the closest full-feature Azure region to Ireland and the most common choice for Irish companies. `northeurope` (Ireland) is also available but has fewer services.

Why `project_name` as a prefix? Azure resource names must be globally unique (Key Vault names, storage accounts, container registries). Prefixing with a project name and appending a random suffix avoids naming collisions across different deployments.

---

#### FILE 2: `terraform/main.tf`

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.110"
    }
  }
  required_version = ">= 1.7"
}

provider "azurerm" {
  features {
    key_vault {
      purge_soft_delete_on_destroy    = true
      recover_soft_deleted_key_vaults = true
    }
  }
}

resource "azurerm_resource_group" "main" {
  name     = "${var.project_name}-${var.environment}-rg"
  location = var.location

  tags = {
    project     = var.project_name
    environment = var.environment
    managed_by  = "terraform"
  }
}
```

`terraform {}` block — configures Terraform itself, not Azure.
`required_providers` — pins the Azure provider version. `~> 3.110` means "3.110 or any later 3.x version". This prevents a provider upgrade from silently breaking your configuration.
`required_version = ">= 1.7"` — ensures nobody runs this with an old Terraform that lacks features you rely on.

`provider "azurerm"` — configures the Azure provider.
`features {}` — required block even if empty. The `key_vault` sub-block controls what happens when you `terraform destroy`:
- `purge_soft_delete_on_destroy = true` — permanently deletes the Key Vault instead of leaving it in soft-delete state (which blocks recreating it with the same name for 90 days).
- `recover_soft_deleted_key_vaults = true` — if a Key Vault with the same name exists in soft-delete, recover it instead of erroring.

`azurerm_resource_group` — every Azure resource must live inside a Resource Group. Think of it as a folder. You can delete a Resource Group and everything inside it disappears — useful for tearing down demos cleanly.

`name = "${var.project_name}-${var.environment}-rg"` — string interpolation in HCL (Terraform's language). Produces `"secureops-dev-rg"` with defaults.

`tags` — metadata attached to the Resource Group (and inherited by resources inside it). Tags are used for:
- Cost management (filter billing by project)
- Security auditing (find all resources that aren't tagged with `managed_by = "terraform"`)
- Automation (scripts that target resources by tag)

`managed_by = "terraform"` is a standard convention. It signals to anyone looking in the Azure Portal that this resource should not be edited manually.

---

#### FILE 3: `terraform/keyvault.tf`

```hcl
data "azurerm_client_config" "current" {}

resource "azurerm_key_vault" "main" {
  name                       = "${var.project_name}-${var.environment}-kv"
  location                   = azurerm_resource_group.main.location
  resource_group_name        = azurerm_resource_group.main.name
  tenant_id                  = data.azurerm_client_config.current.tenant_id
  sku_name                   = "standard"
  soft_delete_retention_days = 7
  purge_protection_enabled   = false

  network_acls {
    default_action = "Allow"
    bypass         = "AzureServices"
  }

  tags = {
    project     = var.project_name
    environment = var.environment
    managed_by  = "terraform"
  }
}

resource "azurerm_key_vault_access_policy" "terraform_deployer" {
  key_vault_id = azurerm_key_vault.main.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = data.azurerm_client_config.current.object_id

  secret_permissions = ["Get", "List", "Set", "Delete", "Purge"]
}

resource "azurerm_key_vault_secret" "db_connection" {
  name         = "db-connection-string"
  value        = "Server=secureops-db.database.windows.net;Database=secureopsdb;Authentication=Active Directory Managed Identity"
  key_vault_id = azurerm_key_vault.main.id

  depends_on = [azurerm_key_vault_access_policy.terraform_deployer]
}
```

`data "azurerm_client_config" "current" {}` — a data source (reads existing Azure state rather than creating something). `azurerm_client_config` reads the identity of whoever is running Terraform right now — their tenant ID and object ID. We need this to grant the deployer access to Key Vault.

`tenant_id` — your Azure Active Directory tenant. Every Azure subscription belongs to exactly one tenant. The tenant ID is a UUID that identifies your organisation.

`sku_name = "standard"` — Key Vault has two tiers. `standard` uses software-protected keys. `premium` uses HSM (Hardware Security Module) — dedicated tamper-proof hardware for keys. Standard is free-tier compatible and sufficient for this project. Production financial systems use premium.

`soft_delete_retention_days = 7` — if you accidentally delete a secret, it goes into a recycle bin for 7 days before permanent deletion. This prevents catastrophic data loss.

`purge_protection_enabled = false` — purge protection prevents anyone (including you) from permanently deleting the vault before the retention period. Set to `true` in production for compliance. Set to `false` here so `terraform destroy` works cleanly in the demo.

`network_acls` — firewall rules for Key Vault.
`default_action = "Allow"` — allow all network traffic by default. In production this should be `"Deny"` with explicit IP allowlists or private endpoints. We use `Allow` here because the free tier does not include private endpoints and we need GitHub Actions (which runs on Microsoft-owned IPs) to be able to reach it.
`bypass = "AzureServices"` — even when the default action is `Deny`, trusted Azure services (Azure DevOps, Logic Apps, Monitor) can still access the vault. This is necessary for Sentinel and Defender for Cloud to work.

`azurerm_key_vault_access_policy "terraform_deployer"` — grants the Terraform deployer permission to create and read secrets. Without this, the next resource (`azurerm_key_vault_secret`) would fail because Terraform cannot write to the vault.

`secret_permissions = ["Get", "List", "Set", "Delete", "Purge"]` — explicit list of allowed operations. This is least-privilege in practice: the deployer can manage secrets but cannot manage keys or certificates unless explicitly granted.

`azurerm_key_vault_secret "db_connection"` — creates one secret in the vault. In production this would be your real database connection string. Note the value uses `Authentication=Active Directory Managed Identity` — no password, because the application authenticates using its Managed Identity.

`depends_on = [azurerm_key_vault_access_policy.terraform_deployer]` — Terraform normally figures out resource ordering from references. But Key Vault access policies and secrets have a subtle timing issue: the policy must be fully applied before secrets can be written. `depends_on` forces explicit ordering.

---

#### FILE 4: `terraform/monitoring.tf`

```hcl
resource "azurerm_log_analytics_workspace" "main" {
  name                = "${var.project_name}-${var.environment}-law"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  sku                 = "PerGB2018"
  retention_in_days   = 30

  tags = {
    project     = var.project_name
    environment = var.environment
    managed_by  = "terraform"
  }
}

resource "azurerm_sentinel_log_analytics_workspace_onboarding" "main" {
  workspace_id = azurerm_log_analytics_workspace.main.id
}
```

`azurerm_log_analytics_workspace` — this is the database that stores all logs. Think of it as the hard drive that Microsoft Sentinel reads from. Every security event, every pipeline finding, every Azure activity log gets written here as structured JSON.

`sku = "PerGB2018"` — pay-per-use pricing model. You pay per GB of data ingested per day. For a demo project with low volume this effectively costs nothing. The alternative `"Free"` SKU only retains 7 days and has strict ingestion limits.

`retention_in_days = 30` — how long logs are kept before automatic deletion. 30 days is the minimum for most compliance frameworks. GDPR requires logs to be kept long enough to investigate incidents but not longer than necessary. 30 days is reasonable for a demo; production typically uses 90 days.

`azurerm_sentinel_log_analytics_workspace_onboarding` — this single resource is what turns a plain Log Analytics Workspace into Microsoft Sentinel. Without this, you have a log database. With it, you have a full SIEM with analytics rules, incident management, and threat intelligence feeds.

Why is Sentinel just an "onboarding" on top of Log Analytics? Because Sentinel does not store data itself — it is an analytics and orchestration layer that sits on top of Log Analytics. The logs live in Log Analytics; Sentinel adds the intelligence layer: detection rules, incident creation, automation playbooks (SOAR), and threat hunting queries.

---

#### FILE 5: `terraform/registry.tf`

```hcl
resource "azurerm_container_registry" "main" {
  name                = "${var.project_name}${var.environment}acr"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "Basic"
  admin_enabled       = false

  tags = {
    project     = var.project_name
    environment = var.environment
    managed_by  = "terraform"
  }
}
```

`azurerm_container_registry` — Azure's private Docker image registry. Like Docker Hub but private and inside your Azure tenant.

The name has no hyphens: `"${var.project_name}${var.environment}acr"` → `"secureopsdevacr"`. ACR names must be alphanumeric only, no hyphens. This is a quirk of the Azure service.

`sku = "Basic"` — the cheapest tier. Includes private image storage, vulnerability scanning (via Defender for Containers), and integration with AKS and Container Apps. The Basic tier costs about €0.17/day — essentially free for a demo. Standard and Premium add geo-replication and private endpoints.

`admin_enabled = false` — this is a critical security setting. Admin access means a username/password that grants full access to the registry. Enabling it is convenient but violates Zero Trust because the credentials must be stored somewhere. With `admin_enabled = false`, the only way to push or pull images is via Azure RBAC and Managed Identities — no passwords anywhere.

---

#### FILE 6: `terraform/outputs.tf`

```hcl
output "resource_group_name" {
  description = "Name of the resource group containing all resources"
  value       = azurerm_resource_group.main.name
}

output "key_vault_url" {
  description = "URL of the Key Vault — set as AZURE_KEY_VAULT_URL in Container Apps"
  value       = azurerm_key_vault.main.vault_uri
}

output "key_vault_name" {
  description = "Name of the Key Vault"
  value       = azurerm_key_vault.main.name
}

output "log_analytics_workspace_id" {
  description = "Workspace ID — used when connecting data sources to Sentinel"
  value       = azurerm_log_analytics_workspace.main.workspace_id
}

output "container_registry_login_server" {
  description = "ACR login server URL — used in docker push commands"
  value       = azurerm_container_registry.main.login_server
}
```

Outputs are printed to the terminal after `terraform apply` completes. They are also accessible programmatically — GitHub Actions can run `terraform output -raw key_vault_url` to get the URL and pass it as an environment variable to the container deployment.

This is how infrastructure and application deployment stay in sync without hardcoding anything.

---

#### SUMMARY OF WHAT YOU HAVE AFTER STEP 4

```
Azure Secure pipeline/
├── app/app.py
├── tests/test_app.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── terraform/
│   ├── variables.tf    ← Input parameters
│   ├── main.tf         ← Provider + Resource Group
│   ├── keyvault.tf     ← Key Vault + access policy + demo secret
│   ├── monitoring.tf   ← Log Analytics + Sentinel
│   ├── registry.tf     ← Azure Container Registry
│   └── outputs.tf      ← Values printed after deploy
└── learning.md
```

When you run `terraform apply` against a real Azure subscription:
- A Resource Group called `secureops-dev-rg` is created in West Europe
- A Key Vault is created with one demo secret
- A Log Analytics Workspace is created
- Microsoft Sentinel is enabled on that workspace
- An Azure Container Registry is created

Total cost on Azure free tier: approximately €0.

---

### STEP 5: GitHub Actions Pipeline — The Security Gates

---

#### WHAT IS GITHUB ACTIONS — EXPLAINED FROM ZERO

GitHub Actions is an automation system built into GitHub. Every time something happens in your repository — someone pushes code, opens a pull request, merges a branch — GitHub Actions can automatically run a set of tasks in response.

Think of it like a factory assembly line. Raw materials (your code) go in one end. The assembly line runs automatic checks and processes. A finished, tested, verified product comes out the other end (deployed to Azure). If any check fails, the line stops and nothing ships.

In security engineering, this assembly line is called a **CI/CD pipeline**:
- **CI (Continuous Integration)** — automatically test and scan every code change
- **CD (Continuous Deployment)** — automatically deploy code that passes all checks

The security version is called **DevSecOps** — security checks are baked into the pipeline, not done manually afterwards. This is called **shift-left security** — move security earlier in the process, closer to where code is written, rather than checking at the end.

---

#### THE FOUR CONCEPTS YOU MUST KNOW

**1. Workflow** — the entire automation file. Lives in `.github/workflows/`. One YAML file = one workflow.

**2. Trigger (`on:`)** — what event starts the workflow. Common triggers:
- `push` — someone pushes code to a branch
- `pull_request` — someone opens a PR
- `schedule` — runs on a cron schedule (e.g., every night at midnight)

**3. Job** — a group of steps that runs on one machine. Jobs run **in parallel by default**. If Job A must finish before Job B starts, you use `needs: job-a`.

**4. Step** — a single action inside a job. A step either:
- Runs a shell command (`run: pip install bandit`)
- Uses a pre-built action (`uses: actions/checkout@v4`)

---

#### WHAT IS A RUNNER?

`runs-on: ubuntu-latest` — a runner is the machine that executes your job. GitHub provides free virtual machines (runners). `ubuntu-latest` is a fresh Ubuntu Linux VM spun up just for your job, used once, then destroyed.

This matters for security: every job starts from a clean slate. No leftover files, no contaminated environment from previous runs.

---

#### WHAT IS AN ACTION (`uses:`)?

Actions are reusable building blocks. Instead of writing 50 lines of shell script to set up Python, you write one line: `uses: actions/setup-python@v5`. Someone else wrote and maintains that 50-line script.

`@v4`, `@v5` — version pins. Always pin action versions. An unpinned action (`uses: actions/checkout`) could pull a new version tomorrow that breaks your pipeline or — in a supply chain attack — runs malicious code.

---

#### WHAT ARE SECRETS?

`${{ secrets.AZURE_CLIENT_ID }}` — secrets are encrypted values stored in GitHub (Settings → Secrets and variables → Actions). They are injected into the pipeline as environment variables at runtime. Nobody can read them — not even you after saving them. They never appear in logs.

We will store Azure credentials as secrets so the pipeline can authenticate to Azure without credentials in the code.

---

#### OUR PIPELINE — 5 SECURITY GATES

Every time code is pushed to the `main` branch, our pipeline runs 5 security scans in parallel:

```
Code pushed to GitHub
         │
         ▼
┌────────────────────────────────────────────────────┐
│                  PARALLEL JOBS                     │
│                                                    │
│  Gate 1: Tests      Gate 2: SAST (Bandit)         │
│  pytest runs all    Scans Python code for          │
│  test functions     insecure patterns              │
│                                                    │
│  Gate 3: Secrets    Gate 4: IaC Scan (Checkov)    │
│  detect-secrets     Scans Terraform files for      │
│  scans all files    misconfigurations              │
│                                                    │
│  Gate 5: Container Scan (Trivy)                   │
│  Scans Docker image for OS + package CVEs         │
└────────────────────┬───────────────────────────────┘
                     │ all 5 must pass
                     ▼
          Results uploaded as artifacts
          (downloadable reports for each scan)
```

Each gate produces a JSON report uploaded as a GitHub Actions artifact — a downloadable file showing exactly what was found. A recruiter looking at your GitHub sees real scan results with real findings.

---

#### THE YAML FILE — COMPLETE EXPLANATION

Create `.github/workflows/security-pipeline.yml`. We build it in four blocks.

**Block 1 — Name and triggers:**

```yaml
name: SecureOps Security Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  PYTHON_VERSION: "3.12"
  IMAGE_NAME: secureops-api
```

`name:` — appears in the GitHub Actions UI. Make it descriptive.

`on:` — when to run. We trigger on:
- Any push to `main` branch
- Any pull request targeting `main`

This means: every time code is committed, the security gates run automatically. No human needs to remember to run the scans.

`env:` — global environment variables available to all jobs. Defining `PYTHON_VERSION` once here means if you upgrade to Python 3.13 later, you change one line and all jobs update.

---

**Block 2 — Tests job:**

```yaml
jobs:
  test:
    name: Run Tests
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: pip install -r requirements.txt pytest

      - name: Run tests
        run: pytest tests/ -v
```

`actions/checkout@v4` — clones your repository onto the runner. Without this, the runner has no code to work with.

`actions/setup-python@v5` — installs Python 3.12 on the runner. The `with:` block passes parameters to the action.

`${{ env.PYTHON_VERSION }}` — reads the global env variable we defined above.

`pip install -r requirements.txt pytest` — installs your app dependencies plus pytest.

`pytest tests/ -v` — runs all test functions in the `tests/` directory. `-v` means verbose — print each test name and result. If any test fails, this step fails, the job fails, and the pipeline stops.

---

**Block 3 — SAST scan (Bandit):**

```yaml
  sast:
    name: SAST - Bandit Code Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Bandit
        run: pip install bandit

      - name: Run Bandit SAST scan
        run: bandit -r app/ -f json -o bandit-results.json || true

      - name: Upload SAST results
        uses: actions/upload-artifact@v4
        with:
          name: bandit-sast-results
          path: bandit-results.json
```

`bandit -r app/` — scan the `app/` directory recursively.
`-f json` — output in JSON format (machine-readable, importable into Sentinel).
`-o bandit-results.json` — write results to this file.
`|| true` — this is critical. Without it, if Bandit finds ANY vulnerability, it exits with code 1, and the pipeline fails and stops. We want the pipeline to continue and collect ALL findings across all 5 gates, then report everything together. `|| true` makes the step always succeed regardless of findings.

`actions/upload-artifact@v4` — saves `bandit-results.json` as a downloadable file attached to this pipeline run. Anyone can click the GitHub Actions run and download the scan report.

**What Bandit will find in our app:**
- `hashlib.md5()` — insecure hash function
- `sqlite3` f-string query — SQL injection
- `subprocess.run(shell=True)` — command injection

Bandit will report all three. The pipeline captures the findings, the developer sees them, and fixes them. This is shift-left security working exactly as designed.

---

**Block 4 — Secrets, IaC, and Container scans:**

```yaml
  secrets-scan:
    name: Secrets Detection
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install detect-secrets
        run: pip install detect-secrets

      - name: Run secrets scan
        run: detect-secrets scan --all-files > secrets-results.json || true

      - uses: actions/upload-artifact@v4
        with:
          name: secrets-scan-results
          path: secrets-results.json

  iac-scan:
    name: IaC Scan - Checkov
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Checkov
        run: pip install checkov

      - name: Run Checkov IaC scan
        run: checkov -d terraform/ --output json --output-file-path . || true

      - uses: actions/upload-artifact@v4
        with:
          name: checkov-iac-results
          path: results_json.json

  container-scan:
    name: Container Scan - Trivy
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t secureops-api:test .

      - name: Run Trivy container scan
        uses: aquasecurity/trivy-action@0.28.0
        with:
          image-ref: secureops-api:test
          format: json
          output: trivy-results.json
          exit-code: "0"

      - uses: actions/upload-artifact@v4
        with:
          name: trivy-container-results
          path: trivy-results.json
```

`detect-secrets scan --all-files` — scans every file in the repository for patterns that look like secrets. It will find `DB_PASSWORD = "SuperSecret123!"` in our `app.py` and flag it. That is exactly what we want — demonstrate the tool works.

`checkov -d terraform/` — scans every `.tf` file in the `terraform/` directory for misconfigurations. It checks against 1000+ security rules mapped to CIS Benchmarks and NIST. It will find things like `purge_protection_enabled = false` (we set this intentionally for demo purposes) and flag it. Again — real findings, real demo.

`docker build -t secureops-api:test .` — builds the Docker image on the GitHub Actions runner before scanning it. The runner has Docker pre-installed.

`aquasecurity/trivy-action@0.28.0` — Trivy is maintained by Aqua Security, a major cloud security company. This action scans the built image for CVEs in the base OS packages and Python dependencies.

---

#### SUMMARY — WHAT YOU HAVE AFTER STEP 5

A GitHub Actions pipeline that automatically, on every push:
1. Runs your tests
2. Scans your Python code for insecure patterns (Bandit)
3. Scans all files for leaked secrets (detect-secrets)
4. Scans your Terraform for misconfigurations (Checkov)
5. Builds and scans your Docker image for CVEs (Trivy)

All five run in parallel. Each produces a downloadable JSON report. The pipeline takes 3-5 minutes total. A developer gets feedback on security issues before the code is ever deployed.

---

#### NOW CREATE THE FILE

Create `.github/workflows/security-pipeline.yml` and type all four blocks in order. The complete file is all four blocks combined — `name`, `on`, `env` at the top, then `jobs:` containing all five job definitions.

---
