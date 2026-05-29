# Jenkins CloudOps DevSecOps Pipeline

This project demonstrates a Jenkins-based DevSecOps CI/CD pipeline for a containerized CloudOps Ticket Analyzer API.

## Project Overview

The application is a lightweight FastAPI service that analyzes CloudOps support tickets and assigns a risk score based on severity and keywords such as outage, breach, failed, unauthorized, and latency.

The Jenkins pipeline automates testing, Terraform validation, Infrastructure-as-Code scanning, Docker image builds, and container vulnerability scanning.

## Skills Demonstrated

- Jenkins CI/CD
- Jenkins Pipeline-as-Code
- Python FastAPI development
- Unit testing with Pytest
- Docker image builds
- Terraform validation
- Infrastructure-as-Code with Terraform
- Checkov IaC security scanning
- Trivy container vulnerability scanning
- DevSecOps security gates
- GitHub source control

## Pipeline Stages

1. Checkout source code from GitHub
2. Install Python dependencies
3. Run unit tests
4. Validate Terraform configuration
5. Scan Terraform code with Checkov
6. Build Docker image
7. Scan Docker image with Trivy
8. Prepare for deployment approval

## Why This Project Matters

This project mirrors real-world DevSecOps workflows where application code, infrastructure code, container security, and CI/CD automation are validated before deployment.

It demonstrates how Jenkins can be used to enforce quality checks and security scanning early in the software delivery lifecycle.
