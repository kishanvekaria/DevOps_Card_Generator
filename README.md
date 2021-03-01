# DevOps_Card_Generator

## Contents
1. Brief
2. Software Design
3. Project Planning
4. Risk Assessment
5. Testing
6. Front End
7. Evaluation
8. Appendix

## 1. Brief
The project is designed to implement the use of multiple pieces of software integrated by the DevOps methodology.

This project is to be made from a minimum of 4 services. Service 2 + 3 are both random generators. Service 4 must combine the two random attributes together. Finally Service 1 must present the data on the Front-end of the application making it viewable through a web app, and also integrate data storage through MySQL.

The requirements of the project is as follows:
* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.

* This could also provide a record of any issues or risks that you faced creating your project.

* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine

* If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application

* The project must follow the Service-oriented architecture that has been asked for.

* The project must be deployed using containerisation and an orchestration tool.

* As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.

* The project must make use of a reverse proxy to make your application accessible to the user.

_The other constraint in this project is the technologies that need to be used.
The project needs to utilise the technologies discussed during the training modules:_

* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX


## 2. Software Design

Before writing any code it was important to establish an idea for the project. Due to the nature of the project I had to think of something that would need two randomly generated outputs. I decided to create an app that could randomly generate a card from a deck of cards.
 
### Service Architecture 

As mentioned earlier in the requirements. The app would need a minimum of 4 services. For my project I needed one random generator deciding the face of the card (Service 2) and the other random generator deciding the suit of the card (Service 3). Service 4 would then combine the two outputs and send them to the front-end Service 1. Which would store the data in MySQL and then present it to the user. 

Here's a diagram I made to display the architecture:

![service_arch](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603ce8862205c285f569eb6c/06c94468c3a0fd389969d8d548f03ade/servicearch.jpg)


### CI Pipeline

Below is a CI (Continuous Integration) pipeline diagram showing all the different software packages I used and how they relate in relation to one another

![CI Pipeline](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603ce9bf9cf009775f96b512/818bcb6015f72c8aa4ef5252863cc92b/cipipeline.jpg)

As you can see I used **GitHub** as a version control system. Trello (Kanban Board) to manage my project planning. **Visual Studio** IDE to write my code in **Python**. Pytest to test my coverage. **Jenkins** allows for automation to take place in that it has a web hook to my GitHub repository and has a script to test the code before building images and pushing them to **DockerHub**. Jenkins then using **Ansible** for configuration management then deploys the services. The services pass through a reverse proxy using 
All the Virtual machine instances are being held on **Google Cloud Platform, GCP**. The shell being run on GCP is a **Linux/Unix** language through **Ubuntu 18.0**.

### Virtual Machine Architecture

#### Initial VM design
When I first started the project I planned having an architecture limited to three virtual machines. 
Services would be running through docker containers and replicas created to run over both the swarm manager and worker. 
Nginx would also be running through a docker container and working as a reverse proxy, meaning the front end user would only have access to the displayed output and not the backend workings of the services. 
I also planned on having mySQL running through a docker container within the swarm instances.

Here is the initial design layout
![firstVMlayout](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603cf0a93538cc327fd56308/11f0ff9b86bff91ff5e5353e8fed992c/firstvmdesign.jpg)

#### Final VM design
However as time passed I released it would be better to have Nginx running as a load balancer for the two swarm machines and hence I decided to create a separate Virtual Machine instance for it. 
This means it would be able to manage incoming traffic between the two machines and hence lower the chance of machines crashing due to an increase in the amount of users accessing the Card Generator. 
I also decided it would be better to create a specialised MySQL database instance on GCP as this would mean the database would be running all the time and not need to be deployed like the services
![finalVMlayout](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603cf0a93538cc327fd56308/dba0af8b3aa5d9e5e4a6e14ed252390f/finalvmdesign.jpg)

## 3. Project Planning
I used Trello to manage my planning for the project. It contains a very simple user interface which allows for Todo, Doing and Done coloumns.
This style of planning is taken from the japanese method of Kanban. I could also use it to store my planning diagrams. 

To see the actual Trello Board:

[Link to Trello Board](https://trello.com/b/uLHNhHsV/qa-week-9-project)

This is my final Trello board:
![Trello](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603ced05ba9754549dd927cb/2a3af3c0facd644dffb1b9224ecf0bea/trelloboard.JPG)


## 4. Risk Assessment
This is the risk assessment I have conducted for the project
![Risk Assessment](https://trello-attachments.s3.amazonaws.com/6006b837abee6877e9b3597f/6020355e91dfc2794a87e432/197c575103b08e6b80da596bf160311a/Risk_Assessment.JPG)

## 5. Testing

####Pytest
Once again, we only had time to conduct unit testing for the project and not the integration testing as this had not been taught before the deadline for the project.
I used **Pytest** to conduct the tests for my project. I'm glad we were taught the type of testing to test random functionality as this is what was causing testing to fail on my previous project.
So I'm glad to have the answer to this now. To test random output data I used a python flask import called unittest.mock and module called patch.
This meant I could substitute a random output, to that of my choosing, to get a response was coming through on the HTML  

Here are screenshots of my test coverage reports for each of my 4 services:
##### Service 1
![Test](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603cfcbb3aed0532159d0c0e/d0ae146b4391b7e79af8fdd756f88812/app1test.JPG)
##### Service 2
![Test2](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603cfcbb3aed0532159d0c0e/080a555b3622c18063b0a804b86d9931/app2test.JPG)
##### Service 3
![Test3](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603cfcbb3aed0532159d0c0e/70b48aa465b276d282de2f31474cbd96/app3test.JPG)
##### Service 4
![Test4](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603cfcbb3aed0532159d0c0e/8eaeb681ca403c0a7ddc48fc5d1eeceb/app4test.JPG)

Total coverage on each service:
* Service 1: 96%
* Service 2: 91%
* Service 3: 91%
* Service 4: 92%

####Front-end testing
Whilst creating my services I was testing the outputs from each service on the front end to ensure each service was delivering out what it required. 

![frontendtest](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603cff2b5e21ca792b2c50c8/bb674edccf969a707f53900aa4d1be48/testing_service_data_appears_on_the_app.JPG)

## 6. Front End
The aim of this project was to create good backend infrastructure and use DevOps skills to automate services. So the front-end ofthe project basic. but as stated before, functionality was the main purpose of the project.

Here are screenshots of my app when running:

![frontend1](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603cff96d30dc34f01237750/1fd35f5296ed347fb89fa447373da363/frontend1.JPG)

![frontend2](https://trello-attachments.s3.amazonaws.com/603cd4dc733be54ef8b4952d/603cff96d30dc34f01237750/4f20c7aaafe9968b83b39f4ae0a48bb5/frontend2.JPG)



## 7. Evaluation   
   Overall I think the project was successful. 
   I managed to have Jenkins automate the entire process of testing, building, configuration management and deploying the services. 
   Jenkins was also able to build the pipeline job automatically because I had used a web-hook detecting any changes in the main branch of my Git repository.
   
   If I could do it again and had more time I would love to get the services to output a number of cards to players around a table. The backend infrastructure all went to plan though so I am more than pleased with the result. 
   
## 8. Appendix  

Author: Kishan Vekaria

All the content in this repository has been created by me and is being stored on Github. Hence it's open source. If you have any questions or contribrutions you would like to make please contact me and I would be happy to hear from you!
