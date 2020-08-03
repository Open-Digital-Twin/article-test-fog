#!/bin/bash

cp `docker inspect --format='{{.LogPath}}' messages_scylla-db_1` scylla.log && chmod +rw scylla.log
cp `docker inspect --format='{{.LogPath}}' messages_mqtt-broker_1` broker.log && chmod +rw broker.log
cp `docker inspect --format='{{.LogPath}}' messages_twin_1` twin.log && chmod +rw twin.log
cp `docker inspect --format='{{.LogPath}}' messages_client_1` client.log && chmod +rw client.log

