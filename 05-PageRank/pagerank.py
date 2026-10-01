# chyk2468
import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    num_pages = len(corpus)
    if num_pages == 0:
        return {}

    # If the page has no outgoing links, treat it as linking to all pages
    links = corpus.get(page, set())
    if not links:
        return {p: 1.0 / num_pages for p in corpus}

    # Each page gets base probability from random jump
    base_prob = (1.0 - damping_factor) / num_pages
    # Outgoing links get additional probability from following a link
    link_prob = damping_factor / len(links)

    distribution = dict()
    for p in corpus:
        distribution[p] = base_prob + (link_prob if p in links else 0.0)

    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    if not corpus or n <= 0:
        return {page: 0.0 for page in corpus}

    counts = {page: 0 for page in corpus}
    pages = list(corpus.keys())

    # The first sample is chosen uniformly at random from all pages
    current_page = random.choice(pages)
    counts[current_page] += 1

    # Generate remaining n - 1 samples using transition model
    for _ in range(n - 1):
        dist = transition_model(corpus, current_page, damping_factor)
        next_pages = list(dist.keys())
        weights = list(dist.values())
        current_page = random.choices(next_pages, weights=weights, k=1)[0]
        counts[current_page] += 1

    # Convert counts to proportions
    return {page: count / n for page, count in counts.items()}


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    num_pages = len(corpus)
    if num_pages == 0:
        return {}

    # Initialize each page with an equal rank of 1 / N
    current_ranks = {page: 1.0 / num_pages for page in corpus}

    # Pre-process links: a page with no outgoing links is interpreted
    # as having a link to every page in the corpus (including itself).
    all_pages = set(corpus.keys())
    effective_links = {
        page: links if len(links) > 0 else all_pages
        for page, links in corpus.items()
    }

    base_rank = (1.0 - damping_factor) / num_pages

    while True:
        new_ranks = dict()
        for p in corpus:
            link_sum = sum(
                current_ranks[i] / len(effective_links[i])
                for i in corpus
                if p in effective_links[i]
            )
            new_ranks[p] = base_rank + damping_factor * link_sum

        # Check convergence: no PageRank value changes by more than 0.001
        converged = all(
            abs(new_ranks[p] - current_ranks[p]) <= 0.001
            for p in corpus
        )

        current_ranks = new_ranks

        if converged:
            break

    # Normalize so that values sum to 1
    total = sum(current_ranks.values())
    return {p: rank / total for p, rank in current_ranks.items()}


if __name__ == "__main__":
    main()
