import pytest
from word_count import count_words_in_file, count_word_occurrences, print_words_counted, choose_file

def test_count_words_in_file():
    assert len(count_words_in_file('test_file.txt')) > 0

def test_count_word_occurrences():
    assert count_word_occurrences('test', ['test', 'file']) == 1

def test_print_word_counts(capsys):
    print_words_counted(['test', 'file'])
    captured = capsys.readouterr()
    assert 'test: 1' in captured.out

def test_select_file(monkeypatch):
    def mock_askopenfilename():
        return 'test_file.txt'
    monkeypatch.setattr('tkinter.filedialog.askopenfilename', mock_askopenfilename)
    assert choose_file() == 'test_file.txt'
