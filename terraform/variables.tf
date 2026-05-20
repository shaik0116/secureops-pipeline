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
  description = "deploy environment:dev, staging or prod"
  type        = string
  default     = "dev"

}