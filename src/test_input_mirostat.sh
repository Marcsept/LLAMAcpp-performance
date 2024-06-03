#!/bin/bash
#==============================================================================
# Script Name: test_input_mirostat.sh
# Description: A simple function who try some value of mirostat option
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================

#Source
  source src/utils/try_command.sh

mirostat () {

  #Define variables
  local md=$1
  local option="mirostat"
  local outputs_path="outputs/"${md}"_test_input_${option}"
  local inputs_path="inputs"
  local model="models/""${md}"".gguf"

  echo $option
  # Create file if doesn't exist
  mkdir -p "$outputs_path/outputs_res"
  mkdir -p "$outputs_path/outputs_log"



  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.2 --mirostat-ent 2" "mirostat1_br02_ent2"
  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.2 --mirostat-ent 5" "mirostat1_br02_ent5"
  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.2 --mirostat-ent 8" "mirostat1_br02_ent8"
  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.2 --mirostat-ent 15" "mirostat1_br02_ent15"

  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.5 --mirostat-ent 2" "mirostat1_br05_ent2"
  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.5 --mirostat-ent 5" "mirostat1_br05_ent5"
  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.5 --mirostat-ent 8" "mirostat1_br05_ent8"
  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.5 --mirostat-ent 15" "mirostat1_br05_ent15"
 
  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.02 --mirostat-ent 2" "mirostat1_br002_ent2"
  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.02 --mirostat-ent 5" "mirostat1_br002_ent5"
  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.02 --mirostat-ent 8" "mirostat1_br002_ent8"
  try_option $outputs_path $inputs_path $model "--mirostat 1 --mirostat-lr 0.02 --mirostat-ent 15" "mirostat1_br002_ent15"


  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.2 --mirostat-ent 2" "mirostat2_br02_ent2"
  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.2 --mirostat-ent 5" "mirostat2_br02_ent5"
  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.2 --mirostat-ent 8" "mirostat2_br02_ent8"
  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.2 --mirostat-ent 15" "mirostat2_br02_ent15"

  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.5 --mirostat-ent 2" "mirostat2_br05_ent2"
  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.5 --mirostat-ent 5" "mirostat2_br05_ent5"
  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.5 --mirostat-ent 8" "mirostat2_br05_ent8"
  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.5 --mirostat-ent 15" "mirostat2_br05_ent15"
 
  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.02 --mirostat-ent 2" "mirostat2_br002_ent2"
  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.02 --mirostat-ent 5" "mirostat2_br002_ent5"
  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.02 --mirostat-ent 8" "mirostat2_br002_ent8"
  try_option $outputs_path $inputs_path $model "--mirostat 2 --mirostat-lr 0.02 --mirostat-ent 15" "mirostat2_br002_ent15"

  python agregation_data1.py "outputs/${md}_test_input_${option}/outputs_log"


}
