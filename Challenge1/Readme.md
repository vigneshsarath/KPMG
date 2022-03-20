# Challenge1

A 3 tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.

**Note:** This is basic Three tier infrastructure provisioning script with minimal resources and creates a external loadbalancer url as output which loadbalances and displays the change between the two web servers. There can be lot of improvements made to ensure we have a highly available and secure environment, but just to keep it simple have scripted a basic three tier setup in this challenge.

## Prerequisites:

1. Install Terraform
2. Install AWS CLI
3. Configure the Access and Secret keys to connect with your AWS account using aws configure command.

### Execution steps:

1. Create a folder and place all the terraform files available in this directory.
2. Execute the commands to provision the three tier infrastructure on AWS.

```
terraform init .    #Initializes a working directory containing Terraform configuration files.
terraform fmt .     #Ensures the formatting is correct 
terraform validate  #Ensures there are no syntax errors.
terraform plan      #Displays what resources will be created
terraform apply     #Creates the three tier Infrastructure, ensure to type Yes when prompted.

Finally if you want to delete the complete setup run the below command.
terraform destroy . #Destroys the complete infrasturcture created.
```
