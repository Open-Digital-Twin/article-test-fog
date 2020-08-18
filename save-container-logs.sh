#!/bin/bash

docker container ls --format {{.Names}} | xargs -I {} sh -c 'docker logs {} -t --details 2>&1 | tee {}.log'
