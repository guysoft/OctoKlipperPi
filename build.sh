#!/bin/bash
docker run --rm --privileged -v ${PWD}/src:/CustoPiZer/workspace -v ${PWD}/src/config:/CustoPiZer/config.local ghcr.io/octoprint/custopizer:latest
