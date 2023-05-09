import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_wafv2_basic_auth.cdk_wafv2_basic_auth_stack import CdkWafv2BasicAuthStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_wafv2_basic_auth/cdk_wafv2_basic_auth_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkWafv2BasicAuthStack(app, "cdk-wafv2-basic-auth")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
