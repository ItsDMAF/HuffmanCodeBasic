import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left, merged_node.right = left, right

        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}

    if node.char is not None:
        mapping[node.char] = code
    if node.left is not None:
        build_huffman_codes(node.left, code + "0", mapping)
    if node.right is not None:
        build_huffman_codes(node.right, code + "1", mapping)

    return mapping

def encode_text(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

def decode_text(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree

    return decoded_text

def main():
    input_file_path = 'input.txt'
    encoded_file_path = 'encode.txt'
    decoded_file_path = 'decode.txt'

    with open(input_file_path, 'r') as file:
        original_text = file.read()

    huffman_tree = build_huffman_tree(original_text)
    huffman_codes = build_huffman_codes(huffman_tree)

    encoded_text = encode_text(original_text, huffman_codes)

    with open(encoded_file_path, 'w') as file:
        file.write(encoded_text)

    decoded_text = decode_text(encoded_text, huffman_tree)

    with open(decoded_file_path, 'w') as file:
        file.write(decoded_text)

if __name__ == "__main__":
    main()