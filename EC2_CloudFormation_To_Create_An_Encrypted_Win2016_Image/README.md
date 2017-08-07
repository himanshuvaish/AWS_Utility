# Why you need that
You need to have a Windows AMI with encrypted features

# Rebuild an image in an Encrypted way
For Windows original images you can't perform a direct copy ami with encryption features, but you need to:

* create a machine with an not encrypted version
* run the encryption command to obtain a new ami

What do you need if you want to do this in an automatic way?

## Why you should do in an automatic way?

* you need to deliver to somebody else with low level of knowledge
* you want to keep the encrypted image updated to the latest official image released by AWS

# What this CloudFormation recipe does.

* Create a Role and a profile with associated the the permissions to Create an image
* Create a Winodws machine in the default vpc, in one default subnet and default security group (It is important that the default vpc routing and security group were not changed and they can allow internet access)
* Run the powershell script to create an encrypted version of the EC2 machine itself

## The powershell script
Here the explanation of the completely not interactive powershell

  iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

install the chocolatey package manager from internet

  choco install awscli -y

install the amazon comman line using the package manager installed the step before

  $env:path = "C:\Program Files\Amazon\AWSCLI\;$env:path"

change the environment path variable so it is possible use the awscli without reload the shell

  Add-Content diskparam.json "[{`"DeviceName`": `"/dev/sda1`",`"Ebs`" :{`"Encrypted`" : true,`"DeleteOnTermination`": true} } ]"

prepare a json file with the encrypted information

  $env:myid=Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/instance-id

recover the instance id and put in a variable so it can be used in the next command

  aws ec2 create-image --region ${AWS::Region} --reboot --instance-id $env:myid --name mysolution-encrypted --block-device-mappings file://diskparam.json --description Encrypted-image-win2016

run the command to create an encrypted image of the running instance

# Conclusions
Around 5 minutes after the CloudFormation templace creation you can see the new image in the AMIs ==> Owned by Me and you can delete the CloudFormation Stack , in this way the ec2 windows machine created will be erased but the image will persist. 
