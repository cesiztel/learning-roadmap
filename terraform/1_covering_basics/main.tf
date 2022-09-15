terraform {
  cloud {
    organization = "cesar-izquierdo"
    workspaces {
      name = "development"
    }
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.8.0"
    }
  }
}

provider "aws" {
  region = "eu-west-2"
}

locals {
  project_name = "Andrew"
}

resource "aws_instance" "my_server" {
  ami           = "ami-087c17d1fe0178315" // terraform won't validate the ami id
  instance_type = var.instance_type

  tags = {
    Name = "MyServer-${local.project_name}"
  }
}