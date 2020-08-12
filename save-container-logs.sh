#!/bin/bash

docker container ls --format {{.Names}} | xargs -I {} docker logs {} -t --details 2>&1 | tee {}.log
