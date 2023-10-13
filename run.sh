#!/bin/bash

nohup bazel run main:hello -- \
  -n='elbowai' \
  --age=45 \
  --job='running' \
  --num_a=45 \
  --num_b=99 &