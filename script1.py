"""SPECULATIVE DECODING"""


"""
THE Script compares:
    1. Normal Greedy decoding
    2. Speculative Decoding

Goal:
    1. Show how speculative decoding works
    2. Compare speed and outputs
"""

#Step 1: Import libraries
#step 2: Load Models
#Step 3: Encode input prompt
#Step 4: Normal Decoding
#Step 5: Speculative Decoding
#Step 6: Compare results




# Step 1. Import Libraries
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


# Step 2. load Models

draft_model_name = "gpt2" #smaller model for Drafting
draft_model = AutoModelForCausalLM.from_pretrained(draft_model_name)

#Target Model for Final Decoding
target_model_name = "gpt2-medium" #larger model for Final Decoding
target_model = AutoModelForCausalLM.from_pretrained(target_model_name)

# Shared Tokenizer
tokenizer = AutoTokenizer.from_pretrained(draft_model_name) #gpt2 and gpt2-medium share the same tokenizer


# Step 3. Encode Input Prompt
prompt = "In a shocking finding, scientists discovered a herd of unicorns living in a remote, " 
inputs = tokenizer(prompt, return_tensors="pt")


# Step 4. Nromal Decoding
print("Normal Greedy Decoding")
start = time.time()
normal_ouptuts = target_model.generate(
    **inputs,
    max_new_tokens=50, #number of tokens to be generated
    do_sample=False, #Greedy Decoding
    num_return_sequences=1 # will only generate one sequence
)
end = time.time()

normal_text = tokenizer.decode(normal_ouptuts[0], skip_special_tokens=True) #decoding the output tokens to text
print(f"Output Text: {normal_text}")
print("Time taken:(Normal)",round(end-start, 3), "seconds")

# Step 5. Speculative Decoding ( draft + target )
"""
Internally, Hugging Face does:
    1. Run draft model → propose k tokens.
    2. Run target model once → get probabilities for those k tokens.
    3. Run accept/reject test for each.
    4. If rejected → resample from target.
    5. Continue until output length is reached.
"""
print("\nSpeculative Decoding")
start = time.time()
spec_outputs = target_model.generate(
    **inputs,
    max_new_tokens=50, #number of tokens to be generated
    do_sample=True, #to add randomness in the words selection
    num_return_sequences=1, # will only generate one sequence
    assistant_model=draft_model, #draft model for speculation
)
end = time.time()

spec_text = tokenizer.decode(spec_outputs[0], skip_special_tokens=True)
print(f"Output Text: {spec_text}")
print("Time taken: (Speculative)",round(end-start, 3), "seconds")

# Step 6. Compare Results
print("\nComparison of Outputs")
print("\nNormal Decoding Output:\n", normal_text)
print("\nSpeculative Decoding Output:\n", spec_text)