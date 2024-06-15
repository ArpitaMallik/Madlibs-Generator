with open("story.txt", "r") as f:
    story = f.read()

words = []
start_of_word = -1

target_start = "<"
target_end = ">"

# Extract the placeholders
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    elif char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        if word not in words:
            words.append(word)
        start_of_word = -1

# Collect user inputs
answers = {}
for i in words:
    answer = input(f"Enter a word for {i}: ")
    answers[i] = answer

# Replace placeholders
for word in words:
    story = story.replace(word, answers[word])

print(story)
