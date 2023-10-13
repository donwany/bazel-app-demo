#!/bin/bash

docker build -t container1 .

docker run -p 1957:1957 container1
