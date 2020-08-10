#!/bin/bash

docker service logs messages_twin -t --details 2>&1 | tee twin.log &&
docker service logs messages_scylla-db -t --details 2>&1 | tee scylla-db.log &&
docker service logs messages_mqtt-broker -t --details 2>&1 | tee mqtt-broker.log

cp ../docker-compose.yml .
cp ../mosquitto.conf .

docker service logs messages_client -t --details 2>&1 | tee client.log


