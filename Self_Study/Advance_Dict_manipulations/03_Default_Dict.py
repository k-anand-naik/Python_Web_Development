from collections import defaultdict

# Creating a defaultdict with int as the default factory
word_count = defaultdict(int)

# Counting the occurrences of each word
for word in ["apple", "banana", "apple", "cherry"]:
    word_count[word] += 1

# Converting defaultdict to a regular dictionary for printing
print(dict(word_count))  # Output: {'apple': 2, 'banana': 1, 'cherry': 1}



# List: Useful for grouping items.
# Creating a defaultdict with list as the default factory
group_by_first_letter = defaultdict(list)

# Grouping words by their first letter
for word in ["apple", "banana", "cherry", "avocado"]:
    group_by_first_letter[word[0]].append(word)

print(dict(group_by_first_letter))  
# Output: {'a': ['apple', 'avocado'], 'b': ['banana'], 'c': ['cherry']}


# Set: Useful for collecting unique items.
# Creating a defaultdict with set as the default factory
unique_groups = defaultdict(set)

# Adding items to groups based on some criteria
for item in [("apple", 1), ("banana", 2), ("apple", 3), ("banana", 1)]:
    unique_groups[item[0]].add(item[1])

print(dict(unique_groups))  
# Output: {'apple': {1, 3}, 'banana': {1, 2}}