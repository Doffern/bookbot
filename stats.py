def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def char_counts(text):
    char_counts_amount = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in char_counts_amount:
                char_counts_amount[char] += 1
            else:
                char_counts_amount[char] = 1
    return char_counts_amount

def sort_on(items):
    return items["num"]

def char_counts_sorted(char_counts_dict):
    items = list(char_counts_dict.items())
    items.sort(reverse=True, key=lambda item:item[1])

    
    return items
