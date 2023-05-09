#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_wafv2_basic_auth.cdk_wafv2_basic_auth_stack import CdkWafv2BasicAuthStack


app = cdk.App()
CdkWafv2BasicAuthStack(
    app, "CdkWafv2BasicAuthStack",
    # ScopeをCloudFrontとするため、us-east-1にリソースを作成する
    env=cdk.Environment(region='us-east-1')
)

app.synth()
