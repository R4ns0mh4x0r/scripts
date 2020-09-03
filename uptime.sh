#!/bin/bash

time=$(uptime | awk '{print $1}')

echo "My Uptime: $time"

exit


