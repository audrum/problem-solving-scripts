# Taken from https://github.com/snietzsche/interview-prompts
# Write a Python script that converts a list into a dict, where the dict key for each item is the index number in the list.

# EXAMPLE: $ ./script.py
# Original List: [111, 'two', 333, 'four', {'five': 555}]
# New Dictionary: {0: 111, 1: 'two', 2: 333, 3: 'four', 4: {'five': 555}}

original_list = [111, 'two', 333, 'four', {'five': 555}]
new_dict = {i: original_list[i] for i in range(len(original_list))}
print("Original List: " + str(original_list))
print("New Dictionary: " + str(new_dict))