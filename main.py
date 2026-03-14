import warnings
from transformers import AutoTokenizer
from helper import show_tokens

warnings.filterwarnings("ignore")

# -----------------------------------------
# Basic Tokenization Example
# -----------------------------------------

sentence = "Hello world!"

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

token_ids = tokenizer(sentence).input_ids

print("Token IDs:")
print(token_ids)

print("\nTokens:")
for id in token_ids:
    print(tokenizer.decode(id))


# -----------------------------------------
# Tokenization Visualization
# -----------------------------------------

text = """
English and CAPITALIZATION
🎵 鸟
show_tokens False None elif == >= else: two tabs:"    " Three tabs: "       "
12.0*50=600
"""

print("\n----- BERT CASED -----")
show_tokens(text, "bert-base-cased")

print("\n----- BERT UNCASED -----")
show_tokens(text, "bert-base-uncased")

print("\n----- GPT-4 TOKENIZER -----")
show_tokens(text, "Xenova/gpt-4")

print("\n----- GPT2 -----")
show_tokens(text, "gpt2")

print("\n----- FLAN-T5 -----")
show_tokens(text, "google/flan-t5-small")

print("\n----- STARCODER -----")
show_tokens(text, "bigcode/starcoder2-15b")

print("\n----- PHI-3 -----")
show_tokens(text, "microsoft/Phi-3-mini-4k-instruct")

print("\n----- QWEN2 -----")
show_tokens(text, "Qwen/Qwen2-VL-7B-Instruct")