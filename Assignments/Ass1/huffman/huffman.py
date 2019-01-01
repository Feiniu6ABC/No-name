class Tree:
    """
    Stores the Huffman tree itself as a collection of nodes,
    for pickling. 

    The root of the tree is redefined for easy access to the start
    of the tree.
    """
    def __init__(self, nodes, root):
        self.nodes = nodes
        self.root = root

class TreeLeaf:
    """
    Leaf node of a Huffman tree. Stores the value.

    Should store an 8-bit integer to represent a single byte, or None
    to indicate the special "end of message" character.
    """
    def __init__ (self, value):
        self.value = value


class TreeBranch:
    """
    Simple representation of an internal node on a Huffman tree.
    Just stores the two children.
    """
    def __init__ (self, left, right):
        self.left = left
        self.right = right

def custom_min(trees):
    """ Takes a list of tuples called trees, finds the smallest 
    item and removes it from the list. Both the smallest item and
    new list are returned.

    Each item in trees is a tuple of (symbol, frequency)
    """

    if len(trees) == 0:
        raise ValueError("The list passed as input was empty.")

    # default to the first item
    min_item = trees[0]
    min_index = 0

    for i in range(len(trees)):
        # if this item has a smaller frequency
        if trees[i][1] < min_item[1]:
            min_item = trees[i]
            min_index = i

    del trees[min_index]

    return min_item[0], min_item[1], trees



def make_tree(freq_table):
    """
    Constructs and returns the Huffman tree from the given frequency table.
    """

    trees = []
    trees.append((TreeLeaf(None), 1))

    for (symbol, freq) in freq_table.items():
        trees.append((TreeLeaf(symbol), freq))

    while len(trees) > 1:
        right, rfreq, trees = custom_min(trees)
        left, lfreq, trees = custom_min(trees)
        trees.append((TreeBranch(left, right), lfreq+rfreq))

    root_node, _, _ = custom_min(trees)

    # store the nodes in the tree
    tree = Tree(trees, root_node)

    return tree


def make_encoding_table(huffman_tree):
    """
    Given a Huffman tree, will make the encoding table mapping each
    byte (leaf node) to its corresponding bit sequence in the tree.
    """
    table = {}

    def recurse(tree, path):
        """
        Traces out all paths in the Huffman tree and adds each
        corresponding leaf value and its associated path to the table.
        """
        if isinstance(tree, TreeLeaf):
            # note, if this is the special end message entry then
            # it stores table[None] = path
            table[tree.value] = path
        elif isinstance(tree, TreeBranch):
            # the trailing , has this properly interpreted as a tuple
            # and not just a single boolean value
            recurse(tree.left, path+(False,))
            recurse(tree.right, path+(True,))
        else:
            raise TypeError('{} is not a tree type'.format(type(tree)))

    recurse(huffman_tree, ())
    return table


def make_freq_table(stream):
    """
    Given an input stream, will construct a frequency table
    (i.e. mapping of each byte to the number of times it occurs in the stream).

    The frequency table is actually a dictionary.
    """

    # freqs = Counter()
    freq_dict = dict()
    buff = bytearray(512)
    while True:
        count = stream.readinto(buff)

        for b in buff:
            if b not in freq_dict:
                freq_dict[b] = 1
            else:
                freq_dict[b] += 1

        if count < len(buff): # end of stream
            break

    return freq_dict
