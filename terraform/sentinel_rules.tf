resource "azurerm_sentinel_alert_rule_scheduled" "brute_force_detection" {
  name                       = "brute-force-detection"
  log_analytics_workspace_id = azurerm_sentinel_log_analytics_workspace_onboarding.main.workspace_id
  display_name               = "Brute Force Login Detection"
  description                = "Detects more than 5 failed sign-in attempts from the same IP within 1 hour"
  severity                   = "High"
  enabled                    = true

  query = <<-QUERY
    SigninLogs
    | where ResultType != "0"
    | where TimeGenerated > ago(1h)
    | summarize FailedAttempts = count() by UserPrincipalName, IPAddress
    | where FailedAttempts > 5
    | project UserPrincipalName, IPAddress, FailedAttempts
  QUERY

  query_frequency = "PT1H"
  query_period    = "PT1H"

  trigger_operator  = "GreaterThan"
  trigger_threshold = 0
}
resource "azurerm_sentinel_alert_rule_scheduled" "keyvault_access_anomaly" {
  name                       = "keyvault-access-anomaly"
  log_analytics_workspace_id = azurerm_sentinel_log_analytics_workspace_onboarding.main.workspace_id
  display_name               = "Key Vault Access Outside Business Hours"
  description                = "Detects Key Vault secret retrieval outside 07:00-19:00 UTC - potential credential harvesting"
  severity                   = "Medium"
  enabled                    = true

  query = <<-QUERY
    AzureDiagnostics
    | where ResourceType == "VAULTS"
    | where OperationName == "SecretGet"
    | where TimeGenerated > ago(1h)
    | extend HourOfDay = datetime_part("hour", TimeGenerated)
    | where HourOfDay < 7 or HourOfDay > 19
    | project TimeGenerated, Resource, CallerIPAddress, HourOfDay
  QUERY

  query_frequency = "PT1H"
  query_period    = "PT1H"

  trigger_operator  = "GreaterThan"
  trigger_threshold = 0
}
resource "azurerm_sentinel_alert_rule_scheduled" "privilege_escalation_detection" {
  name                       = "privilege-escalation-detection"
  log_analytics_workspace_id = azurerm_sentinel_log_analytics_workspace_onboarding.main.workspace_id
  display_name               = "Privilege Escalation - Role Assignment Detected"
  description                = "Detects when any user is added to a privileged Azure AD role"
  severity                   = "High"
  enabled                    = true

  query = <<-QUERY
    AuditLogs
    | where OperationName == "Add member to role"
    | where Result == "success"
    | where TimeGenerated > ago(1h)
    | extend InitiatedBy = tostring(InitiatedBy.user.userPrincipalName)
    | extend TargetUser  = tostring(TargetResources[0].userPrincipalName)
    | extend RoleName    = tostring(TargetResources[1].displayName)
    | project TimeGenerated, InitiatedBy, TargetUser, RoleName
  QUERY

  query_frequency = "PT1H"
  query_period    = "PT1H"

  trigger_operator  = "GreaterThan"
  trigger_threshold = 0
}
resource "azurerm_sentinel_alert_rule_scheduled" "suspicious_api_volume" {
  name                       = "suspicious-api-volume"
  log_analytics_workspace_id = azurerm_sentinel_log_analytics_workspace_onboarding.main.workspace_id
  display_name               = "Suspicious API Request Volume"
  description                = "Detects more than 100 API requests from a single IP within 5 minutes - potential scanning or DDoS"
  severity                   = "Medium"
  enabled                    = true

  query = <<-QUERY
    AppRequests
    | where TimeGenerated > ago(5m)
    | summarize RequestCount = count() by ClientIP
    | where RequestCount > 100
    | project ClientIP, RequestCount
  QUERY

  query_frequency = "PT5M"
  query_period    = "PT5M"

  trigger_operator  = "GreaterThan"
  trigger_threshold = 0
}
