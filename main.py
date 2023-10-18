from timeit import default_timer as timer
import random
from termcolor import colored, cprint
from sys import argv
import csv
from os import get_terminal_size

usage = '''
Usage: python3 typing_speed_tester.py [options] [wordlist_type]
    options:
            -h, --help: prints this message and quits.
            -n {integer}: number of words to test, default=10.
    wordlist_type:
            -t100, --top100: top 100 English words, default.
            -t500, --top500: top 500 English words.
            -pr, --programming: top 100 programming terms.
'''

def main():
    n = 10
    list_type = 'top100.csv'
    if len(argv) > 1:
        if argv[1] == '-h' or argv[1] == '--help':
            print(usage)
            return
        elif argv[1] == '-n':
            try:
                n = int(argv[2])
                if n <= 0 or n > 100:
                    raise Exception
            except:
                print('Please provide correct number after -n')
                print('It should be between 1 and 100.')
                return
        if len(argv) == 4:
            if argv[3] == '-t100' or argv[3] == '--top100':
                list_type = 'top100.csv'
            elif argv[3] == '-t500' or argv[3] == '--top500':
                list_type = 'top500.csv'
            elif argv[3] == '-pr' or argv[3] == '--programming':
                list_type = 'programming100.csv'
            else:
                print('Please choose  right wordlist type, use -h for help.')
                return

    words = generate_words(n, list_type)
    terminal_columns = get_terminal_size().columns
    print('-' * terminal_columns)
    for i in words:
        cprint(i, 'cyan', end=' ')
    print()
    print('-' * terminal_columns)

    try:
        input('Press Enter when ready')
    except KeyboardInterrupt:
        print()
        print('quit')
        return
    start_time = timer()
    try:
        text = input('Type every word seperated by space and ' + colored('press Enter', 'green') + ' when you finish\n' + '-' * 30 + '\n')
    except KeyboardInterrupt:
        print()
        print('quit')
        return
    end_time = timer()
    time = round(end_time - start_time, 2)
    typed_words = list(text.split(' '))
    print('-' * 30)
    wpm = calculate_average_speed(len(typed_words), time)
    acc = calculate_accuracy(words, typed_words)
    print(f'Speed: {wpm} words per minute.')
    print(f'Accuracy: {acc}%.')


def calculate_accuracy(test_words: list, typed_words: list) -> float:
    letters = 0
    errors = 0
    typed_words_len = len(typed_words)
    test_words_len = len(test_words)

    if typed_words_len > test_words_len:
        n = test_words_len - typed_words_len
        del typed_words[n:]
        typed_words_len = test_words_len

    for i in range(typed_words_len):
        test_current_word_len = len(test_words[i])
        type_current_word_len = len(typed_words[i])

        letters += test_current_word_len
        if typed_words[i] == test_words[i]:
            continue
        else:
            if type_current_word_len > test_current_word_len:
                errors += type_current_word_len - test_current_word_len
                continue
            for j in range(type_current_word_len):
                try:
                    if typed_words[i][j] != test_words[i][j]:
                        errors += 1
                except:
                    pass
    accuracy = (letters - errors) * 100
    accuracy /= letters
        
    return round(accuracy, 2)


def calculate_average_speed(words: int, time: float) -> float:
    # wpm
    words_per_second = words / time
    wpm = words_per_second * 60
    return round(wpm)

def generate_words(length: int, list_type: str) -> list:
    with open(list_type, 'r') as f:
        reader = csv.reader(f)
        wordlist = [row[0] for row in reader]

    words = []
    for _ in range(length):
        i = random.randint(0, len(wordlist) - 1)
        words.append(wordlist[i])

    return words



if __name__ == "__main__":
    main()
