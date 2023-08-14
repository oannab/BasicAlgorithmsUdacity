#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[1]:


## Represents a single node in the Trie - the building block
class TrieNode: # Space complexity is linear O(n), n is no of children which depends on no of unique characters
    def __init__(self): 
        ## Initialize this node in the Trie
        self.children = {}
        self.is_end_of_word = False
O
    def suffixes(self, suffix=''): # Time Complexity O(n) where n is the no of children the node has/the depth of Tries
        #generate suffixes that can be formed using the existing characters. 
        # traverse all chhildren nodes - characters
        suffix_list = []
        if self.is_end_of_word: #if current node during traversal is the last node
            suffix_list.append(suffix) # append the current suffix to the list
        
        for char, child_node in self.children.items():
            suffix_list.extend(child_node.suffixes(suffix + char)) # keep track of accumulated suffixes
        
        return suffix_list
        
    def insert(self, char): # O(1)
        # Add a child node in this Trie with associated character
        self.children[char] = TrieNode() # insert new character into a newly created node


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[2]:


class Trie: # Space complexity of the Trie is O(n), where the n is the unique characters in the input set of words
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word): # Time complexity is O(L) where L is length of characters in the word inserted. // O(n)
        node = self.root
        for ch in word: #iterate through each character in the word  - O(n), n = length of word
            if ch not in node.children:
                node.children[ch] = TrieNode() # create new node if not in children and add char to children node
            node = node.children[ch] # add char to children
        node.is_end_of_word = True # mark last char as end of word
        
    def find(self, prefix): # Time complexity is O(P), P is the lenght of a word/ number of characters in the input prefix // O(n) 
        node = self.root # start at root node
        for char in prefix: #traverse the Trie by character based on prefix
            if char not in node.children: # if char is not in children of current_node
                print("char", char)
                print("current_node", current_node)
                return None # return None if not found 
            node = node.children[char]
        return node # if whole word is found return the word
        
    def autocomplete_word(self, prefix): # Time complexity is O(P+N), P is the length of prefix, N is the no of children in the prefix node
        results = []
        prefix_node = self.find(prefix)
        if prefix_node:
            results.extend(prefix_node.suffixes(prefix))
        return results


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[3]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[4]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# ## Problem 4: Autocomplete with Trie
# 
# **Requirement:**
# 
# * A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix. 
# 
# 
# **TrieNode Class**
# - building block for the Trie - creates nodes 
# - root node and children nodes that map the characters from a dictionary
# - is_end_of_word() attribute is a boolean that indicates if the character / leaf-child node represents the end of a word
# - Overall space complexity -  worst-case is linear - O(n) - where n is the total no of children the Trie node has. A node can have n children - dependant on the length of words.
# - Overall time complexity is O(n) - traverse and visit all nodes O(N), where N is total no of nodes + generate suffixes for each node and appending chars to the new nodes O(L), where n is length of longest word inserted
# 
# 
# *suffixes()
# - recursively traverses the Trie, until it finds an end_of_word node
# - returns a list with suffixes that can be made
# - Time complexity is given by the number of children a node has and the depth of the Trie it has to traverse. Since each node represents a character, the function traverses each node in the Trie -->> the time complexity is linear O(n)
# 
# *insert()
# - creates a new TrieNode child node instance and adds a new character to it
# - time complexity is O(1) due to operations like checking the dictionary and adding key-value pairs
# 
# 
# **Trie Class**
# - Overall time complexity is O(n) - n is total no' of nodes in subtree
# - Space complexity is linear O(n). complexity is given by the number of unique characters inserted in words in Trie. The total number of nodes in the Trie is dependend on the total number of characters across all the words.
# 
# 
# - instantiate a root node using the TrieNode class. serves as starting point for all operations
# *insert()
# - Time complexity is linear - O(L) where L is length of characters in the word inserted. // O(n)
# - instantiate a root node
# 
# *find()
# - search for prefix in the Trie starting at root node, iterating troguh all existing nodes searching for an input character and checks  if that character is associated with an existing node. Traversal returns the corresponding node associated with the character if that exists in the Trie. If node (character associated with a node) doesn't exit the method returns None.
# - If prefix is found, the last corresponding character/node of the input prefix is returned, and it serves as a starting point for further operation like autocompletion, by traversing the Trie from this point
# - Time Complexity is linear - O(P) where P is the length of prefix. 
# 
# *autocomplete_word()
# - uses the find() method to locate the node corresponding to the end of input prefix.
# - if prefix is found, returns the node corresponding to the last character in the prefix. 
# - if prefix exists, it retrieves suffixes using suffixes() to generate a list with all possible suffixes that can be generated by using the chars in the subtree that roots/starts from the end node point of the prefix found. Suffixes() traverses recursively the Trie below the end node in the prefix and lists all completed words in all subroots/nodes - marked by end-of-word.
# - the method taked generated sufixxes list and adds them to result[] that holds all possible completions for the input prefix.
# - Time complexity is O(P+N) where P is the length of input prefix and N is the no of children in the prefix node. 
# 
# 
# 
# *references:
# - https://www.geeksforgeeks.org/trie-insert-and-search/
# - https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
# - https://stackoverflow.com/questions/46038694/implementing-a-trie-to-support-autocomplete-in-python
# - https://www.lavivienpost.com/autocomplete-with-trie-code/
# - https://mailtojyoti2005.medium.com/implementing-autocomplete-feature-in-python-using-trie-data-structure-73f78a9aa47
# - https://www.youtube.com/watch?v=P89vzewWDdw

# In[ ]:




