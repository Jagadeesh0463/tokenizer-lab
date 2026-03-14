# Tokenizer Analysis Lab

## Overview

This project demonstrates how different Large Language Model (LLM) tokenizers process and split text into tokens.
Using the Hugging Face `transformers` library, the project compares multiple tokenizers and visualizes how each model interprets the same input text.

Tokenization is a fundamental step in Natural Language Processing (NLP) because language models operate on tokens rather than raw text. Understanding these differences helps in evaluating model behavior and preprocessing strategies.

---

## Objectives

The main goals of this project are:

* Demonstrate how tokenization works in modern LLMs
* Compare tokenization strategies across multiple models
* Visualize token outputs in a readable colored format
* Examine how models treat:

  * Capitalization
  * Special characters
  * Unicode symbols
  * Programming operators
  * Whitespace and tab characters

---

## Technologies Used

| Technology                | Purpose                                |
| ------------------------- | -------------------------------------- |
| Python                    | Core programming language              |
| Hugging Face Transformers | Tokenizer implementations              |
| python-dotenv             | Secure environment variable management |
| VS Code                   | Development environment                |

---

## Project Structure

```text
TOKENIZER-LAB
│
├── helper.py        # Utility functions and token visualization
├── main.py          # Main script to execute tokenizer comparisons
├── .env             # Environment variables (API keys)
├── .gitignore       # Ignored files for version control
├── README.md        # Project documentation
└── .venv            # Local Python virtual environment
```

---

## Setup Instructions

### 1. Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

---

### 2. Install Dependencies

```bash
python3 -m pip install transformers python-dotenv
```

---

## Environment Configuration

The project loads API keys using a `.env` file for secure configuration.

Create a `.env` file in the project root directory:

```
OPENAI_API_KEY=your_api_key_here
```

Example:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

This approach prevents sensitive credentials from being stored directly in the codebase.

---

## Tokenization Workflow

### Step 1 – Basic Tokenization

The program first tokenizes the sentence:

```
Hello world!
```

using the `bert-base-cased` tokenizer.

Example process:

1. Load tokenizer
2. Convert text into token IDs
3. Decode tokens back into readable text

---

### Step 2 – Token Visualization

The project provides a utility function:

```
show_tokens(text, tokenizer_name)
```

This function:

* Loads the specified tokenizer
* Converts input text to token IDs
* Displays token vocabulary size
* Prints tokens in color-coded format for clarity

---

## Models Evaluated

The following tokenizers are compared in this project:

| Model                            | Description                          |
| -------------------------------- | ------------------------------------ |
| bert-base-cased                  | Case-sensitive BERT tokenizer        |
| bert-base-uncased                | Lowercase BERT tokenizer             |
| Xenova/gpt-4                     | GPT-style tokenizer implementation   |
| gpt2                             | OpenAI GPT-2 tokenizer               |
| google/flan-t5-small             | T5 sequence-to-sequence tokenizer    |
| bigcode/starcoder2-15b           | Code-focused tokenizer               |
| microsoft/Phi-3-mini-4k-instruct | Microsoft Phi-3 tokenizer            |
| Qwen/Qwen2-VL-7B-Instruct        | Multimodal vision-language tokenizer |

---

## Key Observations

The comparison highlights several differences between tokenizers:

* Vocabulary sizes vary significantly across models
* Case-sensitive tokenizers preserve capitalization
* Emojis and Unicode characters may be split differently
* Code-oriented tokenizers better recognize programming symbols
* Whitespace and tabs can be represented as separate tokens

These differences influence how models interpret user input and generate responses.

---

## Running the Project

Execute the main script:

```bash
python main.py
```

The program will:

1. Tokenize sample text
2. Display token IDs
3. Visualize tokenization results for multiple models

---

## Version Control Configuration

The following files are excluded from Git tracking using `.gitignore`:

```
.venv/
__pycache__/
.env
```

These directories contain:

* Local virtual environments
* Temporary Python cache files
* Sensitive configuration data

---

## Conclusion

This project demonstrates how tokenization strategies vary across different language models and highlights the importance of understanding token-level processing in LLM-based applications.

The visualization approach used here provides an intuitive way to analyze tokenizer behavior and compare multiple models in a consistent environment.
