# ATS
Automatic Ticket Assignment system API

This api works based on a linear model to classify support tickets into respective Groups 0,1,2


Make sure you have docker engine installed in your environment

## Step 1:

git clone https://github.com/sarvan0506/ATS.git

## Step 2:

sudo docker build -t <image_name>:<tag>

## Step 3:

sudo docker run -d -p <sys_port>:<docker_port> --name <app_name> <image_name>:<tag>


# Access the api via post request:

## request - application/json
http:// <ip>:<port> /
{  
    "description": "there are belgium costumers calling the polish phone number of agnwfwieszka.\ncan we do something on it."  
}  

## response - application/json
{  
  "Group": "2"  
}  