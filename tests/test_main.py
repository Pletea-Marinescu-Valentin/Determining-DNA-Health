import unittest
from main import getHealth, Trie

class TestDNAHealth(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert("a", 1)
        self.trie.insert("b", 2)
        self.trie.insert("ab", 3)

    def test_single_gene(self):
        self.assertEqual(getHealth("a", 0, 0, self.trie), 1)

    def test_multiple_genes(self):
        self.assertEqual(getHealth("ab", 0, 1, self.trie), 4)

    def test_no_match(self):
        self.assertEqual(getHealth("c", 0, 1, self.trie), 0)

if __name__ == "__main__":
    unittest.main()
