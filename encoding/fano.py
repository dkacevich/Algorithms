class FanoCoding:
    def __init__(self):
        self.codes = {}
    
    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if not character in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def sort_frequency(self, frequency):
        return sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    def fano_coding(self, sorted_freq, prefix=''):
        if len(sorted_freq) == 0:
            return
        if len(sorted_freq) == 1:
            self.codes[sorted_freq[0][0]] = prefix
            return
        total_freq = sum([freq for char, freq in sorted_freq])
        cumulative_freq = 0
        split_point = 0

        for i, (char, freq) in enumerate(sorted_freq):
            if cumulative_freq + freq > total_freq / 2:
                break
            cumulative_freq += freq
            split_point = i

        self.fano_coding(sorted_freq[:split_point + 1], prefix + '1')
        self.fano_coding(sorted_freq[split_point + 1:], prefix + '0')

    def encode(self, text):
        frequency = self.make_frequency_dict(text)
        sorted_freq = self.sort_frequency(frequency)
        self.fano_coding(sorted_freq)

        encoded_text = ''
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def decode(self, encoded_text):
        reverse_mapping = {v: k for k, v in self.codes.items()}
        current_code = ''
        decoded_text = ''

        for bit in encoded_text:
            current_code += bit
            if current_code in reverse_mapping:
                decoded_text += reverse_mapping[current_code]
                current_code = ''

        return decoded_text

# Test Fano Coding
fano_coding = FanoCoding()

text = input("Text: ")
encoded_text = fano_coding.encode(text)
decoded_text = fano_coding.decode(encoded_text)


original_size = len(text) * 8 # 8 bits per char
encoded_size = len(encoded_text)  # each char is a bit

saving = (original_size - encoded_size) / 8 # convert bits to bytes


print(encoded_text)
print(f"Size saving: {saving} bytes")