from itertools import count


def work_file(filename):
    headline_lengths = []
    headline_word_count = []
    headline_count = 0
    avg_words = 0
    avg_characters = 0
    file_data = open(f'{filename}.txt', 'r')
    word1 = input("\nWhat's a word you would like to search the headlines for: ")
    word2 = input("\nWhat's another word you would like to search the headlines for: ")
    print('\nWorking...\n')
    user_word_dict = {word1: 0, word2: 0 }
    for headline in file_data:
        word_count = 0
        headline_length = len(headline)
        headline_lengths.append(headline_length)
        headline_words = headline.split()
        for word in headline_words:
            word_count += 1
            if word.lower() == word1.lower():
                user_word_dict[word1] += 1
            elif word.lower() == word2.lower():
                user_word_dict[word2] += 1
        headline_word_count.append(word_count)
    total_words = 0
    for number in headline_word_count:
        headline_count += 1
        total_words += int(number)
    avg_words = float(total_words / headline_count)
    total_characters = 0
    for number in headline_lengths:
        total_characters += int(number)
    avg_characters = float(total_characters / headline_count)
    print(f"The word '{word1}' appears {user_word_dict[word1]} times.")
    print(f"The word '{word2}' appears {user_word_dict[word2]} times.")
    print(f"The average word count of the headlines is {avg_words}.")
    print(f"The average character count of the headlines is {avg_characters}.")
    print(f"The shortest headline is {min(headline_word_count)} words and {min(headline_lengths)} characters.")
    print(f"The longest headline is {max(headline_word_count)} words and {max(headline_lengths)} characters.\n")


def main():
    passthru = False
    intro_line1 = "Welcome the the ABC headline reader!"
    intro_line2 = "Here, you can read every ABC headline from 2014 to 2019."
    intro_line3 = "This program also allows you to run various diagnostics on the sets of headlines."
    print("-" * 85)
    print(f"{intro_line1:^85}")
    print(f"{intro_line2:^85}")
    print(f"{intro_line3:^85}")
    print('-' * 85)
    print('')
    while not passthru:
        passthru2 = False
        while not passthru2:
            file_name = input('Enter the desired headline year in digits: ')
            if file_name.isdigit():
                if file_name == '2014' or file_name == '2015' or file_name == '2016' or file_name == '2017' or file_name == '2018' or file_name == '2019':
                    work_file(file_name)
                    passthru2 = True
                else:
                    print('This year is not on hand. Select a year from 2014 to 2019\n')
            else:
                print('This input is invalid. Please express the year as a set of digits (2014, 2017)\n')
        passthru3 = False
        while not passthru3:
            again_query = input('Would you like to run the program again?\nExpress your answer as Y or N: ')
            if again_query.lower() == 'n':
                print('Thank you for using the ABC headline reader!')
                passthru3 = True
                passthru = True
            elif again_query.lower() == 'y':
                print('Restarting...\n')
                passthru3 = True
            else:
                print('This input is invalid. Please express your answer as Y or N\n')

main()


