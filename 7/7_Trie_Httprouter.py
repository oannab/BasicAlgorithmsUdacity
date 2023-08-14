""" Problem 7: Request Routing in a Web Server with a Trie
HTTPRouter using a Trie
"""

## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        self.children = {} # store children nodes with associated value - path
        self.handler = None # to attribute functions to the deepest children nodes on a path.

    def insert(self, path): #TC is worst case O(n), n is the length of the path created/ nodes inserted into dictionary
        # Insert the node as befores
        if path not in self.children: # path is the key and the value is the children node in the dictionary 
            self.children[path] = RouteTrieNode() # create a new child node with the associated path value


# Example usage:
# node = RouteTrieNode()
# node.insert("about")


## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode() # root node 
        self.root_handler = root_handler # the root handler - function attribute for the root node

    def insert(self, path, handler): #TC is O(n) n is the number of segments on a path, with a single traversal per segment - segments = node children
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root # start at root node
        for p in path: # traverse each path
            if p not in node.children: # if the path is not in the children of the node, create a new node with the path value and assign it as a child node 
                node.children[p] = RouteTrieNode() # create a new child node with the associated path value 
            node = node.children[p] # move to the next node in the path
        node.handler = handler # when last node is reached, a handler is assigned
        

    def find(self, path): # TC is O(n) n is the number of segments on a path it needs to traverse, with a single traversal per segment -> segments = node children
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root # start at root node
        for p in path: # traverse each path
            if p not in node.children: # if the path is not in the children of the node, return None
                return None
            node = node.children[p] # move to the next node in the path 
        return node.handler # if found - when last node is reached, return the handler for the node    


""" *** """

## The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, error_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie(root_handler) # create the root node with the function attribute for the root node
        self.error_handler = error_handler # error handler - function attribute for the root node if path not found


    def add_handler(self, path, handler): # TC is O(n) n is the number of segments on a path 
        # Add a handler for a specific path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(path) # split the path into parts - O(n), n length of path/ no of children
        self.route.insert(path, handler) # call the insert method on the RouteTrie to add the handler to the Trie path - O(n), calling the insert() method 

        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path = self.split_path(path) # split the path into parts
        handler = self.route.find(path) # call the find method on the RouteTrie to find the handler for the path
        if handler == None: 
            return self.error_handler if self.error_handler is not None else None # if not found - return the error handler
        return handler
    
    
    def split_path(self, path): # O(n), n is the no of segments in a path
        # you need to split the path into parts for 
        # both the add_handler and loopup functions, so it should be placed in a function here
        if path == "/":
            return ["/"] # return the root segment in a list
        if path[-1] == "/" and path != "/": # remove trailing slash
            path = path[:-1] # remove trailing slash
        return path.split("/")[1:] if path != "/" else []# exclude the root segment unless root node is '/', then return empty list with nodes/segments

##Test Cases
## Here are some test cases and expected outputs you can use to test your implementation
## create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one




"""
References:
https://github.com/Nishtha-Jaiswal/Problems-vs.-Algorithms/blob/master/Request%20Routing%20in%20a%20Web%20Server%20with%20a%20Trie.py
https://www.youtube.com/watch?v=2L7CtCww12E

"""





"""Problem 7: Request Routing in a Web Server with a Trie
HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter 
like you would find in a typical web server using the Trie data 
structure we learned previously.
There are many different implementations of HTTP Routers such as 
regular expressions or simple string matching, but the Trie is an 
excellent and very efficient data structure for this purpose.
The purpose of an HTTP Router is to take a URL path like "/", "/about", 
or "/blog/2019-01-15/my-awesome-blog-post" and figure out what 
content to return. In a dynamic web server, the content will often 
come from a block of code called a handler.
First we need to implement a slightly different Trie than the one 
we used for autocomplete. Instead of simple words the Trie will 
contain a part of the http path at each node, building from the 
root node /
In addition to a path though, we need to know which function will 
handle the http request. In a real router we would probably pass 
an instance of a class like Python's SimpleHTTPRequestHandler which 
would be responsible for handling requests to that path. For the 
sake of simplicity we will just use a string that we can print out 
to ensure we got the right handler
We could split the path into letters similar to how we did the 
autocomplete Trie, but this would result in a Trie with a very 
large number of nodes and lengthy traversals if we have a lot of 
pages on our site. A more sensible way to split things would be 
on the parts of the path that are separated by slashes ("/"). 
A Trie with a single path entry of: "/about/me" would look like:
(root, None) -> ("about", None) -> ("me", "About Me handler")
We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

*** Next we need to implement the actual Router. 
The router will initialize itself with a RouteTrie for 
holding routes and associated handlers. It should also support 
adding a handler by path and looking up a handler by path. 
All of these operations will be delegated to the RouteTrie.
Hint: the RouteTrie stores handlers under path parts, so remember 
to split your path around the '/' character
Bonus Points: Add a not found handler to your Router which is returned 
whenever a path is not found in the Trie.
More Bonus Points: Handle trailing slashes! A request 
for '/about' or '/about/' are probably looking for the same page. 
Requests for '' or '/' are probably looking for the root handler. 
Handle these edge cases in your Router.
"""