'''
How to compile and run:
>> python3 Huffman.py
If you cannot use python3,
>> python2 Huffman.py

ABRACADABRA

make the encording tree ...
z1: [left: C, right: D]
z2: [left: B, right: R]
z3: [left: z1, right: z2]
z4: [left: A, right: z3]

The code for each letter
A: 0
C: 100
D: 101
B: 110
R: 111

ABRACADABRA is encoded as
01101110100010101101110

01101110100010101101110 is decoded as
ABRACADABRA
'''
import heapq


class Node:
    def __init__(self, char, freq=1):
        self.name = char
        self.left = None
        self.right = None
        self.freq = freq
        self.code = None

    # define the comparison operator
    def __eq__(self, other):
        return self.freq == other.freq

    def __lt__(self, other):
        if self.__eq__(other):
            return self.name < other.name

        return self.freq < other.freq


def MIN_PRIORITY_QUEUE(S):
    Q = []
    for k, v in S.items():
        heapq.heappush(Q, v)

    return Q


def HUFFMAN(S):
    n = len(S)
    Q = MIN_PRIORITY_QUEUE(S)

    for i in range(1, n):
        z = Node('z' + str(i))
        z.left = x = heapq.heappop(Q)
        z.right = y = heapq.heappop(Q)
        z.freq = x.freq + y.freq
        heapq.heappush(Q, z)
        print("{}: [left: {}, right: {}]".format(z.name, x.name, y.name))

    return heapq.heappop(Q)


def defcode(encoding_tree, code):
    # define and print code for each letter
    if encoding_tree.left is not None:
        defcode(encoding_tree.left, code + '0')

    if encoding_tree.right is not None:
        defcode(encoding_tree.right, code + '1')

    if (encoding_tree.left is None) and (encoding_tree.right is None):
        encoding_tree.code = code
        print("{}: {}".format(encoding_tree.name, code))
        return


def encode(letters):
    encoded = ""
    if type(letters) is str:
        for c in letters:
            encoded += S[c].code
    elif type(letters) is list:
        for c in letters:
            encoded += S[c[0]].code

    return encoded


def decode(encoding_tree, encoded):
    decoded = ""
    now = encoding_tree
    for i in encoded:
        if i == '0':
            now = now.left
        elif i == '1':
            now = now.right

        if (now.left is None) and (now.right is None):
            decoded += now.name
            now = encoding_tree

    return decoded


'''
example of letters:
Slide: "ABRACADABRA"
Probrem1: "ABBCACCEACBCCFABCDAFEABFFADBBC"
Problem2: [('A', 1), ('B', 1), ('C', 2), ('D', 3), ('E', 5), ('F', 8), ('G', 13), ('H', 21)]
Problem3: "Yuji Yanatori"
'''
letters = "ABRACADABRA"
print("{}\n".format(letters))

# word count
S = {}
if type(letters) is str:
    for i in letters:
        if i in S:
            S[i].freq += 1
        else:
            S[i] = Node(i)
elif type(letters) is list:  # this is for Problem2
    for i in letters:
        S[i[0]] = Node(i[0], i[1])

# make the encoding tree
print("make the encording tree ...")
encoding_tree = HUFFMAN(S)

# define the code for each letter
print("\nThe code for each letter")
defcode(encoding_tree, "")

if type(letters) is str:
    # encoding
    print("\n{} is encoded as".format(letters))
    encoded = encode(letters)
    print(encoded)

    # decoding
    decoded = decode(encoding_tree, encoded)
    if letters == decoded:
        print("\n{} is decoded as\n{}".format(encoded, decoded))
    else:
        print("\nFailed decoding")
