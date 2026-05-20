output "resource_group_name" {
  description = "Name of the resource group containing all resources"
  value       = azurerm_resource_group.main.name
}

output "key_vault_url" {
  description = "Key Vault URI — set as AZURE_KEY_VAULT_URL in the application"
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
  description = "ACR login server — used in docker push commands"
  value       = azurerm_container_registry.main.login_server
}
