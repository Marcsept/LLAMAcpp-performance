#!/bin/bash
#==============================================================================
# Script Name: main_test.sh
# Description: run all test
# Author: Valère BILLAUD
# Pseudonyme: Marcsept
# Created: 2024-05-31 
#==============================================================================


source src/test_input_ctv_ctk.sh
source src/test_input_grp_att.sh
source src/test_input_keep.sh
source src/test_input_min-p.sh
source src/test_input_mirostat.sh
source src/test_input_nkvo.sh
source src/test_input_only.sh
source src/test_input_repeat_last_n.sh
source src/test_input_repeat_penalty.sh
source src/test_input_split.sh
source src/test_input_temp.sh
source src/test_input_tfs.sh
source src/test_input_threads.sh
source src/test_input_top-k.sh
source src/test_input_top-p.sh
source src/test_input_typical.sh

source src/utils/load_bar.sh
model=$1
total_steps=16
echo $model


update_loading_bar $total_steps 0
ctv_ctk $model

update_loading_bar $total_steps 1
grp_att $model

update_loading_bar $total_steps 2
keep $model

update_loading_bar $total_steps 3
min-p $model

update_loading_bar $total_steps 4
mirostat $model

update_loading_bar $total_steps 5
nkvo $model

update_loading_bar $total_steps 6
only $model

update_loading_bar $total_steps 7
repeat_last_n $model

update_loading_bar $total_steps 8
repeat_penalty $model

update_loading_bar $total_steps 9
split $model

update_loading_bar $total_steps 10
temp $model

update_loading_bar $total_steps 11
tfs $model

update_loading_bar $total_steps 12
threads $model

update_loading_bar $total_steps 13
top-k $model

update_loading_bar $total_steps 14
top-p $model

update_loading_bar $total_steps 15
typical $model
update_loading_bar $total_steps 16
echo 

echo -ne Start aggregation\r
python agregation_global.py $model
echo -ne 