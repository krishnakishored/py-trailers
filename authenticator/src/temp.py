from typing import List


# Implement a function to count the frequency of each word
# return the dictionary of word frequency
def word_count(paragraph: List[str]):
    word_freq = {}
    for line in paragraph:
        for word in line.split():
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    return word_freq


# Implement a function to sort the list of people based on the key_name
# return the sorted list
def sortTheList(list_of_people: List[dict], key_name: str):
    return sorted(list_of_people, key=lambda x: x[key_name])


# sortedArray(list, key_name)

# key_name = "age"
# Output - Ram, Gita, Sam, Sita

# key_name = "name"
# Output - Gita, Ram, Sam, Sita

if __name__ == "__main__":
    # list of sententences
    paragraph = [
        "the quick brown fox jumps over the lazy dog",
        "All is well that ends well",
        "the quick brown fox jumps over the lazy dog",
    ]
    # paragraph = "the quick brown fox jumps over the lazy dog"
    print(word_count(paragraph))

    list_of_characters = [
        {"name": "Ram", "age": 20},
        {"name": "Sam", "age": 25},
        {"name": "Sita", "age": 27},
        {"name": "Gita", "age": 22},
    ]
    print(sortTheList(list_of_characters, "name"))
    print(sortTheList(list_of_characters, "age"))
