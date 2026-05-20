# Terraform — Complete Self-Teaching Guide
### From Zero to Writing Real Infrastructure Without Help

---

## SECTION 1: WHAT TERRAFORM IS AND WHY IT EXISTS

### The problem it solves

Imagine you are a cloud engineer at a company. You need to create:
- A database
- A storage account
- A virtual network
- A firewall
- 3 virtual machines

You could log into the Azure Portal and click through menus to create each one. That takes 2 hours, and if you need to do it again for staging and production environments, you do it 3 times. If a colleague needs to recreate your setup, they have to guess what settings you chose. If something breaks, you have no record of what the configuration was.

**Terraform solves this by turning infrastructure into code.**

Instead of clicking, you write a text file that says "I want a database with these settings, a storage account with these settings..." and Terraform creates it all automatically. That same file creates dev, staging, and production environments identically. That file lives in Git — version controlled, reviewable, auditable.

### The single most important mental model

Terraform is **declarative**. You describe *what you want to exist*, not *how to create it*.

- **Imperative** (normal programming): "Create a VM. Then install Python on it. Then start the app."
- **Declarative** (Terraform): "A VM with Python installed and the app running should exist."

Terraform calculates the difference between what exists now and what you described, then takes the minimum steps to close that gap. If the VM already exists, it does nothing. If only the Python installation is missing, it only installs Python.

---

## SECTION 2: INSTALLING TERRAFORM AND THE AZURE CLI

### Step 1 — Install Terraform

Go to https://developer.hashicorp.com/terraform/install and download for Windows.
Or with winget (Windows package manager):
```
winget install HashiCorp.Terraform
```
Verify: open a new terminal and run `terraform version`

### Step 2 — Install Azure CLI

```
winget install Microsoft.AzureCLI
```
Verify: `az version`

### Step 3 — Install the Azure Terraform VS Code extension

In VS Code Extensions panel, search for **HashiCorp Terraform**. Install it.
This gives you: syntax highlighting, autocomplete, format-on-save, inline documentation.

---

## SECTION 3: HOW TERRAFORM CONNECTS TO AZURE

This is the question most tutorials ignore and most beginners get stuck on.

Terraform needs **credentials** to talk to Azure — permission to create and modify resources in your subscription. There are three methods. You need to understand all three because you will use different ones in different contexts.

---

### METHOD 1: Azure CLI (for your laptop — local development)

This is the simplest method. You log in with the Azure CLI and Terraform automatically picks up your credentials.

**Step 1 — Log in:**
```bash
az login
```
A browser window opens. Sign in with your Azure account. The CLI stores a token on your machine.

**Step 2 — Select the right subscription (if you have more than one):**
```bash
az account list --output table
az account set --subscription "YOUR-SUBSCRIPTION-ID"
```

**Step 3 — Verify you are in the right account:**
```bash
az account show
```
This shows your subscription name, ID, and tenant ID.

**Step 4 — Run Terraform:**
```bash
terraform init
terraform plan
terraform apply
```
The `azurerm` provider sees the Azure CLI token and uses it automatically. No extra configuration needed.

**Why this works:** The Azure CLI stores a short-lived OAuth token after login. The Terraform Azure provider checks for this token automatically. This is the recommended method for local development because the token expires (you re-login periodically) — a stolen token has limited lifetime.

**When to use:** Running Terraform from your own laptop during development and learning.

---

### METHOD 2: Service Principal with Client Secret (for CI/CD pipelines — the old way)

A **Service Principal** is an identity in Azure Active Directory that represents an application or automation process — not a human. Think of it as a service account. It has its own client ID and a secret (password).

When GitHub Actions runs Terraform, it cannot do `az login` because there is no browser and no human. Instead it authenticates as a Service Principal.

**Step 1 — Create a Service Principal:**
```bash
az ad sp create-for-rbac \
  --name "secureops-terraform-sp" \
  --role "Contributor" \
  --scopes "/subscriptions/YOUR-SUBSCRIPTION-ID"
```

This outputs:
```json
{
  "appId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "displayName": "secureops-terraform-sp",
  "password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "tenant": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

**Step 2 — Set environment variables (Terraform reads these automatically):**
```bash
export ARM_CLIENT_ID="appId value"
export ARM_CLIENT_SECRET="password value"
export ARM_SUBSCRIPTION_ID="your subscription ID"
export ARM_TENANT_ID="tenant value"
```

In GitHub Actions, these become repository secrets set in Settings → Secrets and variables → Actions.

**Step 3 — The Terraform provider block needs no extra config:**
```hcl
provider "azurerm" {
  features {}
}
```
Terraform reads the `ARM_*` environment variables automatically.

**Security concern with this method:** The `password` (client secret) is a long-lived credential. If it leaks (committed to Git, exposed in logs), an attacker has permanent access until you rotate it. This is why the next method exists.

**When to use:** GitHub Actions pipelines when you cannot use OIDC (older setup, simpler to understand initially).

---

### METHOD 3: OIDC / Workload Identity Federation (for CI/CD — the modern, secure way)

This is the method you should use in production. It eliminates the long-lived client secret entirely.

**The idea:** Instead of GitHub Actions storing a password that grants Azure access, Azure trusts GitHub Actions directly. GitHub says "I am running a workflow from repository X on branch Y" and Azure verifies this claim cryptographically. No password is ever stored anywhere.

**Step 1 — Create a Service Principal (same as above, but without a secret):**
```bash
az ad app create --display-name "secureops-oidc-sp"
```
Note the `appId` from the output.

```bash
az ad sp create --id "THE-APP-ID"
```

**Step 2 — Assign the Contributor role:**
```bash
az role assignment create \
  --assignee "THE-APP-ID" \
  --role "Contributor" \
  --scope "/subscriptions/YOUR-SUBSCRIPTION-ID"
```

**Step 3 — Create a Federated Identity Credential:**
This is what links GitHub Actions to your Azure app. It says: "trust tokens from this GitHub repository's main branch."
```bash
az ad app federated-credential create \
  --id "THE-APP-ID" \
  --parameters '{
    "name": "github-actions-main",
    "issuer": "https://token.actions.githubusercontent.com",
    "subject": "repo:YOUR-GITHUB-USERNAME/YOUR-REPO-NAME:ref:refs/heads/main",
    "audiences": ["api://AzureADTokenExchange"]
  }'
```

**Step 4 — Store three values as GitHub repository secrets (no password):**
- `AZURE_CLIENT_ID` = the app ID
- `AZURE_TENANT_ID` = your tenant ID
- `AZURE_SUBSCRIPTION_ID` = your subscription ID

**Step 5 — In GitHub Actions workflow:**
```yaml
- uses: azure/login@v2
  with:
    client-id: ${{ secrets.AZURE_CLIENT_ID }}
    tenant-id: ${{ secrets.AZURE_TENANT_ID }}
    subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
```

**When to use:** All production GitHub Actions pipelines. No secrets to rotate, no passwords to leak.

---

### WHICH METHOD TO USE WHEN

| Context | Method | Why |
|---|---|---|
| Your laptop, learning | Azure CLI (`az login`) | Simplest, tokens expire automatically |
| GitHub Actions (learning) | Service Principal + Secret | Easier to set up initially |
| GitHub Actions (production) | OIDC / Workload Identity | No long-lived secrets, most secure |
| Terraform running on an Azure VM | Managed Identity | No credentials needed at all |

For **this project**, use Azure CLI on your laptop and Service Principal with Secret in GitHub Actions. Once the pipeline is working, you can upgrade to OIDC.

---

## SECTION 4: THE HCL LANGUAGE — COMPLETE SYNTAX GUIDE

HCL (HashiCorp Configuration Language) is what Terraform files are written in. It looks similar to JSON but is more readable.

### Block structure — the fundamental unit

Everything in HCL is a **block**:

```hcl
block_type "label_one" "label_two" {
  argument = value
  another  = "string"
  number   = 42
  flag     = true

  nested_block {
    inner = "value"
  }
}
```

Not all block types use two labels. Some use one, some use none.

### Data types

```hcl
# String
name = "secureops-dev-kv"

# Number
retention_in_days = 30

# Boolean
admin_enabled = false

# List (array)
allowed_ips = ["1.2.3.4", "5.6.7.8"]

# Map (key-value pairs)
tags = {
  environment = "dev"
  managed_by  = "terraform"
}

# String interpolation — embed variables inside strings
name = "${var.project_name}-${var.environment}-kv"
```

### Comments

```hcl
# This is a single-line comment

/* This is a
   multi-line comment */
```

---

## SECTION 5: THE FIVE BLOCK TYPES — COMPLETE REFERENCE

### 1. `terraform` block — configures Terraform itself

```hcl
terraform {
  required_version = ">= 1.7"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.110"
    }
  }

  # Optional: remote state storage (for teams)
  backend "azurerm" {
    resource_group_name  = "terraform-state-rg"
    storage_account_name = "tfstateaccount"
    container_name       = "tfstate"
    key                  = "secureops.tfstate"
  }
}
```

`required_version` — minimum Terraform version. Prevents junior engineers from running old Terraform.

`required_providers` — pins which providers to use and their versions:
- `~> 3.110` = any 3.x.x version >= 3.110 (patch and minor updates allowed, major blocked)
- `= 3.110.0` = exactly this version (strictest)
- `>= 3.0` = any version 3.0 or higher (too loose for production)

`backend` — where to store the state file. Without this block, state is local (`terraform.tfstate`). For teams, always use remote state.

---

### 2. `provider` block — configures the cloud provider plugin

```hcl
provider "azurerm" {
  features {
    key_vault {
      purge_soft_delete_on_destroy    = true
      recover_soft_deleted_key_vaults = true
    }
    resource_group {
      prevent_deletion_if_contains_resources = false
    }
  }
  subscription_id = "your-subscription-id"  # optional if set via env var
}
```

The `features {}` block is **mandatory** for the Azure provider even if empty. It controls behaviour of specific resources during destroy operations.

You rarely need to put credentials in the provider block — use environment variables (`ARM_*`) or Azure CLI instead. Credentials in code = credentials in Git history.

---

### 3. `variable` block — input parameters

```hcl
variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```

`description` — shown in `terraform plan` output and documentation. Always write one.
`type` — enforced at plan time. Types: `string`, `number`, `bool`, `list(type)`, `set(type)`, `map(type)`, `object({key = type})`, `any`
`default` — makes the variable optional. Without a default, Terraform asks you to provide a value interactively or via a `.tfvars` file.
`validation` — custom rules. The `condition` is any expression that returns `true` (valid) or `false` (invalid). `error_message` is shown when validation fails.

**Referencing variables:** `var.environment`

**Ways to pass values:**
```bash
# Command line
terraform apply -var="environment=prod"

# .tfvars file (create terraform.tfvars — never commit if it has secrets)
environment = "prod"
location    = "northeurope"

# Environment variable (TF_VAR_ prefix)
export TF_VAR_environment=prod
```

---

### 4. `locals` block — internal computed values

```hcl
locals {
  # Computed once, used many times
  resource_prefix = "${var.project_name}-${var.environment}"

  # Shared tags applied to every resource
  common_tags = {
    project     = var.project_name
    environment = var.environment
    managed_by  = "terraform"
    created_at  = "2026"
  }
}
```

**Referencing locals:** `local.resource_prefix`, `local.common_tags`

Rule of thumb: if you write the same string expression more than twice, put it in a local.

---

### 5. `resource` block — creates infrastructure

```hcl
resource "azurerm_key_vault" "main" {
  # Required arguments
  name                = "${local.resource_prefix}-kv"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"

  # Security settings
  soft_delete_retention_days = 7
  purge_protection_enabled   = false

  # Nested block
  network_acls {
    default_action = "Allow"
    bypass         = "AzureServices"
  }

  # Tags using local
  tags = local.common_tags
}
```

**The reference pattern — memorise this:**
```
resource_type.local_name.attribute
azurerm_key_vault.main.vault_uri
azurerm_resource_group.main.name
azurerm_key_vault.main.id
```

When you reference one resource inside another (`resource_group_name = azurerm_resource_group.main.name`), Terraform automatically knows it must create the resource group before the key vault. This is an **implicit dependency**.

---

### 6. `data` block — reads existing resources

```hcl
# Reads the identity of whoever is running Terraform
data "azurerm_client_config" "current" {}

# Reads an existing resource group (not created by this Terraform)
data "azurerm_resource_group" "existing" {
  name = "some-existing-rg"
}
```

**Referencing data sources:**
```
data.data_type.local_name.attribute
data.azurerm_client_config.current.tenant_id
data.azurerm_client_config.current.object_id
data.azurerm_resource_group.existing.location
```

---

### 7. `output` block — values after apply

```hcl
output "key_vault_url" {
  description = "Key Vault URI — set as AZURE_KEY_VAULT_URL in app config"
  value       = azurerm_key_vault.main.vault_uri
  sensitive   = false   # set true to hide from terminal output (still in state)
}
```

**Reading outputs after apply:**
```bash
terraform output                    # print all outputs
terraform output key_vault_url      # print one output
terraform output -raw key_vault_url # print without quotes (for scripts)
```

---

## SECTION 6: THE WORKFLOW IN DETAIL

### `terraform init`

Downloads provider plugins to `.terraform/` directory. Run once per project, and again if you add new providers.
```bash
terraform init
```

### `terraform validate`

Checks HCL syntax without connecting to Azure. Catches typos and type errors before plan.
```bash
terraform validate
```

### `terraform fmt`

Auto-formats `.tf` files to the canonical style (consistent indentation, aligned `=` signs). Run before every commit.
```bash
terraform fmt -recursive
```

### `terraform plan`

Connects to Azure, reads the current state, calculates what needs to change. Does not make any changes. **Always read this output before apply.**
```bash
terraform plan
terraform plan -out=tfplan  # save plan to file
```

**Reading plan output:**
```
+ resource will be created
~ resource will be updated in-place
- resource will be destroyed
-/+ resource will be destroyed and recreated
```

The `-/+ destroy and recreate` entry is the most dangerous. It means some argument cannot be changed in-place (e.g., a Key Vault name). The resource will be **deleted** and a new one created. For databases this means data loss. Read every `-/+` line carefully.

### `terraform apply`

Executes the changes. Asks for confirmation unless `-auto-approve` is passed.
```bash
terraform apply           # asks for confirmation
terraform apply tfplan    # applies a saved plan (no confirmation needed)
terraform apply -auto-approve  # skips confirmation (CI/CD use only)
```

### `terraform destroy`

Deletes everything Terraform manages. Asks for confirmation.
```bash
terraform destroy
```

In CI/CD you might not want to destroy automatically. Use this in your local dev environment to clean up after testing and avoid Azure costs.

---

## SECTION 7: STATE MANAGEMENT

### What state is

`terraform.tfstate` is a JSON file that maps your Terraform resource definitions to real Azure resource IDs. Without it, Terraform does not know what it deployed.

Example snippet:
```json
{
  "resources": [
    {
      "type": "azurerm_key_vault",
      "name": "main",
      "instances": [
        {
          "attributes": {
            "id": "/subscriptions/xxx/resourceGroups/secureops-dev-rg/providers/Microsoft.KeyVault/vaults/secureops-dev-kv",
            "vault_uri": "https://secureops-dev-kv.vault.azure.net/",
            "name": "secureops-dev-kv"
          }
        }
      ]
    }
  ]
}
```

### Never commit state to Git

The state file can contain:
- Resource IDs (help an attacker understand your infrastructure)
- Output values marked `sensitive = false` (including connection strings)
- Internal Azure identifiers

Add to `.gitignore`:
```
*.tfstate
*.tfstate.backup
.terraform/
```

### Remote state for teams (Azure Storage)

In a team, everyone needs to read and write the same state. Local state breaks immediately when two people run Terraform. Remote state in Azure Blob Storage with state locking prevents conflicts.

```hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "terraform-state-rg"
    storage_account_name = "secureopstfstate"  # globally unique name
    container_name       = "tfstate"
    key                  = "secureops-dev.tfstate"
  }
}
```

You create the storage account once manually (or with a bootstrap script), then all Terraform state lives there. Azure Blob Storage automatically versions state files, so you can roll back if a bad apply corrupts state.

---

## SECTION 8: READING THE TERRAFORM DOCUMENTATION

This is the skill that makes you independent. Every resource has documentation at:
**https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs**

How to use it:
1. Go to the URL above
2. In the left panel, find "Resources" → search for the resource type you need (e.g., "key_vault")
3. The page shows: required arguments, optional arguments, nested blocks, attributes (outputs), example usage, import instructions

**What each section means:**

- **Argument Reference** — arguments you put *inside* the resource block (`name = ...`, `location = ...`)
- **Required arguments** — you must provide these or Terraform errors
- **Optional arguments** — have defaults or are not needed in all cases
- **Attributes Reference** — values Terraform knows *after* the resource is created. These are what you use in `output` blocks and when referencing from other resources (e.g., `azurerm_key_vault.main.vault_uri` — `vault_uri` is an attribute)
- **Timeouts** — how long Terraform waits for each operation before giving up
- **Import** — how to bring an existing Azure resource under Terraform management without recreating it

**Practice exercise:** Before writing `keyvault.tf`, go to the documentation page for `azurerm_key_vault` and find every argument we use. Understand what it does before typing it.

---

## SECTION 9: COMMON PATTERNS IN PRODUCTION TERRAFORM

### Pattern 1: One module per major concern, not one file

Production codebases use modules (reusable packages of Terraform) rather than flat `.tf` files. For this project, separate files per concern is fine. At a company you will see:
```
modules/
  key-vault/
    main.tf
    variables.tf
    outputs.tf
  networking/
  monitoring/
environments/
  dev/
    main.tf
  prod/
    main.tf
```

### Pattern 2: Never hardcode IDs, names, or secrets

Wrong:
```hcl
tenant_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"  # hardcoded
```
Right:
```hcl
tenant_id = data.azurerm_client_config.current.tenant_id  # dynamic
```

### Pattern 3: Tags on everything

Every resource gets a `tags` block. Companies use tags for:
- Billing (which team owns this cost?)
- Security auditing (is everything managed by Terraform?)
- Automation (target all resources with `environment=prod` for a maintenance script)

### Pattern 4: Outputs for everything another system needs

If GitHub Actions, another Terraform module, or an application needs a value, make it an output. Do not hardcode URLs and IDs in pipeline files.

### Pattern 5: `prevent_destroy` for critical resources

```hcl
resource "azurerm_key_vault" "main" {
  lifecycle {
    prevent_destroy = true
  }
}
```
`terraform destroy` will error if it tries to delete this resource. Use on databases and vaults in production.

---

## SECTION 10: THE CHECKLIST FOR WRITING A NEW TERRAFORM FILE

Use this every time you write a new `.tf` file without help:

1. **Look up the resource** in the Terraform Registry documentation
2. **Identify required arguments** — what must you provide?
3. **Read optional arguments** — which ones affect security, cost, or reliability?
4. **Check for nested blocks** — does the resource have sub-configurations?
5. **Check attributes** — what values does the resource expose after creation?
6. **Write the resource** — use `local.resource_prefix` for naming, `local.common_tags` for tags, reference other resources by their Terraform address not hardcoded IDs
7. **Run `terraform validate`** — catches syntax errors immediately
8. **Run `terraform plan`** — read every `+` and `-/+` carefully before applying
9. **Run `terraform fmt`** — consistent formatting before committing

---

## SECTION 11: WRITING OUR PROJECT FILES — NOW YOU WRITE THEM

You now have everything needed to write the six Terraform files for the SecureOps Pipeline without copying from anywhere.

### What each file should contain

**`variables.tf`**
Define three variables. Each needs `description`, `type`, and `default`. Variables: `project_name` (string, default "secureops"), `location` (string, default "westeurope"), `environment` (string, default "dev").

**`main.tf`**
Two blocks: a `terraform {}` block pinning `azurerm ~> 3.110` and requiring Terraform `>= 1.7`, and an `azurerm_resource_group` resource named `main` using the variables for its name and location, with three tags.

**`keyvault.tf`**
Three resources:
1. `azurerm_key_vault` named `main` — use the documentation to find the required arguments. Key settings: `soft_delete_retention_days = 7`, `purge_protection_enabled = false`, a `network_acls` block with `default_action = "Allow"` and `bypass = "AzureServices"`.
2. `azurerm_key_vault_access_policy` named `terraform_deployer` — grants the current deployer (from `data.azurerm_client_config.current`) permission to Get, List, Set, Delete, and Purge secrets.
3. `azurerm_key_vault_secret` named `db_connection` — stores one demo secret. `depends_on` the access policy.

Also add: `data "azurerm_client_config" "current" {}` — needed for `tenant_id` and `object_id`.

**`monitoring.tf`**
Two resources:
1. `azurerm_log_analytics_workspace` named `main` — SKU `PerGB2018`, retention 30 days.
2. `azurerm_sentinel_log_analytics_workspace_onboarding` named `main` — takes the workspace ID from the first resource.

**`registry.tf`**
One resource: `azurerm_container_registry` named `main` — SKU `Basic`, `admin_enabled = false`. Note: ACR names cannot have hyphens.

**`outputs.tf`**
Five outputs: `resource_group_name`, `key_vault_url` (attribute: `vault_uri`), `key_vault_name`, `log_analytics_workspace_id` (attribute: `workspace_id`), `container_registry_login_server` (attribute: `login_server`).

---

Go file by file. Use the documentation at registry.terraform.io when you are unsure of an argument name. Come back after each file and I will check it and explain anything unexpected.

---

## QUICK REFERENCE CARD

```
BLOCK TYPES
  terraform {}           → Terraform settings, providers, backend
  provider "name" {}     → Provider config (features, credentials)
  resource "type" "id"   → Creates Azure resources
  data "type" "id"       → Reads existing Azure resources
  variable "name"        → Input parameter (use as var.name)
  locals {}              → Computed internal values (use as local.name)
  output "name"          → Values printed after apply

REFERENCES
  azurerm_key_vault.main.vault_uri     → resource attribute
  var.project_name                      → variable
  local.resource_prefix                 → local value
  data.azurerm_client_config.current.tenant_id  → data source

WORKFLOW
  terraform init      → download providers (once)
  terraform validate  → check syntax (always)
  terraform fmt       → format code (before commit)
  terraform plan      → preview changes (always before apply)
  terraform apply     → make changes
  terraform destroy   → delete everything

VERSION CONSTRAINTS
  = 3.110.0    → exactly this version
  ~> 3.110     → 3.110.x only (patch updates ok)
  >= 3.0       → any version 3.0 or higher (avoid)

AUTHENTICATION TO AZURE
  Local dev      → az login (Azure CLI)
  CI/CD basic    → ARM_CLIENT_ID / ARM_CLIENT_SECRET env vars
  CI/CD secure   → OIDC Workload Identity Federation (no secrets)
```
