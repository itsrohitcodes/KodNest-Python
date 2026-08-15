# Normalize and Process a sentence

# Read the sentence
sentence = input()

# Clean and normalize the sentence
clean_sentence = sentence.strip()
lower_sentence = clean_sentence.lower()

# Split the sentence and create the slug
normal_sentence = lower_sentence.replace('.', "")
split_sentence = normal_sentence.split()

# Produce the uppercase form and search result
join_sentence = "-".join(split_sentence)
upper_sentence = normal_sentence.upper()

# Search for the word "python"
search_result = normal_sentence.find("python")

# Display all processed values
print(f"Cleaned: {clean_sentence}")
print(f"Normalized: {normal_sentence}")
print(f"Words: {split_sentence}")
print(f"Slug: {join_sentence}")
print(f"Uppercase: {upper_sentence}")
print(f"Python Position: {search_result}")