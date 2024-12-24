from collections import Counter, List

# Example with a list
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# create counter with a dictionary
counter = Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(counter)  # Output: Counter({'apple': 3, 'banana': 2})


# Use most_common to get the n most common elements.
print(counter.most_common(2))  # Output: [('apple', 3), ('banana', 1)]


# Your Counter
pattern_cnt = Counter({
    ('home', 'about', 'career'): 2,
    ('home', 'cart', 'maps'): 1,
    ('cart', 'maps', 'home'): 1,
    ('home', 'cart', 'home'): 1,
    ('home', 'maps', 'home'): 1
})

# Get the most common key
most_common_key = pattern_cnt.most_common(1)[0][0]

print(most_common_key)  # Output: ('home', 'about', 'career')