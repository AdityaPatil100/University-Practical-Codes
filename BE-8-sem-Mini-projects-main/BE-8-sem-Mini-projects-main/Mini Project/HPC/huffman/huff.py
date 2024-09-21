import tkinter as tk
from tkinter import filedialog, messagebox
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

def write_details_to_file(input_file_length, compressed_file_length, huffman_codes, input_text):
    with open('file_details.txt', 'w') as file:
        file.write("Input text:")
        file.write(f"{input_text}\n")
        file.write(f"\nInput file length: {input_file_length}\n")
        file.write(f"Compressed file length: {compressed_file_length}\n")
        
        
        file.write("\nHuffman codes:\n")
        for char, code in huffman_codes.items():
            file.write(f"{char}: {code}\n")

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:
        input_file_entry.delete(0, tk.END)
        input_file_entry.insert(0, filename)

def compress_file():
    input_filename = input_file_entry.get()
    if not input_filename:
        messagebox.showerror("Error", "Please select an input file.")
        return

    with open(input_filename, 'r') as file:
        input_text = file.read()

    messagebox.showinfo("Input Text", f"Input Text:\n\n{input_text}")

    encoded_text, huffman_codes = huffman_encode(input_text)
    compressed_file_length = len(encoded_text)
    write_details_to_file(len(input_text), compressed_file_length, huffman_codes, input_text)
    messagebox.showinfo("Success", "File compressed and details saved to file_details.txt.")

# Create the main window
root = tk.Tk()
root.title("Huffman Encoding")

# Create widgets
input_file_label = tk.Label(root, text="Select Input File:")
input_file_entry = tk.Entry(root, width=50)
browse_button = tk.Button(root, text="Browse", command=browse_file)
compress_button = tk.Button(root, text="Compress File", command=compress_file)

# Place widgets in the window
input_file_label.grid(row=0, column=0, padx=10, pady=10)
input_file_entry.grid(row=0, column=1, padx=10, pady=10)
browse_button.grid(row=0, column=2, padx=10, pady=10)
compress_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Run the application
root.mainloop()
