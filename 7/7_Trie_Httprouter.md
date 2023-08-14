**Problem 7: Request Routing in a Web Server with a Trie**
**Requirement**
- HTTPRouter using a Trie
- implement an HTTPRouter using the Trie data structure
- First we need to implement a slightly different Trie than the one we used for autocomplete. Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /
- In addition to a path though, we need to know which function will handle the http request. In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path. 
- For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler
- A way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like: 
    (root, None) -> ("about", None) -> ("me", "About Me handler")
- We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes. We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

_Abbreviation:_
_Time Complexity = TC_
_Space Complexity = SC_

 
**RouteTrieNode Class**
- constructor module

* insert()
- check if path/child does not exist
- create and insert new child node with path
- TC is O(n), n is the length of the path
- SC is O(n), n is no of children nodes created

**RouteTrie Class**
* insert()
- traverse each segment of given path. check if it exists. if exits, add handler to the last node on the segment. 
- if not, create new RouteTrieNode node and assign it a handler.
- TC is O(n) n is the number of segments on a path, with a single traversal per segment -> segments = node children
- SC is O(n) n is the number of newly created nodes/segments

* find()
- traverse each path segment and add child nodes if non existent
- return the handler for the last node if found
- TC is O(n) n is the number of segments on a path it needs to traverse, with a single traversal per segment -> segments = node children
- SC is O(1) as it doesn't allow additional memory to grow with the input size. It traverses the existing nodes without creating new data nor does it need more space to run even if the input size increases.

**Router Class**
* add_handler()
- split path and add handler to RouteTrie data structure
- TC is linear O(n) n is the number of segments on a path
- SC is O(n) n is the number of newly created nodes/segments

* lookup()
- split path into segments, traverse and find requested handler. return handler if found
- TC is linear O(n), n is length of path. the method traverses trough each node/segment.
- SC is constant O(1), as the memory used doesn't increase with the size of the path. It traverses existing nodes without creating additional Trie nodes.

* split_path()
- helper method
- the method splits the path by using the '/' as a demlimiter. This returns a list of segments.
- the f() creates a list to store individual segments of the path, stored as elements of a list
- TC is linear - O(n), n is the no of segments in a path
- SC is also linear - O(n), since n is the number of segments returned in a list that can increase