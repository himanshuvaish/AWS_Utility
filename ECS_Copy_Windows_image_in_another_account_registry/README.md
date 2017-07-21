# AWS ECS Windows Copy an Image in another account

# What I need to do

I have an image for Windows inside a registry and I need to copy to another registry in another account.

# Parameters 
| Source Account Where the image is | Destination Account where to copy the image |
| --------------------------------- | ------------------------------------------- |
| 123456789012                      | 111111111111                                |

registry names

| Source Registry | Destination Registry |
| --------------- | -------------------- |
| mysourcerepo    | mydestinationrepo    |

The whole example is in Ohio region us-east-2 adapt to your case
The Windows machine used is created from **Microsoft Windows Server 2016 Base with Containers**

# Step 1 Create the registry in the Destination Account
1. Use the CloudFormation template for the registry creation provided in this example
2. After go in the Amazon ECS and copy the URI , you will need in the next step will be like

    123456789012.dkr.ecr.us-east-2.amazonaws.com/mysourcerepo


# Step 2 From the Windows 2016 server machine you need to pull and push the repo

The machine need to be associated to a role with the following policy

- Managed Policies: AmazonEC2ContainerServiceforEC2Role 
- Inline Policies: this custom one


    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "ecr:InitiateLayerUpload",
                    "ecr:UploadLayerPart",
                    "ecr:PutImage",
                    "ecr:CompleteLayerUpload"
                ],
                "Resource": [
                    "arn:aws:ecr:*:*:repository/*"            ]
            }
        ]
    }


## Install the aws cli

You need to install the aws cli, currently in the image is not installed by default. It is possible doing a cut and past of these 2 commands in a PowerShell 


    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
    choco install awscli -y

if you want to know more about [chocolatey click here](https://chocolatey.org/) but you don't really need

## Lets do the push finally 
- acquire the permissions to operate 


    Invoke-Expression -Command (aws ecr get-login --no-include-email --region us-east-2)


- pull the source docker image that you want to copy


    docker pull 123456789012.dkr.ecr.us-east-2.amazonaws.com/mysourcerepo
- tag the image 


    docker tag 123456789012.dkr.ecr.us-east-2.amazonaws.com/mysourcerepo 111111111111.dkr.ecr.us-east-2.amazonaws.com/mydestinationrepo


- acquire the permission of the destination account and push the image


    PS C:\Users\Administrator> Invoke-Expression -Command (aws ecr get-login --no-include-email --region us-east-2 --registry-ids 111111111111)
    Login Succeeded
    PS C:\Users\Administrator> docker push 111111111111.dkr.ecr.us-east-2.amazonaws.com/mydestinationrepo


# Verification

In the destination account , go to Amazon ECS registry and verify that the Size is upper than 0

