import re

text = input()

paragraphs = 1 if text.strip() else 0

sentences = len(re.findall(r"[.!?]", text))
if sentences == 0 and text.strip():
    sentences = 1

words = re.findall(r"\b[a-zA-Z]+\b", text)

total_words = len(words)
total_letters = sum(len(word) for word in words)

avg_word_length = round(total_letters / total_words, 2) if total_words else 0
avg_sentence_length = round(total_words / sentences, 2) if sentences else 0

print("Words:", total_words)
print("Sentences:", sentences)
print("Paragraphs:", paragraphs)
print("Average Word Length:", avg_word_length)
print("Average Sentence Length:", avg_sentence_length)