# chyk2468
import math
import nltk
import os
import string
import sys

FILE_MATCHES = 1
SENTENCE_MATCHES = 1

# Cache stopwords and punctuation sets for performance
STOPWORDS = set(nltk.corpus.stopwords.words("english"))
PUNCTUATION = set(string.punctuation)


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = dict()
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    files[filename] = f.read()
    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    words = nltk.word_tokenize(document)
    filtered = []
    for word in words:
        w = word.lower()
        if w in STOPWORDS:
            continue
        if all(c in PUNCTUATION for c in w):
            continue
        filtered.append(w)
    return filtered


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    num_docs = len(documents)
    if num_docs == 0:
        return dict()

    # Create word sets for each document for fast lookup
    doc_word_sets = [set(words) for words in documents.values()]

    # Collect all unique words across all documents
    all_words = set().union(*doc_word_sets)

    idfs = dict()
    for word in all_words:
        doc_count = sum(1 for doc_words in doc_word_sets if word in doc_words)
        idfs[word] = math.log(num_docs / doc_count)

    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    scores = dict()
    for filename, words in files.items():
        score = 0.0
        for word in query:
            if word in idfs:
                tf = words.count(word)
                score += tf * idfs[word]
        scores[filename] = score

    sorted_files = sorted(scores.keys(), key=lambda f: scores[f], reverse=True)
    return sorted_files[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    def score_sentence(sentence):
        words = sentences[sentence]
        # 1. Matching word measure: sum of IDFs for distinct matching query words
        matching_words = query.intersection(words)
        matching_measure = sum(idfs.get(word, 0) for word in matching_words)

        # 2. Query term density: proportion of sentence words that are query words
        if len(words) == 0:
            density = 0.0
        else:
            density = sum(1 for w in words if w in query) / len(words)

        return (matching_measure, density)

    sorted_sentences = sorted(sentences.keys(), key=score_sentence, reverse=True)
    return sorted_sentences[:n]


if __name__ == "__main__":
    main()
