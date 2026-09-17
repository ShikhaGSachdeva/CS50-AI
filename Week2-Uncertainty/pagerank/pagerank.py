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
    
    # Step 1 — initialize empty distribution
    distribution = {}
    
    # Step 2 — get total pages and links
    total_pages = len(corpus)
    links = corpus[page]          # pages current page links to
    num_links = len(links)
    
    # Step 3 — handle special case (no links)
    if num_links == 0:
        # treat as linking to all pages
        for p in corpus:
            distribution[p] = 1 / total_pages
        return distribution
    
    # Step 4 — calculate probability for each page
    for p in corpus:
        # base probability — random jump
        distribution[p] = (1 - damping_factor) / total_pages
        
        # additional probability — if linked
        if p in links:
            distribution[p] += damping_factor / num_links
    
    return distribution


def sample_pagerank(corpus, damping_factor, n):

    counts = {page: 0 for page in corpus}
    current_page = random.choice(list(corpus.keys()))

    for i in range(n):
        counts[current_page] += 1
        distribution = transition_model(corpus, current_page, damping_factor)
        pages = list(distribution.keys())
        weights = list(distribution.values())
        current_page = random.choices(pages, weights=weights, k=1)[0]

    return {page: counts[page] / n for page in counts}


def iterate_pagerank(corpus, damping_factor):

    N = len(corpus)
    pagerank = {page: 1/N for page in corpus}

    while True:
        new_pagerank = {}

        for page in corpus:
            # Part 1 — random jump
            new_pr = (1 - damping_factor) / N

            # Part 2 — link contribution
            for i in corpus:
                if len(corpus[i]) == 0:
                    new_pr += damping_factor * pagerank[i] / N
                elif page in corpus[i]:
                    new_pr += damping_factor * pagerank[i] / len(corpus[i])

            new_pagerank[page] = new_pr

        # Step 3 — check convergence
        converged = all(
            abs(new_pagerank[page] - pagerank[page]) < 0.001
            for page in pagerank
        )

        pagerank = new_pagerank

        if converged:
            return pagerank


if __name__ == "__main__":
    main()
