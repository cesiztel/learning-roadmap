## Glossary of term

- **_Provisioning_**: To prepare a server with systems, data and software, and make it ready for network operation. When you launch a cloud service and configure it you are `provisioning`.
- **_Deployment_**: Is the act of delivering a version of your application to run a provisioned server.
- **_Orchestration_**: Is the act of coordianting multiple systems or services.
- **_Configuration Drift_**: Is when provisioned infrastructure has a unexpected configuration by team member changes, malicious actors, changes on API's.
- **_Mutable vs Immutable Infrastucture_**:
  - **_Mutable_**: A VM is deployed and then a Configuration Management tool like Ansible, etc is used to configure the state of the server
  - **_Immutable_**: A VM is launched and provisioned, and then and it is turned into a Virtual Image, store in image repository that image is used to deployed VM instances.
- **_GitOps_**: Is when you table IaC and you use a git repository to introduce a formal process to review and accept changes to infrastructure code.

## Learn about IaC

Most important features on working on the cloud environment:

- API driven.
- Much elasticity of resources and much more scale (much more services to provision).
- Provision tends to be cyclic. Scale up-down, horizontal-vertical. Taking advantage of the pricing as you go.

Infrastructure as Code (IaC):

- Make changes idempotent (run the same routing multiple time must output the same result), consistent, repeatable and predictable
- Automatization (codification) of the operational infrastructure actions (creating, updating or destroying)
- Versioning
- Transparency of the history of actions

Terraform running:

- Will examine the state of the currently running infrastructure.
- Determine what differences exist between the current state and the revised desired state, and indicate the necessary changes that must be applied.
- When approved to proceed, only the necessary changes will be applied, leaving existing, valid infrastructured untouched.

## Infrastructure Lifecycle

A number of clearly defined and distinct work phases which are used to _plan, design, buid, test, deliver, maintain and retire_ cloud infrastructure.
This is possible for the characteristics of IaC:

- Reliability: idempotent, consistent, repeatable and predictable
- Manageability:
  - enable mutation via code
  - revised, with minimal changes
- Sensibility: avoid financial and reputational losses to even loss of life when cosidering government and military dependencies on infrastructure

## What is Terraform?

Is an open source and cloud-agnostic IaC tool. Terraform uses declarative configuration files. That configuration files are written in HCL
(HashiCorp Configuration Language).

## Terraform Lifecycle

To deploy infrastructure with Terraform:

- **Scope** - Identify the infrastructure for your project.
- **Author** - Write the configuration for your infrastructure.
- **Initialize** - Install the plugins Terraform needs to manage the infrastructure.
- **Plan** - Preview the changes Terraform will make to match your configuration.
- **Validate** - Ensure types and values are balid. Ensures required attributes are present.
- **Apply** - Make the planned changes.

Code > Init > Plan > Validate > Apply > Code or Destroy

## Terraform Change Management

- **Change Management**: Is the procedure that will be followed when resources are modidy and applied via configuration script.
- **Change Automation**: a way of automatically creating a consistent, systematic, and predictable way of managing change request via controls and policies.
- **Change Set**: collection of commits that represent changes made to a versioning repo.

In Terraform the Change automation is in the form of `Execution Plans` and `Resource graphs` to apply and review complex changesets. Allow you to know
exactly what Terraform will change and in what order.

## Excution plans

You can visualize an execution plan on after `terraform apply` or via `terraform graph` using a visualizator like GraphViz

```
terraform graph | dot -Tsvg > graph.svg
```

Terraform build a `dependency graph` from the Terraform configurations, and walks this graph to generate plans, refresh stage, and more. Elements of the graph:

- **Resource Node**: single resource
- **Resource Meta-Node**: group of resources (no actions at it's own)
- **Provider Configuration Node**: Represents the time to fully configure a provider

## Terraform Core and Plugins

Terraform Core (code) communicates with plugins via RPC. Plugins are compose by providers and provisioners and they expose an implementation
for a specific service, or provider

![Terraform core and plugins](/docs/images/1.png)

## Terraform Providers vs Modules

- Provider: is a plugin that is a mapping to a Cloud Service Provider (CSPs) API
  To list all the providers on your project:

```
terraform providers
```

- Module: A module is a group of configuration files that provide common configuration functionality. Enforces best practices, reduces
  the amount of code and reduce time to develop scripts.

## Extra resources

[Terraform best practices](https://www.terraform-best-practices.com/)
