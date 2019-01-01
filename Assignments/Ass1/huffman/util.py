import bitio
import huffman
import pickle


def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream o read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    '''
    tree = pickle.load(tree_stream)    
    return tree                # load the huffmantree from the given file
    

def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """
    a = tree.root
    while True:
        bit = bitreader.readbit()     #go throuth the tree and get the designated value of each character
        if bit:
            a = a.right    #if its true go tothe next node on right
        else:          
            a = a.left     
        if isinstance(a, huffman.TreeLeaf):    #when it reaches the treeleaf, return the value
            return a.value
 

def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'tree_stream' using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''
    tree = read_tree(compressed)
    r = bitio.BitReader(compressed)
    w = bitio.BitWriter(uncompressed)
    
    
    while True:
        Byte = decode_byte(tree,r)
        if Byte != None:          # write the decopressed code to output before EOF
            w.writebits(Byte,8)
        else:
            break
        
    pass
def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''
    pickle.dump(tree, tree_stream)  #save the tree stream
    pass
def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'tree_stream' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
      tree_stream: A file stream where the tree data should be dumped.
      
    '''
    maketable = huffman.make_encoding_table(tree.root)
    write_tree(tree, compressed)
    write_bit = bitio.Bitwriter(compressed)
    read_bit = bitio.BitReader(uncompressed)
    while True:
        try:
            byte = read_bit.readbits(8)  #read byte by byte 
            for t in table[byte]:
                write_bit.writebit(t)   
        except:                           # break when it reaches the end
            break
    compressed.close()
    uncompressed.close()
    pass