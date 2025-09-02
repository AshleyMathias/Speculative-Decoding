import streamlit as st
import torch
import time
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load models and tokenizer only once (cache for performance)
@st.cache_resource
def load_models():
    target_model = AutoModelForCausalLM.from_pretrained("gpt2")
    draft_model = AutoModelForCausalLM.from_pretrained("sshleifer/tiny-gpt2")
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    return target_model, draft_model, tokenizer

target_model, draft_model, tokenizer = load_models()

# App UI
st.title("Speculative Decoding Demo")
st.write("Generate text using Normal Greedy Decoding or Speculative Decoding.")

# GPU info
if torch.cuda.is_available():
    st.success("✅ GPU detected. Using CUDA for faster generation.")
else:
    st.warning("⚠️ Running on CPU. Speculative decoding may not be faster, consider uisng GPU for 2,3x speedup.")

# Input section
user_prompt = st.text_area("Enter your prompt:", "In a shocking finding, scientists discovered")
decoding_method = st.radio("Choose decoding method:", ["Normal Greedy Decoding", "Speculative Decoding"])
max_tokens = st.slider("Max tokens to generate:", 20, 200, 80)

if st.button("Generate"):
    inputs = tokenizer(user_prompt, return_tensors="pt")

    start_time = time.time()

    if decoding_method == "Normal Greedy Decoding":
        outputs = target_model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=False
        )
    else:  # Speculative Decoding
        outputs = target_model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=True,
            assistant_model=draft_model,
        )
        
    end_time = time.time()

    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Output
    st.subheader("Generated Output:")
    st.write(output_text)
    st.markdown("---")
    st.caption(f"⏱️ Time taken: {end_time - start_time:.3f} seconds")
