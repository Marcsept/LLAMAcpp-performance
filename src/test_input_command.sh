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
outputs_path="outputs/"${md}"_test_input_${option2}"
inputs_path="inputs"
model="models/""${md}"".gguf"

echo $option
# Create file if doesn't exist
mkdir -p "$outputs_path/outputs_res"
mkdir -p "$outputs_path/outputs_log"
mkdir -p "aggregations/NeuralNetwork/${md}/${option2}"


try_option "$outputs_path" "$inputs_path" "$model" "$option1" "$option2" "aggregations/NeuralNetwork/${md}/${option2}"

#Todo new aggregation 
 

python agregation_data.py "outputs/${md}_test_input_${option2}/outputs_log"

