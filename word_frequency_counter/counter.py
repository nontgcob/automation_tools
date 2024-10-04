def count_word_frequencies(file_path):
    word_freq = {}
    
    with open(file_path, 'r') as file:
        text = file.read()
    
    words = text.lower().split()
    
    for word in words:
        # Remove punctuation from the word
        word = ''.join(char for char in word if char.isalnum())
        
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

def save_word_frequencies(word_freq, output_path):
    # Sort the word frequencies dictionary by frequency in descending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
    
    with open(output_path, 'w') as file:
        for word, freq in sorted_word_freq:
            file.write(f'{word}: {freq}\n')

# Specify the file paths
input_file_path = './word_frequency_counter/input.txt'
output_file_path = './word_frequency_counter/output.txt'

word_frequencies = count_word_frequencies(input_file_path)
save_word_frequencies(word_frequencies, output_file_path)

print(f'Word frequencies have been saved to {output_file_path}')