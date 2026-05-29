output "ecr_repository_name" {
  value = aws_ecr_repository.cloudops_app.name
}

output "ecr_repository_url" {
  value = aws_ecr_repository.cloudops_app.repository_url
}
