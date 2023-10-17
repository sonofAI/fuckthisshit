from timeit import default_timer as timer
import random
from termcolor import colored, cprint

usage = 

def main():
    if len(argv) > 1:
        if argv[1] == '-h' or argv[1] == '--help':
            print('Usage: python3 typing_speed_tester.py [options]')
            print()



    words = generate_words(10)
    for i in words:
        cprint(i, 'red', end=' ')
    print()

    wait = input('Press Enter when ready')
    start_time = timer()
    text = input('Type every word seperated by space and ' + colored('press Enter', 'green') + ' when you finish\n' + '-' * 30 + '\n')
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

    for i in range(len(typed_words)):
        letters += len(test_words[i])
        if typed_words[i] == test_words[i]:
            continue
        else:
            if len(typed_words[i]) > len(test_words[i]):
                errors += len(typed_words[i]) - len(test_words[i])
                continue
            for j in range(len(typed_words[i])):
                try:
                    if typed_words[i][j] != test_words[i][j]:
                        errors += 1
                except Exception as e:
                    print(e)

    accuracy = (letters - errors) * 100
    accuracy /= letters
        
    return round(accuracy, 2)


def calculate_average_speed(words: int, time: float) -> float:
    # wpm
    words_per_second = words / time
    wpm = words_per_second * 60
    return round(wpm)

def generate_words(length: int, list_type: str) -> list:
    wordlist = ['print', 'shit', 'lol', 'physics', 'table', 'fools', 'hate']

    words = []
    for _ in range(length):
        i = random.randint(0, len(wordlist) - 1)
        words.append(wordlist[i])

    return words



if __name__ == "__main__":
    main()
