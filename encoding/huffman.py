import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Node):
            return False
        return self.freq == other.freq


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency
    

    def build_heap(self, frequency):
        for key in frequency:
            node = Node(key, frequency[key])
            heapq.heappush(self.heap, node)
            
            

    def merge_nodes(self):
        while(len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)
    

    def make_codes_function(self, root, current_code):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char

        self.make_codes_function(root.left, current_code + "1")
        self.make_codes_function(root.right, current_code + "0")

    def make_codes(self):
        root = self.heap[0]
        current_code = ""
        self.make_codes_function(root, current_code)

    def huffman_encoding(self, text):
        frequency = self.make_frequency_dict(text)
        self.build_heap(frequency)
        self.merge_nodes()
        self.make_codes()

        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]

        return encoded_text



    def huffman_decoding(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text



huffman_coding = HuffmanCoding()


text = input("Text: ")

encoded_text = huffman_coding.huffman_encoding(text)
decoded_text = huffman_coding.huffman_decoding(encoded_text)


original_size = len(text) * 8 # 8 bits per char
encoded_size = len(encoded_text)  # each char is a bit

saving = (original_size - encoded_size) / 8 # convert bits to bytes


print(encoded_text)
print(f"Size saving: {saving} bytes")
