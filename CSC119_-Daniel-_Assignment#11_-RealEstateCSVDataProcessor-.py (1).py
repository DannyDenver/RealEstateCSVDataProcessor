
# coding: utf-8

# In[ ]:

import csv
import sys


def main():
    
    
    
    """
    The top-level function that orchestrates the analysis of a comma-separated-values (CSV) file
    """

    # constants
    PROGRAM_NAME = 'Real Estate CSV Data Processor'
    CSV_DATA_FILENAME = 'SacramentoResidentialRealEstateTransactions2008.csv'
    MENU = '\n[L]oad data file\n[P] find hi/lo priced\n[A]verage all properties\n[C]ondo averages\n[Q]uit\nChoice:\t'
    CHOICES = 'LPACQ'

    # print the header
    print_header(PROGRAM_NAME)

    # read in the data set from the CSV file
    data_set = read_data_file(CSV_DATA_FILENAME)

    # main driving loop for this program
    while True:
        # ask the user what they want to do
        choice = menu(MENU, CHOICES)

        # TODO add other options
        # [A]verage price of all properties
        if choice == 'A':
            avg_price = get_average_price(data_set)
            # see formatting tutorial at:
            # http://learnpythontutorial.com/advanced-string-formatting-in-python/
            print('\n***** Average Property price: ${:,} *****'.format(avg_price))
        if choice=="L":
            read_data_file(data_set)
        if choice=="P":
            high_low = find_high_and_low(data_set)
            # see formatting tutorial at:
            # http://learnpythontutorial.com/advanced-string-formatting-in-python/
            
            print('\n***** Low price: ${:,} *****'.format(high_low[1]))
            print('\n***** High price: ${:,} *****'.format(high_low[0]))
            
        if choice=="C":
            condo = find_condo_average(data_set)
            # see formatting tutorial at:
            # http://learnpythontutorial.com/advanced-string-formatting-in-python/
            print('\n***** Average Condo price: ${:,} *****'.format(condo))
            
            
            
            

        # [Q]uit the program
        elif choice == 'Q':
            print('\n***** Exiting *****')
            break
        


def print_header(program_name, width=60):
    """
    Print out a text header with the name centered.

    :param program_name:  The string to center in the title
    :param width:  The width of the header
    """

    line = '-' * width
    print()
    print(line)
    # great formatting examples: https://pyformat.info/#string_pad_align
    print('{:^{}s}'.format(program_name, width))
    print(line)
    print()


def get_average_price(data_set, key='price'):
    """
    Average the prices for all properties in the data set

    :param data_set: A list of dictionaries with price data
    :param key: The key to retrieve the price data from the dictionary

    :return: The average price of all properties in the data set as an int
    """
    total, counter = 0, 0
    for row in data_set:
        total += int(row[key])
        counter += 1
    return total // counter


def find_high_and_low(data_set,key='price'):
    
        maximum=None
        minimum=None
        value=0
        for row in data_set:
            value=int(row[key])
            if maximum == None or maximum<value:
                maximum=value
            if minimum==None or minimum>value:
                minimum=value
        return maximum, minimum
    
def find_condo_average(data_set, key='home_type', key2='price'):
    
    sum=0
    counter=0
    for row in data_set:
        if row[key]== "Condo":
            sum+= int(row[key2])
            counter+=1
    return sum //counter



def read_data_file(csv_file):
    
    
    """
    Read in the data contained in the comma-separated-values (CSV) file,
    creating a dictionary for every row that is keyed by the column header
    names, and append the dictionaries to a list.

    :param csv_file: A comma-separated-values (CSV) file with the column
                     headers in the first line

    :return: The list of dictionaries containing data values keyed to the CSV column headers
    """

    # note: Doug Hellmann is a Python expert and the author of the PyMOTW web site.
    #       He recommends putting the try / except / finally all in one scope as I do below.
    #       This approach differs from what is recommended by our text.
    #
    #       See: https://doughellmann.com/blog/2009/06/19/python-exception-handling-techniques/

    data = []
    infile = None
    print('CSV File:', csv_file, '\n')
    try:
        infile = open(csv_file, 'r', encoding='utf-8')
        reader = csv.DictReader(infile)
        for row in reader:
            data.append(row)
        return data

    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)

    finally:
        infile.close()



def menu(formatted_menu, choices):
    """
    Presents a set of choices to the user, gets the user choice,
    validates it, and if it is valid, returns it to the caller.
    If the user's choice is invalid, they will be requested to
    enter an additional choice, until a valid one is obtained.

    :param formatted_menu:  The text-menu to be presented to the user
    :param choices: The list of valid choices

    :return: The validated user's choice as a single upper-case character.
    """
    user_input = ''
    while True:
        # get the user input and convert it to uppercase
        user_input = input(formatted_menu).upper()
        if user_input in choices:
            break
    return user_input


# don't run this program when it is being imported into another module
if __name__ == '__main__':
    main()


# In[ ]:



