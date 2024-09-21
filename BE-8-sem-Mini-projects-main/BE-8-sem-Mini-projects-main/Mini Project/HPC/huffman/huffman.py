import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_counter = Counter(text)
    pq = [HuffmanNode(char, freq) for char, freq in freq_counter.items()]
    heapq.heapify(pq)

    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(pq, merged)

    return pq[0]

def build_huffman_codes(node, current_code="", huffman_codes={}):
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = current_code

    build_huffman_codes(node.left, current_code + "0", huffman_codes)
    build_huffman_codes(node.right, current_code + "1", huffman_codes)

    return huffman_codes

def huffman_encode(text):
    if len(text) == 0:
        return "", {}

    root = build_huffman_tree(text)
    huffman_codes = build_huffman_codes(root)

    encoded_text = ''.join(huffman_codes[char] for char in text)
    return encoded_text, huffman_codes

def calculate_file_length(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return len(content)

def write_encoded_text(encoded_text, output_filename):
    with open(output_filename, 'w') as file:
        file.write(encoded_text)

# Generate input text
input_text = "Jay Maharashtra"

# Encode input text
encoded_text, huffman_codes = huffman_encode(input_text)

# Calculate file lengths
input_file_length = len(input_text)
compressed_file_length = len(encoded_text)

# Write details to text file
with open('file_details.txt', 'w') as file:
    file.write(f"input_text: {input_text}\n")
    file.write(f"Input file length: {input_file_length}\n")
    file.write(f"Compressed file length: {compressed_file_length}\n")
    file.write("Huffman codes:\n")
    for char, code in huffman_codes.items():
        file.write(f"{char}: {code}\n")
