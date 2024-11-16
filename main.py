def work_file(filename):
    file_data = open(f'{filename}.txt', 'r')


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
                if file_name == 2014 or file_name == 2015 or file_name == 2016 or file_name == 2017 or file_name == 2018 or file_name = 2019
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


