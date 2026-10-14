# CS50 AI Project 6A: Parser

## Author
`chyk2468`

---

## 1. Overview
This project implements a Natural Language Processing (NLP) syntax parser using Python and the Natural Language Toolkit (**NLTK**). Given an English sentence, the parser constructs a Context-Free Grammar (CFG) parse tree that reveals the syntactic hierarchy of constituents—sentences ($S$), noun phrases ($NP$), verb phrases ($VP$), prepositional phrases ($PP$), and adjective phrases ($AP$)—and extracts all **Noun Phrase (NP) chunks** (base noun phrases containing no nested sub-noun phrases).

---

## 2. Preprocessing Pipeline (`preprocess`)
Before sentences can be parsed by a formal grammar, raw input strings must be normalized:
1. **Tokenization**: Uses `nltk.word_tokenize(sentence)` to decompose sentences into discrete word and punctuation tokens.
2. **Case Normalization**: Converts all tokens to lowercase strings.
3. **Punctuation & Numeric Filtering**: Retains only tokens containing at least one alphabetic character (`any(c.isalpha() for c in token)`). Pure punctuation (`.`, `,`, `!`, `?`) and numbers (`28`, `123`) are pruned.

---

## 3. Context-Free Grammar Design (`NONTERMINALS`)
The grammar is defined recursively to cover declarative sentences, compound sentences with coordinating conjunctions, adjective cascades, prepositional phrases, and verb phrase coordination:

```text
S -> NP VP | S Conj S

NP -> N | Det N | AP N | Det AP N | NP PP
AP -> Adj | Adj AP
PP -> P NP

VP -> V | V NP | VP PP | VP Adv | Adv VP | VP Conj VP
```

### Key Linguistic Capabilities:
- **Noun Phrase Modification**: Supports simple nouns (`holmes`), determiners (`the door`), single/multiple adjectives (`the little moist red paint`), and prepositional phrase attachments (`the palm of my hand`).
- **Verb Phrase Structures**: Handles intransitive verbs (`sat`), transitive verbs with direct objects (`lit a pipe`), verb-particle / adverbial modifiers (`sat down`, `never said a word`), prepositional adjuncts (`chuckled to himself`), and verb coordination (`sat down and lit his pipe`).
- **Compound Clauses**: Parses full clause coordination (`Holmes sat in the red armchair and he chuckled`) via `S -> S Conj S`.
- **Constraint Handling**: Rejects ungrammatical sequences such as double determiners (`*Holmes sat in the the armchair`) and inverted syntax (`*Armchair on the sat Holmes`).

---

## 4. Noun Phrase Chunking (`np_chunk`)
An **NP chunk** represents a non-overlapping base noun phrase that contains no nested $NP$ subtrees:
- Traverses all candidate subtrees with label `NP`.
- Verifies that no child or descendant subtree also carries the `NP` label.
- For nested structures like `[NP the palm of [NP my hand]]`, correctly extracts the leaf noun phrases `[the palm]` and `[my hand]`, while excluding the overarching complex noun phrase.

---

## 5. Execution

Run the parser on any sentence file:
```bash
python parser.py sentences/1.txt
python parser.py sentences/4.txt
python parser.py sentences/10.txt
```

Interactive input:
```bash
python parser.py
```
