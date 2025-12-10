def get_num_words(content):
    return len(content.split())

def get_char_frequency(content):
    frequencies = {}
    for c in content.lower():
        if c in frequencies:
            frequencies[c] += 1
        else:
            frequencies[c] = 1
    return frequencies

def sort_on(items):
    return items["num"]

def format_frequencies(frequency_dict):
    formatted_list = []
    for char, count in frequency_dict.items():
        formatted_list.append({
            "char": char,
            "num": count
        })
    formatted_list.sort(reverse=True, key=sort_on)
    return formatted_list