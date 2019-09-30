# Datastructures_P1
The following is a series of projects completed as part of Udacity Nanodegree program in Data Structures and Algorithms. 
It deals with Data Structures aspect

Active Directory:

Chose sets over specified lists in users and groups objects for quicker searches
Recursively iterate over groups to find the user.

Time complexity Big O : O(N) 
where N is the number of groups

Space Complexity : O(N * M)
where N is the number of groups and M is the max number of subgroups for each group


BlockChain:

Added print_blockchain and add_block functions for adding a new block and printing the blockchain respectively. Hash function is part of the block class because we are not using it anywhere else

Add:
Time Complexity Big O : O(1)
Space Complexity : O(1)
We only add a single block and prepend it to the list therefore both of them are O(1)

Print:
Big O : O(N)
N is number of nodes
Space Complexity : O(N)
To print all nodes, we need to iterate over all of them which requires N memory locations


Filerecursion:

Recursively iterating over groups to find if the user is part of the group

Time Complexity Big O : O(N)
where N is the number of subdirectories

Worst Case Space Complexity : O(N * M)
where N is the number of subdirectories and M is the maximum number of subdirectories under the subdirectories


Huffman:

Encoding:

Explanation:
1) Create a dictionary with a unique counts of each character in the string
2) Get least repeated characters from the dictionary and start building the tree
3) For building it, get two least repeater characters, create a parent Node and 
4) Set the right and left nodes for the parent node, (left with least count) and save it another dictionary 
5) Create an entry for the parent node and put it back into the dictionary
6) loop steps 2 to 5 until only the parent node is left in the dictionary
7) create encoded characters for each character based on path from the root node
8) replace each character with the encoded character

Big O:
O(length of data) + O(min_character_traversal) + O(tree traversal) + O(length of data - for encoding) + O(sort for new key * number of keys)

O(N) + O(S * SlogS)
where N is the length of data and S is the number of unique characters for sort

Space Complexity :
O(S) where S is the number of unique characters for dictionary

Decoding:

1) get a dictionary of encoded and decoded characters from the tree based on the tree path
2) navigate through each character of the encoded string and replace it with each subsequent character from the encoded_decoded dictionary

Big(O):
O(tree traversal) + O(length of decoded text) ==> O(length of decoded text)

Space Complexity :
O(S) where S is the number of unique characters in the tree


LRUCache:

Used OrderedDict after suggested by the most recent code reviewer.
Learned that since it is still a dictionary, but retains the order of inserted elements, a perfect fit for the problem

Time Complexity:
Since we use a ordered dict the time complexity is O(1)

Space Complexity:
Since we use no other data structure the space complexity is O(1)


UnionIntersection:

I wanted to retain duplicated records for union and intersection operations.
The function could easily be implemented with Sets but we get un-duplicated elements.

Union:
Gets a list of distinct elements in the linkedlist as sets and perform union operation.

Time Complexity : O(LL1) + O(LL2) + O(union) ==> O(LL1) + O(LL2)
Space Complexity: O(LL1) + O(LL2) because we need to hold so many locations in memory

Intersection:
Gets a list of distinct elements in the linkedlist as sets and perform intersection operation.

Time Complexity : O(LL1) + O(LL2) + O(intersection) ==> O(LL1) + O(LL2)
Space Complexity: O(LL1) + O(LL2) because we need to hold so many locations
