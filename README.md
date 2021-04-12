# Password generator

A web application that creates randoms passwords and generates a strength test based on the password created.

Author: Raihan Ahmed

## Requirements

- Kanban Board: Trello Board
- Version Control System - Git
- Functional Web-app made with flask including a front-end and testing
- Cloud intergration - GCP MYSQL Database and VM's
- CI Server - Jenkins
- Containerisation - Docker
- Orchestration Tool - Docker Swarm
- Configuration Management - Ansible
- Reverse Proxy - NGINX
- Documentation

## Application Overview

### Application Architecture

![Screenshot_137](https://user-images.githubusercontent.com/35694370/114310163-c64a2880-9ae1-11eb-9efa-ee9eada307ea.png)

### Microservice

Service 1 : This service calls service 4 to retrieve a password from service 4, and then sends the password back to get password strength and then stores it in a GCP MYSQL database. It then runs a query on the db to get the 10 most recent passwords generated so the user can pick one.

Service 2 : This service creates random text which could randomly vary in length.

Service 3 : This service creates a random string of numbers on a fixed length.

Service 4 : This service calls both service 2 & 3 and retrieves text and numbers. It then joins together the text and numbers and returns a password. It also retrieves a password from service 1 which is the most recently generated password, and then checks the length off the password to determine if the password is either strong or weak.

###

![Screenshot_145](https://user-images.githubusercontent.com/35694370/114385211-a1a88c00-9b87-11eb-9dad-0849dfee0e85.png)

## Jenkins Pipeline

![Screenshot_140](https://user-images.githubusercontent.com/35694370/114309787-59825e80-9ae0-11eb-9ea5-ab4aea653cf2.png)

## Trello Board

![Screenshot_138](https://user-images.githubusercontent.com/35694370/114309883-ae25d980-9ae0-11eb-9bbf-61b18bfecb5e.png)

For an updated trello board please click [here](https://trello.com/b/kGSYZVr3/microservice)

## Testing

96% Coverage has been achieved on service 1

![Screenshot_123](https://user-images.githubusercontent.com/35694370/114309963-fba24680-9ae0-11eb-9275-4d7141952709.png)

90% Coverage has been achieved on service 2

![Screenshot_118](https://user-images.githubusercontent.com/35694370/114309977-03fa8180-9ae1-11eb-8640-e247732624e9.png)

89% Coverage has been achieved on service 3

![Screenshot_119](https://user-images.githubusercontent.com/35694370/114309993-0b218f80-9ae1-11eb-8e1d-d435d77637db.png)

94% Coverage has been achieved on service 4

![Screenshot_121](https://user-images.githubusercontent.com/35694370/114310007-14126100-9ae1-11eb-9175-124872c56d1d.png)

## Webhook

![Screenshot_141](https://user-images.githubusercontent.com/35694370/114309734-1e802b00-9ae0-11eb-9952-b574299f3093.png)

## Risk Assessment

![Screenshot_142](https://user-images.githubusercontent.com/35694370/114309851-93536500-9ae0-11eb-8b5d-67fea95bc172.png)

### Improvements

- Make website more user friendly, implement a eye-catching UI

- Passwords could be more complex, include special characters to further improve password strength

- Make changes to Micro service arachitecture so all services talk to service1 independently

#### References

https://qa-community.co.uk

https://www.youtube.com/watch?v=7KCS70sCoK0

https://www.youtube.com/watch?v=dU5112nqViY

https://www.youtube.com/watch?v=1id6ERvfozo

https://docs.ansible.com/ansible/latest/collections/community/docker/docker_swarm_module.html#ansible-collections-community-docker-docker-swarm-module

https://github.com/raihan1995/project_car
