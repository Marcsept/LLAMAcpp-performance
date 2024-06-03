#!/bin/bash
#==============================================================================
# Script Name: test_input_tremp.sh
# Description: A simple function who try some value of temp option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

temp () {

  #Define variables
  local md=$1
  local option="temp"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model "--temp 0" "temp0"

  try_option $outputs_path $inputs_path $model "--temp 0.5" "temp05"

  try_option $outputs_path $inputs_path $model "--temp 5" "temp5"


  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
