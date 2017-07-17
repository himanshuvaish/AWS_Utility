# Add rules to existing security_groups inside a VPC
With this code it is possible scan all the security_group in that vpc and adds the rules specified

You can specify the vpc id in this variable  

``` 
  myvpc='vpc-xxxxx'
```

in the code is clearly showed how to build the rule

## Boto3 documentation used

[Boto3 security group changes](http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#securitygroup)

[Boto3 describe security groups](https://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.describe_security_groups)

## Running 
This code is lamba ready , you need only to define a lambda role with the loggining permissions

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    }
  ]
}
```

and an AmazonEC2FullAccess policy or you can create a more restrict policy to describe security group and add rules in it
