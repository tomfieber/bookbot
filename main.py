#!/usr/bin/env python3

def main():
    book = "books/frankenstein.txt"
    with open(book, "r") as f:
        file_contents = f.read()
        total_words = len(file_contents.split())
        print(f"--- Begin report of {book} ---")
        print(f"{total_words} fount in the document\n")
        counts = count_characters(file_contents)
        print_report(counts)
        print(f"--- End report ---")

def count_characters(words:str):
    character_counts = {}
    words = words.lower()
    for w in words:
        if w not in character_counts:
            character_counts[w] = 1
        else:
            character_counts[w] += 1
    return character_counts

def print_report(book:dict):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for a in alphabet:
        print(f"The '{a}' character was found {book[a]} times")

if __name__ == "__main__":
    main()