terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_ecr_repository" "cloudops_app" {
  name = "cloudops-ticket-analyzer"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Project     = "Jenkins CloudOps DevSecOps Pipeline"
    Environment = "Dev"
    ManagedBy   = "Terraform"
  }
}
