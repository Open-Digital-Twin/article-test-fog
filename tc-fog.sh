#!/bin/bash

tc qdisc add dev ens3 root netem delay 20ms 5ms distribution normal
