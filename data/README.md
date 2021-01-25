# Deploy a database with data
For this example, we have defined a database schema (See [SPOT -- Database Schema.pdf](SPOT -- Database Schema.pdf)).
We use :
- a [docker-compose.yml](docker-compose.yml) file to deploy a MySQL database 
- and docker volumes to ingest CSV [files](files/) using [scripts](scripts/) 

To link others containers ([api](../api/) and [front](../front/)) with the database container, we use external docker network. If it is not already done, create it:
```terminal
docker network create spot-network
```
Then, you can deploy the database and let it ingest your data:
```terminal
docker-compose up -d
```
