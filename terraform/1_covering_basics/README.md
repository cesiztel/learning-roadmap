## 1. Covering the basics

To deploy infrastructure with Terraform:

- **Scope** - Identify the infrastructure for your project.
- **Author** - Write the configuration for your infrastructure.
- **Initialize** - Install the plugins Terraform needs to manage the infrastructure.
- **Plan** - Preview the changes Terraform will make to match your configuration.
- **Apply** - Make the planned changes.

Commands used on this tutorial

```
$ terraform init

- Downloads the aws provider
- Creates terraform.lock.hck like package.json lock

$ terraform plan -> to look what is going to be deployed

$ terraform fmt -> formatting the configuration

$ terraform validate -> validate configuration

$ terraform apply -> apply configuration
```
