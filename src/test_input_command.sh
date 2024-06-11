#!/bin/bash
#==============================================================================
# Script Name: test_input_ctv_ctk.sh
# Description: A simple function who try some value of ctv and ctk option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
source src/utils/run_command.sh


  #Define variables
md=$1
option1=$2
option2=$3
outputs_path="outputs/"${md}"_test_input_${option1}"
inputs_path="inputs"
model="models/""${md}"".gguf"

echo $option
# Create file if doesn't exist
mkdir -p "$outputs_path/outputs_res"
mkdir -p "$outputs_path/outputs_log"
mkdir -p "$outputs_path/outputs_state"


try_option $outputs_path $inputs_path $model $option2 $option1

#Todo new aggregation 
 
 
python agregation_data.py "outputs/${md}_test_input_${option}/outputs_log"



