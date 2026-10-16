# CS50 AI Project 6B: Questions (Information Retrieval QA System)

## Author
`chyk2468`

---

## 1. Overview
This project implements an automated question-answering (QA) and information retrieval system using Natural Language Processing (NLP) techniques and Term Frequency-Inverse Document Frequency (**TF-IDF**). Given a query and a directory of reference documents (corpus), the AI determines the most relevant document and extracts the best-matching sentence that answers the user's question.

---

## 2. Core Information Retrieval Architecture

### A. Document Loading (`load_files`)
- Reads all `.txt` documents within the designated corpus directory.
- Encodes file content into Python strings indexed by filename (e.g. `machine_learning.txt`).

### B. Preprocessing & Tokenization (`tokenize`)
- Decomposes raw document text into words using `nltk.word_tokenize(document)`.
- Converts tokens to lowercase.
- Prunes English stopwords using `nltk.corpus.stopwords.words("english")`.
- Filters out punctuation characters defined in Python's `string.punctuation`.
- Retains token sequence and repeated content without premature stemming or lemmatization.

### C. Inverse Document Frequency (`compute_idfs`)
For each distinct vocabulary word across all documents in the corpus, computes its inverse document frequency:
$$\text{IDF}(w) = \ln\left(\frac{\text{Total Documents}}{\text{Number of Documents Containing } w}\right)$$
- Words that appear across many documents (e.g. general terms) receive lower IDF weights.
- Specialized terms appearing in few documents receive high IDF weights.

### D. Document Ranking (`top_files`)
Ranks corpus documents by cumulative TF-IDF score for all words present in the user query:
$$\text{Score}(d) = \sum_{w \in \text{Query}} \text{TF}(w, d) \times \text{IDF}(w)$$
where $\text{TF}(w, d)$ is the frequency of word $w$ in document $d$.

### E. Sentence Ranking (`top_sentences`)
Once the most relevant document is selected, candidate sentences are ranked using two metrics:
1. **Matching Word Measure (Primary)**:
   $$\text{MWM}(s) = \sum_{w \in (\text{Query} \cap s)} \text{IDF}(w)$$
   Sums the IDF values for distinct query words occurring in the sentence.
2. **Query Term Density (Tie-Breaker)**:
   $$\text{Density}(s) = \frac{\text{Count of Sentence Tokens Belonging to Query}}{\text{Total Tokens in Sentence}}$$

---

## 3. Reference Corpus
The system operates over 6 comprehensive technical articles covering AI and CS fundamentals:
- `artificial_intelligence.txt`
- `machine_learning.txt`
- `natural_language_processing.txt`
- `neural_network.txt`
- `probability.txt`
- `python.txt`

---

## 4. Execution

Run the question-answering system passing the corpus directory:
```bash
python questions.py corpus
```

### Example Benchmark Interactions:
```text
$ python questions.py corpus
Query: What are the types of supervised learning?
Types of supervised learning algorithms include Active learning , classification and regression.

$ python questions.py corpus
Query: When was Python 3.0 released?
Python 3.0 was released on 3 December 2008.

$ python questions.py corpus
Query: How do neurons connect in a neural network?
Neurons of one layer connect only to neurons of the immediately preceding and immediately following layers.
```
