# ⚡ Speculative Decoding Demo — Faster Token Generation with Hugging Face

[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg?logo=huggingface&logoColor=white)](https://huggingface.co/transformers)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI%20Demo-ff4b4b.svg?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/github/license/AshleyMathias/Speculative-Decoding)](LICENSE)

An interactive **Speculative Decoding demo** built with Hugging Face Transformers, PyTorch, and Streamlit. It compares **normal greedy decoding** vs **speculative decoding** side by side — so you can see how speculative methods speed up token generation in Large Language Models. 🚀

---

## 🚀 Features

- Compare **Normal Greedy Decoding** vs **Speculative Decoding**
- Uses **two models**:  
  - Draft (small, fast) model  
  - Target (larger, accurate) model
- Measure and display **time taken** for both methods
- Simple **Streamlit UI** for user prompts
- Works on CPU (learning), but **real speedups appear on GPU**

---

## 🖼️ Screenshot

| Streamlit UI |
|--------------|
| ![Streamlit Screenshot](Screenshot.png) |

---

## 🧱 Tech Stack

- `Hugging Face Transformers`
- `PyTorch`
- `Streamlit`
- `Python 3.10+`

---

## 🛠️ Installation

```bash
git clone https://github.com/AshleyMathias/Speculative-Decoding.git
cd Speculative-Decoding
