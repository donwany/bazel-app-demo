#!/bin/bash

docker build -t container2 .

docker run -p 1958:1958 container2
