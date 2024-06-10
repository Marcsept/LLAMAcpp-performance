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

command () {

  #Define variables
  local md=$1
  local option1=$2
  local option2=$3
  local outputs_path="outputs/"${md}"_test_input_${option1}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"
  mkdir -p "$outputs_path/outputs_state"


  command $outputs_path $inputs_path $model $option2 $option1

 #Todo new aggregation 
 
 
  python agregation_data.py "outputs/${md}_test_input_${option}/outputs_log"


}
