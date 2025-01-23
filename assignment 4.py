"""
Author : Furqaan Mohammed
Student Number: 752879
Revison date : 20 December 2024
Program : Reading files and searching for data
Description : Reads Wordle data from a file and allows the user to search for specific words or dates. 
VARIABLE DICTIONARY :
    file_name: str - Name of the file containing Wordle data
    file_handle: file object - File handle for reading the Wordle data file
    file_lines: list - List of lines read from the file
    word_list: list - List to store words from the file
    date_list: list - List to store dates from the file
    current_line: str - A single line read from the file
    month_str: str - Month component of the date
    day_str: str - Day component of the date
    year_str: str - Year component of the date
    puzzle_word: str - Word from the file
    combined_date: int - Merged date in integer format
    first_date: int - The earliest date in the date list
    last_date: int - The latest date in the date list
    original_date_list: list - Copy of the date list to maintain original order
    original_word_list: list - Copy of the word list to maintain original order
    input_valid: bool - Flag to validate user input
    search_option: str - User's choice for search option
    word_input: str - User's input word for search
    matching_date: int - Date corresponding to the user's input word
    year_input: str - User's input year for date search
    month_input: str - User's input month for date search
    day_input: str - User's input day for date search
"""
"""
 Function to perform merge sort on two arrays
 Parameters:
   array (list): The main array to be sorted.
   array2 (list): A secondary array that gets rearranged to match the sorting of the main array.
   left (int): The starting index of the subarray to be sorted.
   right (int): The ending index of the subarray to be sorted.
"""
def mergeSort(array, array2, left, right):
    # Base condition to stop recursion when subarray has only one element
    if left < right:
        # Calculate the middle index to divide the array
        middle = left + (right - left) // 2
        # Recursively sort the left half
        mergeSort(array, array2, left, middle)
        # Recursively sort the right half
        mergeSort(array, array2, middle + 1, right)
        # Merge the two sorted halves
        mergeSortMerge(array, array2, left, middle, right)
"""
 Function to merge two sorted subarrays
 Parameters:
   array, array2 (list): Arrays being sorted.
   left (int): Left index of the subarray.
   middle (int): Middle index dividing the subarray.
   right (int): Right index of the subarray.
"""
def mergeSortMerge(array, array2, left, middle, right):
    # Sizes of two subarrays to be merged
    n1 = middle - left + 1
    n2 = right - middle
    # Temporary arrays for the left and right halves
    L = [0] * n1
    R = [0] * n2
    L2 = [0] * n1
    R2 = [0] * n2
    # Copy data to temporary arrays
    for i in range(n1):
        L[i] = array[left + i]
        L2[i] = array2[left + i]
    for j in range(n2):
        R[j] = array[middle + 1 + j]
        R2[j] = array2[middle + 1 + j]
    # Initial indices for merging
    i = j = 0
    k = left
    # Merge the temporary arrays back into the original arrays
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            array2[k] = L2[i]
            i += 1
        else:
            array[k] = R[j]
            array2[k] = R2[j]
            j += 1
        k += 1
    # Copy any remaining elements of the left subarray
    while i < n1:
        array[k] = L[i]
        array2[k] = L2[i]
        i += 1
        k += 1
    # Copy any remaining elements of the right subarray
    while j < n2:
        array[k] = R[j]
        array2[k] = R2[j]
        j += 1
        k += 1
"""
 Function to merge year, month, and day into a single numerical date
 Parameters:
   year (str): The year as a string.
   month (str): The three-letter month abbreviation.
   day (str): The day as a string.
 Returns:
   int: Combined date as an integer in the format YYYYMMDD.
"""
def merge(year, month, day):
    try:
        months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        merged_date = year
        month_str = ""
        for i in range(len(months)):
            if months[i] == month.lower():
                month_str += str(i + 1)
                if len(month_str) == 1:
                    month_str = "0" + month_str
        merged_date += month_str
        merged_date += day
        return int(merged_date)
    except:
        return 0
"""
 Function to check if an item exists in one sorted array and retrieve the corresponding value from another array
 Parameters:
   item: The item to search for.
   sorted_array1 (list): The sorted array to search within.
   sorted_array2 (list): The array with corresponding values.
 Returns:
   The corresponding value if the item is found, or 0 if not found.
"""
def isMatch(item, sorted_array1, sorted_array2):
    index = binarySearch(sorted_array1, item)
    if index != -1:
        return sorted_array2[index]
    return 0
"""
 Function to perform binary search on an array
 Parameters:
   array (list): The sorted array to search.
   item: The item to search for.
 Returns:
   int: Index of the item if found, -1 otherwise.
"""
def binarySearch(array, item):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Open and read the file containing Wordle data
file_name = "wordle.dat"
file_handle = open(file_name, "r")
file_lines = file_handle.readlines()
for i in range(len(file_lines)):
    file_lines[i] = file_lines[i].strip()

# Parse the file lines into word and date lists
word_list = []
date_list = []
for current_line in file_lines:
    month_str, day_str, year_str, puzzle_word = current_line.split()
    combined_date = merge(year_str, month_str, day_str)
    date_list.append(combined_date)
    word_list.append(puzzle_word)

# Backup the original data
first_date = date_list[0]
last_date = date_list[-1]
original_date_list = date_list.copy()
original_word_list = word_list.copy()
# Sort the data using merge sort
mergeSort(word_list, date_list, 0, len(word_list) - 1)

# Wordle database interface
print("Welcome to the Wordle Database!")
input_valid = False
search_option = ""
while not input_valid:
    search_option = input("Enter w if you are looking for a word, or d for a word on a certain date: ")
    if search_option.lower() == "w" or search_option.lower() == "d":
        input_valid = True

# Search for a word
if search_option == "w":
    input_valid = False
    while not input_valid:
        word_input = input("What word are you looking for? ").upper()
        if len(word_input) == 5:
            input_valid = True
    matching_date = isMatch(word_input, word_list, date_list)
    if matching_date:
        print("The word %s was the solution to the puzzle on %d." % (word_input, matching_date))
    else:
        print("%s was not found in the database." % word_input)

# Search for a word by date
elif search_option == "d":
    input_valid = False
    while not input_valid:
        year_input = input("Enter the year: ")
        month_input = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
        day_input = input("Enter the day: ")
        if len(day_input) == 1:
            day_input = "0" + day_input
        matching_date = merge(year_input, month_input, day_input)
        if matching_date != 0:
            input_valid = True
    word_input = isMatch(matching_date, original_date_list, original_word_list)
    if matching_date < first_date:
        print("%d is too early. No wordles occurred before %d. Enter a later date." % (matching_date, first_date))
    elif matching_date > last_date:
        print("%d is too recent. Our records only go as late as %d. Please enter an earlier date." % (matching_date, last_date))
    if word_input:
        print("The word entered on %d was %s." % (matching_date, word_input))
