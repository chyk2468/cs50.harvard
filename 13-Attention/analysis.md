<!-- # chyk2468 -->
# Analysis

## Layer 4, Head 10

In Layer 4, Head 10, determiner tokens (such as "the" and "a") strongly attend to the head noun of the noun phrase that they introduce. Across multiple test sentences, the determiner allocates the vast majority of its attention weight (consistently between 73% and 95%) to the noun directly following it, rather than attending to preceding words, delimiters, or verbs.

In the generated attention heatmaps, this relationship produces distinctive bright cells in the row corresponding to the determiner, specifically focused on the column of the associated noun.

Example Sentences:
- The engineer designed a bridge.
- The computer processed the data.
- The book was placed on the table.

In "The engineer designed a bridge.", the initial determiner "the" at index 1 attends to "engineer" at index 2 with an attention weight of 0.9275 (92.8%), and the indefinite article "a" at index 4 attends to "bridge" at index 5 with an attention weight of 0.7316 (73.2%). Similarly, in "The computer processed the data.", the subject determiner "the" attends to "computer" with a weight of 0.9486 (94.9%), while the object determiner "the" attends to "data" with a weight of 0.8935 (89.4%). In "The book was placed on the table.", the prepositional determiner "the" attends to "table" with an attention weight of 0.9532 (95.3%).

A notable limitation or inconsistency occurs when descriptive adjectives intervene between the determiner and noun (e.g., "the young scientist"); in those cases, the determiner's attention tends to split between the modifying adjective and the noun. Furthermore, non-determiner tokens do not exhibit this focused rightward pattern in this head.

---

## Layer 4, Head 6

In Layer 4, Head 6, tokens systematically attend to the token immediately preceding them in the sequence ($i \to i-1$). This head functions as a sequential left-context aggregator, allowing each token's representation to incorporate immediate prior contextual information from its neighboring word.

In the attention diagram, this behavior manifests as a prominent bright diagonal band shifted exactly one position to the left of the main diagonal, corresponding to cell coordinates $(i, i - 1)$.

Example Sentences:
- The engineer designed a bridge.
- The computer processed the data.

In "The engineer designed a bridge.", "engineer" (index 2) attends to the preceding "the" (index 1) with an attention weight of 0.8633 (86.3%), "designed" (index 3) attends to "engineer" (index 2) with weight 0.4292 (42.9%), "a" (index 4) attends to "designed" (index 3) with weight 0.9646 (96.5%), "bridge" (index 5) attends to "a" (index 4) with weight 0.7031 (70.3%), and the period "." (index 6) attends to "bridge" (index 5) with weight 0.6376 (63.8%). In "The computer processed the data.", "computer" attends to "the" with 0.7975 (79.8%), "processed" attends to "computer" with 0.5849 (58.5%), "the" attends to "processed" with 0.9899 (99.0%), "data" attends to "the" with 0.8296 (83.0%), and "." attends to "data" with 0.6705 (67.1%).

A clear exception to this leftward pattern is the sentence boundary token [SEP], which does not attend to the preceding punctuation mark but instead directs nearly all of its attention back to the initial [CLS] token (weights of 0.8730 and 0.8886 respectively).
