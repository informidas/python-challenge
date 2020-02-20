# import modules
import os, csv, re

letter_count = 0.0
avg_letter_count = 0.0
avg_sentence_len = 0.0

#declare a list array for the tokenized paragraph
tokenized_paragraph = []

#declare a list array for the tokenized sentences
sentence_len = []

#declare a string variable for the clean paragraph
clean_paragraph = ""

# set path for source file
srcpath = os.path.join("data", "paragraph.txt")

# open source files as readonly, and instantiate a reader object
with open(srcpath, 'r', newline='') as txtfile:
  for sentences in txtfile:
    #load the sentences into the clean_paragraph String
    clean_paragraph = sentences

# once we have paragraph loaded as text, determine the number of words per sentence
# initialize a counter for each character in the clean text string
l = 0

# initialize a counter for numbe rof words
w = 1 
# loop through the clean_paragraph string letter by letter
for l in range(len(clean_paragraph)):

  if clean_paragraph[l] == " ":

    # if we hit a space then we found another word so add 1 to the word count total
    w += 1

  elif clean_paragraph[l] == ".":
    
    # we hit a period then it means the sentence is done, so append the word count total to a sentence_len list array
    sentence_len.append(int(w))
    
    # reset the wordc count 
    w = 0

# use the regular expressions module to tokenize the paragraph into an array of words
tokenized_paragraph = re.split(r'\s', clean_paragraph)

for word in tokenized_paragraph:
  letter_count += len(word)

# create and set variables needed for stats in results summary
approx_word_count = len(tokenized_paragraph)
approx_sentence_count = clean_paragraph.count(".")
avg_letter_count = format((letter_count / len(tokenized_paragraph)),".2f")
avg_sentence_len = format(sum(sentence_len) / len(sentence_len), ".1f")

# Print Results
print("Paragraph Analysis")
print("--" * 9)
print(f"Approximate Word Count: {approx_word_count}")
print(f"Approximate Sentence Count: {approx_sentence_count}")
print(f"Average Letter Count: {avg_letter_count}")
print(f"Average Sentence Count: {avg_sentence_len} ")