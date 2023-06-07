# AWS Server Provisioning with Troposphere
This Python script utilizes the Troposphere library to create a YAML file that defines the provisioning of three servers in AWS. The resulting YAML file can be used with AWS CloudFormation to create the servers in your AWS account.

## Prerequisites
Python 3.x installed
troposphere library installed (pip install troposphere)

## Usage
Clone or download the script from the repository.

Install the required dependencies by running:
```bash
pip install requirements.txt
```

Open the script file and modify the following parameters according to your requirements:

    ImageId: Replace with the desired Amazon Machine Image (AMI) ID.

    InstanceType: Replace with the desired instance type.

    SecurityGroups: Replace with the desired security group.

Save the changes.

Run the script.
```bash
python main.py
```

The script will generate a file named aws_servers.yaml.

Use the generated aws_servers.yaml file with AWS CloudFormation to create the servers in your AWS account.

## Important Notes
Ensure that you have the necessary permissions and credentials to create AWS resources.
Review and adjust the security group settings to meet your requirements.
Remember to clean up and delete the AWS resources when they are no longer needed to avoid incurring unnecessary costs.

