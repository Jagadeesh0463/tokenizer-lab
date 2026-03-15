# LLM Tokenizer Explorer

A hands-on lab to explore and compare how different LLM tokenizers work using the Hugging Face `transformers` library.

---

## What This Project Does

- Tokenizes text using different LLM tokenizers
- Visualizes tokens in different colors
- Compares tokenization strategies across models
- Explores vocabulary length and special tokens

---

## Project Structure
```
llm-tokenizer-explorer/
│
├── .env                    # API keys (never commit this!)
├── .gitignore              # Protects .env from github
├── requirements.txt        # Project dependencies
├── helper.py               # Reusable helper functions
└── tokenizer_lab.ipynb     # Main Jupyter notebook
```

---

## Models Explored

| Model | Description |
|---|---|
| `bert-base-cased` | BERT cased tokenizer |
| `bert-base-uncased` | BERT uncased tokenizer |
| `Xenova/gpt-4` | GPT-4 tokenizer |
| `gpt2` | GPT-2 tokenizer |
| `google/flan-t5-small` | Flan-T5 tokenizer |

---

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/llm-tokenizer-explorer.git
cd llm-tokenizer-explorer
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` File
```bash
touch .env
```
Add this inside:
```
OPENAI_API_KEY=your_openai_key_here
```

---

## How to Run

### Launch Jupyter Notebook
```bash
jupyter notebook
```
```
Browser opens
→ Click tokenizer_lab.ipynb
→ Click Kernel
→ Restart & Run All
```

---

## Helper Functions

### `load_env()`
Loads environment variables from `.env` file

### `get_openai_api_key()`
Returns OpenAI API key from `.env` file

### `show_tokens(sentence, tokenizer_name)`
Prints tokens in alternating colors with vocabulary length

---

## Example Output
```
Vocab length: 28996

[Hello] [World] [!]
```

---

## Requirements
```
transformers>=4.46.1
```

---

## Important Notes

- Never commit `.env` file
- Always activate virtual environment before running
- Run cells in order inside Jupyter notebook

---

## Author

Your Name
GitHub: your-username