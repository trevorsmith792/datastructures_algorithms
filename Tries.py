class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Flag to mark the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create a new node for the character
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # Word not found
            node = node.children[char]
        return node.is_end_of_word  # Check if it is a complete word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  # No word starts with the given prefix
            node = node.children[char]
        return True  # Prefix exists

# Example usage:
trie = Trie()
trie.insert("hello")
trie.insert("helium")
trie.insert("hey")

print(trie.search("hello"))  # Output: True
print(trie.search("hel"))    # Output: False
print(trie.starts_with("he"))  # Output: True
print(trie.starts_with("hi"))  # Output: False
