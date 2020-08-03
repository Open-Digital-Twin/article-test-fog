#!/bin/bash

rm -rf log && mkdir log
docker logs 1_mqtt-scylla_db_1 > log/scylla.log
docker logs 1_mqtt-broker_1 > log/broker.log
docker logs 1_mqtt-client_1 > log/client.log
docker logs 1_mqtt-twin_1 > log/twin.log
