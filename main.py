book_path = "books/frankenstein.txt"


def read_book(book_path):
    with open(book_path) as f:
        book = f.read()
        return book


def count_words(book):
    words = book.split()
    return len(words)


def count_chars(book):
    characters = {}
    for char in book:
        letter = char.lower()
        if letter in characters:
            characters[letter] = characters[letter] + 1
        else:
            characters[letter] = 1

    return characters


def sort_on(dict):
    return dict["value"]


def sort_chars_count(chars_count):
    chars_count_list = [
        {"name": key, "value": chars_count[key]} for key in chars_count if key.isalpha()
    ]
    chars_count_list.sort(reverse=True, key=sort_on)
    return chars_count_list


def generate_report(book_path):
    book = read_book(book_path)
    word_count = count_words(book)
    chars_count = count_chars(book)
    chars_count_sorted = sort_chars_count(chars_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for entry in chars_count_sorted:
        name = entry["name"]
        value = entry["value"]
        print(f"The '{name}' character was found {value} times")


if __name__ == "__main__":
    generate_report(book_path)
