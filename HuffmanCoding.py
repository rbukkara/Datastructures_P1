import sys
import copy
from collections import deque


class Node(object):

    def __init__(self, value=None, times=1):
        self.chars = value
        self.times = times
        self.left = None
        self.right = None

    def set_value(self, value):
        self.chars = value

    def get_value(self):
        return self.chars + "-" + str(self.times)

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.times == other.times
        return False

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.times < other.times
        return False

    def __gt__(self, other):
        if isinstance(other, Node):
            return self.times > other.times
        return False


class Queue:

    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Tree(object):

    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while (len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


def char_dictionary(data):

    result = dict()
    for i in range(len(data)):
        if data[i] in result:
            result[data[i]] += 1
        else:
            result[data[i]] = 1

    if len(result.keys()) < 1:
        'padded characters to address edge cases'
        result[''] = 1
        result[None] = 0

    return result


def get_minelement_withpop(char_dic, curr_key=""):

    least_key = None
    least_val = None
    for key in char_dic:
        if key != curr_key:
            if least_key is None:
                least_key = key
                least_val = char_dic[key]
            else:
                if char_dic[key] < least_val:
                    least_key = key
                    least_val = char_dic[key]

    least = {"chars": least_key, "times": least_val}
    #print(least)
    del char_dic[least_key]
    return least, char_dic


def binary_code_dictionary(char_dic, tree):

    code_dict = dict()
    # traverse the tree looking for the chars in each node
    # and assign 0 for each left move and right for each move.
    copy_tree = copy.deepcopy(tree)

    for key in char_dic.keys():
        node = copy_tree.get_root()
        code = ""
        while node is not None:
            if key in node.chars:
                if (node.get_right_child() is not None) and (key in node.get_right_child().chars):
                    code += "1"
                    node = node.get_right_child()
                elif (node.get_left_child() is not None) and key in node.get_left_child().chars:
                    code += "0"
                    node = node.get_left_child()
                else:
                    code_dict[key] = code
                    node = None

    return code_dict

def huffman_encoding(data):

    if data == "":
        print("invalid data. unable to encode")
        return "0", Tree()

    if data is None:
        print("Cannot perform encoding")
        return None, Tree()

    char_dic = char_dictionary(data)
    dic_copy = copy.deepcopy(char_dic)
    char_node_dict = dict()
    result_tree = Tree()
    code_dic = None

    if len(dic_copy.keys()) > 1:

        while True:

            if len(dic_copy.keys()) == 1:
                root_elem, dic_copy = get_minelement_withpop(dic_copy)
                root_node = None
                if root_elem["chars"] in char_node_dict:
                    root_node = char_node_dict[root_elem["chars"]]
                else:
                    root_node = Node(root_elem["chars"], root_elem["times"])
                result_tree.set_root(root_node)
                break

            elem1, dic_copy = get_minelement_withpop(dic_copy)
            elem2, dic_copy = get_minelement_withpop(dic_copy)

            new_key = ''.join(sorted(set(elem1["chars"] + elem2["chars"])))
            parent_node = Node(new_key, elem1["times"] + elem2["times"])
            if elem1["chars"] in char_node_dict:
                parent_node.set_left_child(char_node_dict[elem1["chars"]])
            else:
                left_node = Node(elem1["chars"], elem1["times"])
                parent_node.set_left_child(left_node)
            if elem2["chars"] in char_node_dict:
                parent_node.set_right_child(char_node_dict[elem2["chars"]])
            else:
                right_node = Node(elem2["chars"], elem2["times"])
                parent_node.set_right_child(right_node)
            #print(parent_node)
            char_node_dict[new_key] = parent_node
            dic_copy[new_key] = parent_node.times

        code_dic = binary_code_dictionary(char_dic, result_tree)

    else:
        code_dic = dict()
        code_dic[data[0]] = "0"
        root_node = Node(data[0])
        result_tree.set_root(root_node)

    #print(code_dic)

    encoded_data = ""

    for char in data:
        encoded_data += code_dic[char]

    return encoded_data, result_tree


def traverse_nodes(node, encode_decodes, path):

    if node:
        if not node.has_left_child() and not node.has_right_child():
            encode_decodes[path] = node.chars
            return encode_decodes
        if node.has_left_child():
            lpath = path + "0"
            encode_decodes = traverse_nodes(node.left, encode_decodes, lpath)
        if node.has_right_child():
            rpath = path + "1"
            encode_decodes = traverse_nodes(node.right, encode_decodes, rpath)

    #print(encode_decodes)

    return encode_decodes


def decoded_key_values(ptree):

    if not ptree.get_root().has_left_child() and not ptree.get_root().has_right_child():
        encode_decodes = dict()
        encode_decodes["0"] = ptree.get_root().chars
        #print(encode_decodes)
        return encode_decodes

    encode_decodes = traverse_nodes(ptree.get_root(), dict(), "")
    #print(encode_decodes)
    return encode_decodes


def huffman_decoding(data, tree):

    if data == "0":
        print("invalid data. unable to decode")
        return ""

    if data is None:
        print("Cannot perform encoding")
        return None

    decoded_sentence = ""
    key_value_dict = decoded_key_values(tree)

    #print("decoded key values are below")
    #print(key_value_dict)

    cur_char = ""
    for char in data:
        cur_char += char
        if cur_char in key_value_dict:
            decoded_sentence += key_value_dict[cur_char]
            cur_char = ""

    return decoded_sentence


#a_great_sentence = "cool zoo is amazing in the summer"
#a_great_sentence = "Huffman Algorithm is amazingly right"
a_great_sentence = "What is going on now? Why is it right? my poor decoding algorithm messed it up!"
a_great_sentence = "What makes a great sentence? A lot of words or a few of great words?"
#a_great_sentence = "aaaaaaaaa"
a_great_sentence = ""
#a_great_sentence = None

print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))

encoded_huff, tree = huffman_encoding(a_great_sentence)

print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_huff, base=2))))

#print(tree)

decoded_data = huffman_decoding(encoded_huff, tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))
if decoded_data == a_great_sentence:
    print("Success!")