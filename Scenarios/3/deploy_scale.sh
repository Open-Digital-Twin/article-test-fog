# Reset Twin, client and broker.
docker service scale messages_twin=0 messages_client=0 messages_mqtt-broker=0 &&
docker service scale messages_mqtt-broker=1 &&
docker service scale messages_twin=1

# Test with one client
docker service scale messages_client=1

# with three clients
docker service scale messages_client=3

# with five clients
docker service scale messages_client=5
