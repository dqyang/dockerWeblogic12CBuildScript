Sample Docker Scripts for Weblogic Container
--------------------------------------------
--------------------------------------------


Build Docker Image for developer version:
-----------------------------------------
CD to "dockerfiles" directory:
	sh buildRESDockerImage.sh -v 12.2.1.3 -d
	sh builVidaSDockerImage.sh -v 12.2.1.3 -d


Build Docker Image for Generic version:
-----------------------------------------
CD to "dockerfiles" directory:
	sh buildRESDockerImage.sh -v 12.2.1.3 -g
	sh buildVidaDockerImage.sh -v 12.2.1.3 -g


SSH into a Docker Container
------------------------------------------
docker exec -it <container id> /bin/bash


Access Host that hosting docker From inside the Container
------------------------------------------
host.docker.internal
gateway.docker.internal


Sample Scripts to Execute Commands in the Container
------------------------------------------
List Existing Docker Image Locally:
	docker image ls

List Existing Docker Containers:
	docker container ls -a
	docker container ps

Remove existing containers:
	docker rm $(docker ps -aq)

Launch the docker containers:

	docker run -p 7001:7001 -p 9002:9002  -v /d/flSchip150/dockerWeblogic12CBuildScript/dockerfiles/12.2.1.3/domain_properties:/u01/oracle/properties -e ADMINISTRATION_PORT_ENABLED=false -e DOMAIN_NAME=base_domain weblogicres:12.2.1.3-developer

	docker run -p 7001:7001 -p 9002:9002 --name resadmin --hostname resadmin -v /d/flSchip150/dockerWeblogic12CBuildScript/dockerfiles/12.2.1.3/domain_properties:/u01/oracle/properties -v /d/flSchip150/dockerWeblogic12CBuildScript/dockerfiles/12.2.1.3/deployments:/u01/oracle/deploy -v /d/flSchip150/dockerWeblogic12CBuildScript/dockerfiles/12.2.1.3/domain_lib:/u01/oracle/domain_lib/ -e ADMINISTRATION_PORT_ENABLED=false -e DOMAIN_NAME=res_domain weblogicres:12.2.1.3-generic

	Admin Server:
	docker run -p 7001:7001 -p 7002:7002 --name vidaadmin --hostname vidaadmin -v /d/flSchip150/dockerWeblogic12CBuildScript/dockerfiles/12.2.1.3/domain_properties:/u01/oracle/properties -v /d/flSchip150/dockerWeblogic12CBuildScript/dockerfiles/12.2.1.3/deployments:/u01/oracle/deploy -v /d/flSchip150/dockerWeblogic12CBuildScript/dockerfiles/12.2.1.3/domain_lib:/u01/oracle/domain_lib/ -e ADMINISTRATION_PORT_ENABLED=false -e DOMAIN_NAME=service_domain weblogicvida:12.2.1.3-generic




Replicate a Docker Containers into Docker Service:
-------------------------------------------------
----------------------------------------------------
CD to docker-compose directory:

	docker swarm init
	docker stack deploy -c docker-compose.yml vidaservices
	docker service ls
	docker service ps vidaservices_web


Docker Swarm Cleanup:

	docker stack rm vidaservices


Take Down the Swarm:

	docker swarm leave --force
