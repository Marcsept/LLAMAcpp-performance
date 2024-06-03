#!/bin/bash
#==============================================================================
# Script Name: test_input_grp_att.sh
# Description: A simple function who try some value of grp att option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

grp_att () {

  #Define variables
  local md=$1
  local option="grp_att"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model "-gan 2" "grp_att_n"
  
  try_option $outputs_path $inputs_path $model "-gaw 256" "grp_att_w"
  
  try_option $outputs_path $inputs_path $model "-gan 2 -gaw 256" "grp_att_w_n"


  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
