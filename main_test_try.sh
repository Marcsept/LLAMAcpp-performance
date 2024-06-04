#!/bin/bash
#==============================================================================
# Script Name: main_test_try.sh
# Description: Run all try of command
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================



source src/test_input_try.sh
model=$1
param=$2
option=$3

echo start
#echo "try $model $param $option"
try $model "$param" "$option"

