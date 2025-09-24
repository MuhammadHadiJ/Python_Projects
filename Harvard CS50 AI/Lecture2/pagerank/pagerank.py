import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000
Testing = False


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
    
    total_pages = len(corpus)
    probabilities = dict()
    links = corpus[page]

    if links:
        for Page in corpus:
            probabilities[Page] = (1 - damping_factor) / total_pages
            if Page in links:
                probabilities[Page] += damping_factor / len(links)
    else:
        # Page has no outgoing links: treat it like it links to all pages
        for Page in corpus:
            probabilities[Page] = 1 / total_pages

    return probabilities


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    StartPage = random.choice(list(corpus.keys()))
    weights = transition_model(corpus,StartPage,damping_factor)
    dist = dict()
    for i in corpus.keys():
        dist[i] = 0
    InfluencingAmount = 1/n
    for i in range(n):
        Page = random.choices(list(weights.keys()),list(weights.values()),k=1)[0]
        dist.update({Page:dist.get(Page) + InfluencingAmount})
        weights = transition_model(corpus,Page,damping_factor)
    return dist
    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    Pages = list(corpus.keys())
    dist = dict()

    for i in Pages:
        dist[i] = 1/len(Pages)
    while True:
        dist2 = dist.copy()
        for i in Pages:
            p1 = 1-damping_factor
            p1 = p1/len(Pages)

            PagesI = list()
            for j in Pages:
                OutboundLinks = list(corpus.get(j))
                if i in OutboundLinks:
                    PagesI.append(j)
                elif len(OutboundLinks) == 0:
                    PagesI.append(j)
            p2 = 0

            for q in PagesI:
                if len(list(corpus.get(q))) > 0:
                    p2 += dist[q]/len(list(corpus.get(q)))
                else:
                    p2 += dist[q]/len(Pages)
            p2 *= damping_factor
            PageRank = p1 + p2
            dist2.update({i:PageRank})
        V = 0
        for i in dist.keys():
            if abs(dist.get(i) - dist2.get(i)) < 0.001:
                V += 1
        if V == len(list(dist.keys())):
            return dist2
        else:
            V = 0
        dist = dist2.copy()
    raise NotImplementedError


if __name__ == "__main__":
    main()
