#!/usr/bin/env python3

import aws_cdk as cdk

from aws_stepfunction_cdk.aws_stepfunction_cdk_stack import AwsStepfunctionCdkStack


app = cdk.App()
AwsStepfunctionCdkStack(app, "aws-stepfunction-cdk")

app.synth()
