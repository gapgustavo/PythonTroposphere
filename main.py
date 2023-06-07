from troposphere import Ref, Template
from troposphere.ec2 import Instance, SecurityGroup, SecurityGroupRule, Tag

template = Template()

# Creating an Amazon EC2 instance
for i in range(3):
    instance = Instance(
        "EC2Instance{}".format(i + 1),
        ImageId="ami-12345678",  # Replace with the desired Image ID
        InstanceType="t2.micro",  # Replace with the desired Instance Type
        SecurityGroups=["default"],  # Replace with the desired Security Group
        Tags=[
            Tag("Name", "Instance{}".format(i + 1))
        ]
    )

    template.add_resource(instance)

# Creating a Security Group
security_group = SecurityGroup(
    "EC2SecurityGroup",
    GroupDescription="Allow SSH traffic",
    SecurityGroupIngress=[
        SecurityGroupRule(
            IpProtocol="tcp",
            FromPort="22",
            ToPort="22",
            CidrIp="0.0.0.0/0"
        )
    ]
)

template.add_resource(security_group)

# Exporting the stack to a YAML file
with open("aws_servers.yaml", "w") as file:
    file.write(template.to_yaml())
