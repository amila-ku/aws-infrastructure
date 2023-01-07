import os
from aws_cdk import (
    cdk,
    aws_route53 as route53,
    aws_route53_targets as route53_targets,
)

class MyStack(cdk.Stack):
    def __init__(self, app: cdk.App, id: str) -> None:
        super().__init__(app, id)

        # Create an Amazon Route 53 hosted zone
        hosted_zone = route53.HostedZone(self, 'MyHostedZone',
            zone_name='cloudnativestories.dev',
            comment='Hosted zone for all cloudnativestories.dev',
        )

        # Add a CNAME record to the hosted zone
        route53.CnameRecord(self, 'Handle WWW',
            record_name='www.cloudnativestories.dev',
            domain_name='cloudnativestories.dev',
            zone=hosted_zone,
        )

app = cdk.App()
MyStack(app, "MyStack")
app.synth()

