import math
import bisect
import collections
import logging
import json

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.health_values = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, health):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.health_values.append(health)

    def search(self, strand):
        # Efficient substring matching logic
        node = self.root
        for char in strand:
            if char in node.children:
                node = node.children[char]
            else:
                node = self.root
            if node.is_end_of_word:
                yield ''.join(node.health_values)

def getHealth(strand, first, last, trie):
    h = 0
    for health in trie.search(strand):
        h += health
    return h

def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

def main():
    logging.basicConfig(level=logging.INFO)
    config = load_config('config.json')

    # Read input based on config
    howGenes = config['howGenes']
    genes = config['genes']
    healths = config['healths']
    weights = config['weights']
    howStrands = config['howStrands']

    # Build Trie
    trie = Trie()
    for i, gene in enumerate(genes):
        trie.insert(gene, healths[i] * weights[i])

    # Process strands
    hMin, hMax = math.inf, 0
    for strand_info in config['strands']:
        first = strand_info['first']
        last = strand_info['last']
        strand = strand_info['strand']
        h = getHealth(strand, first, last, trie)
        hMin, hMax = min(hMin, h), max(hMax, h)

    # Printing the minimum and maximum health values for all strands
    print(hMin, hMax)

if __name__ == "__main__":
    main()
