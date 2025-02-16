import tkinter as tk
from tkinter import filedialog

def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read().lower().split()
            return text
    except FileNotFoundError:
        return 'File not found.'

def count_word_occurrences(word, word_list):
    return word_list.count(word)

def print_words_counted(word_list):
    word_counts = {}
    for word in word_list:
        word_counts[word] = count_word_occurrences(word, word_list)
    for word, count in word_counts.items():
        print(f'{word}: {count}')

def choose_file():
    root = tk.Tk()
    root.withdraw()
    file_name = filedialog.askopenfilename()
    return file_name

def main():
    file_name = choose_file()
    if file_name:
        word_list = count_words_in_file(file_name)
        if isinstance(word_list, list):
            print_words_counted(word_list)
        else:
            print(word_list)
    else:
        print('No file selected.')

if __name__ == '__main__':
    main()


