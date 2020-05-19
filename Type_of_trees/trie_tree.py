"""
class Trie:
  def __init__(self):
    self.root = {"*":"*"}

  def add_word(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node:
        curr_node[letter] = {}
      curr_node = curr_node[letter]
    curr_node["*"] = "*"
  
  def does_word_exist(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node:
        return False
      curr_node = curr_node[letter]
    return "*" in curr_node
"""

class TrieNode:
  def __init__(self, letter):
    self.letter = letter
    self.children = {}
    self.is_end_of_word = False

class Trie:
  def __init__(self):
    self.root = TrieNode("*")
  
  def add_word(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        curr_node.children[letter] = TrieNode(letter)
      curr_node = curr_node.children[letter]
    curr_node.is_end_of_word = True
  
  def does_word_exist(self, word):
    if word == "":
      return True
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        return False
      curr_node = curr_node.children[letter]
    return curr_node.is_end_of_word 


trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]
for word in words:
  trie.add_word(word)

print(trie.does_word_exist("wait")) #True
print(trie.does_word_exist("")) #True
print(trie.does_word_exist("waite")) #False
print(trie.does_word_exist("shop")) #True
print(trie.does_word_exist("shoppp")) #False
print(trie.add_word("shopping"))
print(trie.does_word_exist("shopping"))


class TrieNode:
  def __init__(self, letter):
    self.letter = letter
    self.children = {}
    self.is_end_of_word = False

class Trie:
  def __init__(self):
    self.root = TrieNode("*")
  
  def add_word(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        curr_node.children[letter] = TrieNode(letter)
      curr_node = curr_node.children[letter]
    curr_node.is_end_of_word = True
  
  def does_word_exist(self, word):
    if word == "":
      return True
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        return False
      curr_node = curr_node.children[letter]
    return curr_node.is_end_of_word 


trie = Trie()
words = ["wait", "waiter", "shop", "shopper"]
for word in words:
  trie.add_word(word)

print(trie.does_word_exist("wait")) #True
print(trie.does_word_exist("")) #True
print(trie.does_word_exist("waite")) #False
print(trie.does_word_exist("shop")) #True
print(trie.does_word_exist("shoppp")) #False
print(trie.add_word("shopping"))
print(trie.does_word_exist("shopping"))