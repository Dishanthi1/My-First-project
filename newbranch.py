from collections import Counter


def count_words(filename, n):
	with open(filename, 'r') as file:
		text = file.read()
		words = text.split()
		word_count = Counter(words)

		# Get the top N words
		top_words = word_count.most_common(n)

		return top_words


# Input the filename and the number of top words you want to display
filename = "sample.txt"  # Change this to the path of your text file
top_n = 10  # Change this to the number of top words you want

result = count_words(filename, top_n)

print(f"Top {top_n} words in the file '{filename}':")
for word, count in result:
	print(f"{word}: {count}")
