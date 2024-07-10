# Test benchmark LLAMA

By : Valère BILLAUD

## How use it ? 

You can use https://colab.research.google.com/drive/1rvhvTqh2Q2OsafJcRP8HZmN86FoVUYTU?usp=sharing 

- NAME_MODEL : "gpt2", "llama2" and "mistral7B", you can add model in ``models file``

## List of tests 

- only : without more options that potions use to create a similaire environement of run for every test, (the model, the prompt file, the seed and a number of generated tokens)


- ctv ctk : KV cache data type for V and K
    - Default : f16

- grp_att : Groupe attentionfactor and width
    - Values to test : factor 2, witdh 256 and (factor 2 + witdh 256)
    - Default : factor 1, witdh 512

- keep : number of tokens to keep from the initial prompt 
    - Values to test : 0, 20, all
    - Default : 0 

- min-p : min-p sampling 
    - Values to test : 0 and 0.3
    - Default : 0.1 

- mirostat : mirostat sampling with the learning rate and entrhopy (mirostat, mirostat-lr, mirostat-ent)
    - Values to test : (1, 0.2, 5), (1, 0.02, 8),  (2, 0.5, 2), (2, 0.02, 8)
    - Default : (0 (disabeal), 0.1, 5.0)

- nkvo : disable KV offload 

- Repeat last n : last n tokens to consider for penalize
    - Values to test : 0, 32, 128, -1 (All)
    - Default : 64 (0 disabled)

- Repeat penalty : penalize repeat sequence of tokens
    - Values to test : 1, 1.5
    - Default : 1 disabled

- Split : (np : number of parallele sequence, ns : number sequence to decode, sp : speculative decoding split probability)
    - Values to tests : (0.1, 2, 1), (0.9, 10, 1), (0.1, 2, 0.2), (0.9, 10, 0.2)
    - Default : (1, 1, 0.1)

- Temp : temperature 
    - Values to tets : 0, 0.5, 5
    - Default : 0.8

- Tfs : tail free sampling, parameter z 
    - Values to tests :  0.95
    - Default : 1 (disabled)

- Threads : Number of threads to use during generation
    - Values to tests : 1, 2
    - Default : 4

- Top-k : top-k sampling
    - Values to tests : 5, 100
    - Default : 40 (0 disabled)

- Top-p : top-p sambling
    - Values to tests : 0.5, 0.99
    - Default : 0.9 (1 disabled)

- Typical : locally typical sampling, parameter p
    - Values to tests : 0, 0.9 
    - Default : 1 (disabled)

## Input / output  

You can add inputs in the file ``inputs``. 
You can add option in the file ``inputs/option`` 

For all tests a file wase create in outputs to stock the result and the log of the test. At the end a python script retrieve date from log and merge it in a csv per option in file aggregation.

After each run, we save information to understand how the neural network performed during inference. 



