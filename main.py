# Programmers:  Leif LaBianca
# Course:  CS151, Professor Zee
# Due Date: November 21, 11:59
# Lab Assignment:  PA4
# Problem Statement:  read a file of news headlines and run a variety of diagnostics, then report back to user
# Data In: desired file, two search words
# Data Out:  quantity of search words within file, average headline word count and length, longest headline and shortest headline
# Credits: all original code
# Input Files: 2014.txt, 2015.txt, 2016.txt, 2017.txt, 2018.txt, 2019.txt

# Purpose:  unpacks headlines and runs diagnostics
# Parameters: filename
# Return: outputs all diagnostics
def work_file(filename):
    # defines diagnostics as empty values initially to edit later
    headline_lengths = []
    headline_word_count = []
    headline_count = 0
    avg_words = 0
    avg_characters = 0
    # opens user selected file and reads it
    file_data = open(f'{filename}.txt', 'r')
    # requests the user input two words they would like to search the headlines for
    word1 = input("\nWhat's a word you would like to search the headlines for: ")
    word2 = input("\nWhat's another word you would like to search the headlines for: ")
    print('\nWorking...\n')
    # creates a dictionary to keep track of the times each word appears
    user_word_dict = {word1: 0, word2: 0 }
    for headline in file_data:
        # resets word count after each loop
        word_count = 0
        # find and appaneds the length of the headline in characters
        headline_length = len(headline)
        headline_lengths.append(headline_length)
        # splits each headline by individual words
        headline_words = headline.split()
        for word in headline_words:
            # adds 1 to word count for each word
            word_count += 1
            # adds 1 to corresponding dictionary value if the word is found
            if word.lower() == word1.lower():
                user_word_dict[word1] += 1
            elif word.lower() == word2.lower():
                user_word_dict[word2] += 1
        # appends the word count of the specific headline
        headline_word_count.append(word_count)
    # defines total word count to derive average from later
    total_words = 0
    for number in headline_word_count:
        # adds 1 to the headline count for each number processed (equivalent to 1 headline)
        headline_count += 1
        # adds the counts of words present in the list
        total_words += int(number)
    # calculates the average word count
    avg_words = float(total_words / headline_count)
    total_characters = 0
    for number in headline_lengths:
        # adds each character count present in the list to total_chracters to calculate an average
        total_characters += int(number)
    # calculates the average character count
    avg_characters = float(total_characters / headline_count)
    # prints diagnostic results to user
    print(f"The word '{word1}' appears {user_word_dict[word1]} times.")
    print(f"The word '{word2}' appears {user_word_dict[word2]} times.")
    print(f"The average word count of the headlines is {avg_words}.")
    print(f"The average character count of the headlines is {avg_characters}.")
    print(f"The shortest headline is {min(headline_word_count)} words and {min(headline_lengths)} characters.")
    print(f"The longest headline is {max(headline_word_count)} words and {max(headline_lengths)} characters.\n")

# Purpose:  runs main function
# Parameters: none
# Return: outputs all diagnostics
def main():
    # sets loop condition
    passthru = False
    # prints intro message
    intro_line1 = "Welcome the the ABC headline reader!"
    intro_line2 = "Here, you can read every ABC headline from 2014 to 2019."
    intro_line3 = "This program also allows you to run various diagnostics on the sets of headlines."
    print("-" * 85)
    print(f"{intro_line1:^85}")
    print(f"{intro_line2:^85}")
    print(f"{intro_line3:^85}")
    print('-' * 85)
    print('')
    # the loop will continue until the user selects "no" at the end
    while not passthru:
        # sets error checking condition
        passthru2 = False
        while not passthru2:
            # requests user input the name of the file they want
            file_name = input('Enter the desired headline year in digits: ')
            if file_name.isdigit():
                if file_name == '2014' or file_name == '2015' or file_name == '2016' or file_name == '2017' or file_name == '2018' or file_name == '2019':
                    # runs the work_file function with the appropriate file name
                    work_file(file_name)
                    # allows loop to end
                    passthru2 = True
                else:
                    print('This year is not on hand. Select a year from 2014 to 2019\n')
            else:
                print('This input is invalid. Please express the year as a set of digits (2014, 2017)\n')
        # sets another error checking condition
        passthru3 = False
        while not passthru3:
            # asks the user whether they would like to run another diagnostic
            again_query = input('Would you like to run the program again?\nExpress your answer as Y or N: ')
            if again_query.lower() == 'n':
                # prints exist message
                print('Thank you for using the ABC headline reader!')
                # passes through loop
                passthru3 = True
                # passes through program, ends
                passthru = True
            elif again_query.lower() == 'y':
                print('Restarting...\n')
                # passes through loop
                passthru3 = True
            else:
                print('This input is invalid. Please express your answer as Y or N\n')

main()


