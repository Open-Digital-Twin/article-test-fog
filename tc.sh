#!/bin/bash

tc qdisc add dev ens3 root netem delay 50ms 10ms distribution normal
