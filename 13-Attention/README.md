# CS50 AI Project: Attention

An exploration and visualization of transformer self-attention mechanisms in **BERT (Bidirectional Encoder Representations from Transformers)** for Masked Language Modeling (MLM), implemented for Harvard University's **CS50's Introduction to Artificial Intelligence with Python**.

---

## 1. Overview & Problem Description

Modern transformer models like BERT utilize multi-head self-attention to dynamically capture contextual relationships between words. Rather than processing text strictly left-to-right, bidirectional self-attention enables each token to attend to all other tokens across multiple transformer layers.

In this project:
1. We use Hugging Face's `transformers` library with `bert-base-uncased` to predict masked tokens in a sentence (e.g., `We turned down a narrow [MASK] to reach the harbor.`).
2. We extract raw attention weights across all 12 layers and 12 attention heads ($12 \times 12 = 144$ attention matrices).
3. We generate attention heatmaps visualizing which tokens attend to which other tokens.
4. We analyze specific attention heads that perform distinct linguistic functions (e.g., determiner-to-noun binding and immediate left-token context aggregation).

---

## 2. Key Components

- `mask.py`:
  - Tokenizes input with BERT tokenizer.
  - Predicts top $K$ candidate tokens for the `[MASK]` token based on output logits.
  - Generates grid diagrams visualizing attention matrices for all layers and heads.
- `analysis.md`: Detailed linguistic analysis of specific attention heads:
  - **Layer 4, Head 10:** Determiner-to-noun attention (e.g., "the" $\to$ "engineer", "a" $\to$ "bridge").
  - **Layer 4, Head 6:** Immediate previous token attention ($i \to i - 1$ diagonal band).
- `assets/`: Fonts and visual assets used when rendering attention diagrams.

---

## 3. Installation & Requirements

Ensure dependencies are installed:
```bash
pip install -r requirements.txt
```
*(Requires `transformers`, `torch`, `Pillow`, and `tensorflow`)*

---

## 4. Execution Instructions

Run the masked language model with an input sentence containing `[MASK]`:
```bash
python mask.py
```

### Interactive Prompt:
```text
Text: We turned down a narrow [MASK] to reach the harbor.
```

The script will:
1. Output the top predicted words for the `[MASK]` token with associated probabilities.
2. Render attention visualization diagrams into the current working directory.

