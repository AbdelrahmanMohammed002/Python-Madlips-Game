with open("story.txt", "r")as story_file:
    story = story_file.read()

missed_words = set()
start_of_word = -1

target_start= '['
target_end = ']'

for i, char, in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i+1]
        missed_words.add(word)
        start_of_word = -1


answers = {}

for word in missed_words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer


for word in missed_words:
    
    # replace function gives us a new string, not changing the old one
    story = story.replace(word, answers[word])

print(story)