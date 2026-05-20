# SecureOps Pipeline
### AI-Augmented DevSecOps Platform on Azure

![Pipeline](https://github.com/shaik0116/secureops-pipeline/actions/workflows/security-pipeline.yml/badge.svg)
![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?logo=terraform)
![Azure](https://img.shields.io/badge/Cloud-Azure-0078D4?logo=microsoftazure)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python)
![Security](https://img.shields.io/badge/Security-DevSecOps-red)

---

## What This Project Does

SecureOps Pipeline is a production-grade DevSecOps platform that automatically scans every code commit for security vulnerabilities before it reaches Azure infrastructure. It combines five industry-standard security tools, Microsoft Sentinel SIEM, and Google Gemini AI to deliver plain-English risk reports to security teams — all triggered automatically on every `git push`.

**The problem it solves:** Security vulnerabilities discovered after deployment cost 10x more to fix than those caught during development. This pipeline enforces security at every stage of the software delivery lifecycle — from source code to container image to cloud infrastructure.

---

## Architecture

```
Developer pushes code to GitHub
              │
              ▼
┌─────────────────────────────────────────────────────────┐
│              GitHub Actions CI/CD Pipeline               │
│                                                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │   Tests  │ │  SAST    │ │ Secrets  │ │   IaC    │  │
│  │  pytest  │ │  Bandit  │ │ detect-  │ │ Checkov  │  │
│  │          │ │          │ │ secrets  │ │          │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│                                                          │
│              ┌──────────────────┐                        │
│              │ Container Scan   │                        │
│              │     Trivy        │                        │
│              └──────────────────┘                        │
│                       │                                  │
│                       ▼                                  │
│              ┌──────────────────┐                        │
│              │  AI Risk Summary │                        │
│              │  Google Gemini   │                        │
│              └──────────────────┘                        │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                  Azure Infrastructure                    │
│                  (Terraform IaC)                         │
│                                                          │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │  Key Vault  │  │  Sentinel    │  │  Container    │  │
│  │  (Secrets)  │  │  (SIEM)      │  │  Registry     │  │
│  └─────────────┘  └──────────────┘  └───────────────┘  │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │  Log Analytics Workspace (Security Logs)        │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

## Security Gates

| Gate | Tool | What It Detects |
|------|------|-----------------|
| Unit Tests | pytest | Broken application code |
| SAST | Bandit | SQL injection, command injection, weak cryptography |
| Secrets Detection | detect-secrets | Hardcoded passwords, API keys, tokens |
| IaC Security | Checkov | Terraform misconfigurations mapped to CIS Benchmarks |
| Container Scan | Trivy | OS and package CVEs in Docker images |
| AI Risk Summary | Google Gemini | Plain-English risk report for non-technical stakeholders |

---

## Real Findings From This Pipeline

The demo application contains four intentional vulnerabilities that the pipeline detects automatically:

```
SAST (Bandit):        6 issues — 2 HIGH, 2 MEDIUM
  ↳ Weak MD5 hashing (app.py line 19)
  ↳ Command injection via subprocess shell=True (app.py line 38)
  ↳ SQL injection via f-string query (app.py line 29)

Secrets Detection:    2 potential secrets found
  ↳ Hardcoded DB_PASSWORD in application code

IaC Scan (Checkov):   15 checks failed, 3 passed
  ↳ Terraform misconfigurations flagged against CIS Azure Benchmark

Container Scan:       4 HIGH CVEs in base image packages
```

---

## Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| Cloud | Microsoft Azure | Infrastructure hosting |
| IaC | Terraform | Declarative infrastructure as code |
| SIEM | Microsoft Sentinel | Threat detection and incident management |
| Secrets | Azure Key Vault | Zero-trust credential management |
| CI/CD | GitHub Actions | Automated security pipeline |
| SAST | Bandit | Python static analysis |
| Secrets Scan | detect-secrets | Credential leak prevention |
| IaC Scan | Checkov | Infrastructure misconfiguration detection |
| Container Scan | Trivy | CVE scanning for Docker images |
| AI | Google Gemini | AI-powered risk summarisation |
| Language | Python 3.12 | Application and automation scripts |
| Container | Docker + Gunicorn | Production-hardened containerisation |

---

## Azure Infrastructure

All infrastructure is deployed via Terraform with Zero Trust principles:

```hcl
Resources deployed to secureops-dev-rg (West Europe):
  ├── azurerm_key_vault           — Secret storage, no admin passwords
  ├── azurerm_key_vault_access_policy  — Least-privilege RBAC
  ├── azurerm_key_vault_secret    — Managed Identity connection strings
  ├── azurerm_log_analytics_workspace  — Centralised security logging
  ├── azurerm_sentinel_onboarding — SIEM activation
  └── azurerm_container_registry  — Private image store, admin disabled
```

**Security design decisions:**
- `admin_enabled = false` on Container Registry — Managed Identity only, no passwords
- `purge_protection_enabled` — configurable per environment
- `network_acls` with `AzureServices` bypass — controls network access
- All secrets retrieved via `ManagedIdentityCredential` — zero hardcoded credentials

---

## Project Structure

```
secureops-pipeline/
├── app/
│   └── app.py                    # Flask API with vulnerability demonstrations
├── terraform/
│   ├── variables.tf              # Input parameters (project, location, environment)
│   ├── main.tf                   # Provider config + resource group
│   ├── keyvault.tf               # Key Vault + access policy + secrets
│   ├── monitoring.tf             # Log Analytics + Microsoft Sentinel
│   ├── registry.tf               # Azure Container Registry
│   └── outputs.tf                # Post-deploy values for pipeline
├── scripts/
│   └── ai_summariser.py          # Gemini AI risk report generator
├── tests/
│   └── test_app.py               # pytest test suite
├── .github/
│   └── workflows/
│       └── security-pipeline.yml # 6-job GitHub Actions pipeline
├── Dockerfile                    # Non-root, minimal base, gunicorn
├── .dockerignore                 # Prevents secrets entering images
└── requirements.txt              # Pinned Python dependencies
```

---

## How to Deploy

### Prerequisites
- Azure subscription (free tier compatible)
- Terraform >= 1.7
- Azure CLI
- Docker

### 1. Clone and authenticate
```bash
git clone https://github.com/shaik0116/secureops-pipeline.git
cd secureops-pipeline
az login
```

### 2. Deploy Azure infrastructure
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

### 3. Add GitHub Secrets
In repository Settings → Secrets → Actions:
```
GEMINI_API_KEY   — Google AI Studio API key
```

### 4. Trigger the pipeline
```bash
git push origin main
# Pipeline runs automatically — view at Actions tab
```

---

## Security Concepts Demonstrated

**Zero Trust Architecture**
Applications authenticate using Azure Managed Identities — no passwords stored anywhere in code, configuration files, or environment variables.

**Shift-Left Security**
Security checks run at commit time, not after deployment. Vulnerabilities are caught when they cost least to fix.

**Defence in Depth**
Six independent security layers — each catches different vulnerability classes. An attacker must bypass all six simultaneously.

**Principle of Least Privilege**
Every Azure identity (Key Vault access policy, Container Registry) receives only the minimum permissions required for its function.

**Infrastructure as Code Security**
Terraform files are scanned by Checkov against CIS Azure Benchmark before any resource is deployed, making infrastructure misconfigurations reviewable and preventable.

---

## Compliance Mappings

| Control | Framework | Implementation |
|---------|-----------|----------------|
| Access control | CIS Azure 1.0 | RBAC + Managed Identity |
| Secret management | NIST CSF PR.AC | Azure Key Vault |
| Vulnerability management | NIST CSF ID.RA | Bandit + Trivy + Checkov |
| Audit logging | ISO 27001 A.12.4 | Log Analytics + Sentinel |
| Credential hygiene | OWASP A02 | detect-secrets + Key Vault |

---

## Author

**Shaik** — Cloud Security Engineer  
MSc Cybersecurity, Technological University Dublin (2025)  
3 years cloud engineering experience  
Dublin, Ireland

*Open to Cloud Security Engineer, DevSecOps, and IAM/Entra ID roles in Dublin*

---

*Built with Azure, Terraform, GitHub Actions, and a genuine interest in making cloud infrastructure secure by default.*
