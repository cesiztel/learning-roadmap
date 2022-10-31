#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_first_project.cdk_first_project_stack import CdkFirstProjectStack


app = cdk.App()
CdkFirstProjectStack(app, "cdk-first-project")

app.synth()
