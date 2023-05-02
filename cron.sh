#!/bin/bash

while true; do
  wget "http://localhost:3000/instance/?id=1&engine=linear_function"
  sleep 60
done
