"""
Furqaan Mohammed 752879
Date: 23 January, 2025
Course: ICS3U0-Introduction to Computer Science
Title: Credit Card Report
Description: This program reads a file containing credit card data, sorts it by expiration date, and determines the status of each card (EXPIRED, RENEW IMMEDIATELY) based on the current date. The output is printed to the console and written to a file.

VARIABLE DICTIONARY:
  fr                       (file)   File object used for reading input data.
  accholder                (list)   List of full names (account holders) read from the input file.
  cardnums                 (list)   List of credit card numbers read from the input file.
  cardtypes                (list)   List of credit card types read from the input file.
  expdates                 (list)   List of credit card expiration dates in `YYYYMM` integer format.
  lines                    (list)   List of all lines read from the input file, excluding the first header line.
  first_line               (str)    Header line from the input file (not used in processing).
  givenname, surname       (str)    First and last names of the account holder from the input data.
  cctype                   (str)    Credit card type read from the input file.
  ccnumber                 (str)    Credit card number read from the input file.
  exp_mo, exp_yr           (str)    Expiration month and year from the input file.
  date                     (int)    Expiration date in `YYYYMM` format for sorting.
  outfile                  (str)    Output file name where results will be written.
  output                   (file)   File object for writing the sorted and processed credit card data.
  cardstatus               (str)    Status of the credit card ("EXPIRED" or "RENEW IMMEDIATELY") based on the expiration date.
"""

"""
Function to perform merge sort on two arrays.
Parameters:
    arr (list): Array to be sorted.
    arr2, arr3, arr4 (list): Other arrays to be sorted.
    l (int): Left index of the subarray.
    r (int): Right index of the subarray.
"""
def mergeSort(arr, arr2, arr3, arr4, l, r):
    # Check if the subarray has more than one element
    if l < r:
        # Find the middle point to divide the array into two halves
        # Avoids potential overflow for large values of l and r
        m = l + (r - l) // 2
        
        # Sort first and second halves
        mergeSort(arr, arr2, arr3, arr4, l, m)
        mergeSort(arr, arr2, arr3, arr4, m + 1, r)
        merge(arr, arr2, arr3, arr4, l, m, r)
        
"""
Function to merge two sorted arrays.
Parameters:
    arr (list): Array to be sorted.
    arr2, arr3, arr4 (list): Other arrays to be sorted.
    l (int): Left index of the subarray.
    m (int): Middle index of the subarray.
    r (int): Right index of the subarray.
"""
def merge(arr, arr2, arr3, arr4, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # Create temp arrays
    L = [0] * (n1)
    L2 = [0] * (n1)
    L3 = [0] * (n1)
    L4 = [0] * (n1)
    R = [0] * (n2)
    R2 = [0] * (n2)
    R3 = [0] * (n2)
    R4 = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
        L2[i] = arr2[l + i]
        L3[i] = arr3[l + i]
        L4[i] = arr4[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R2[j] = arr2[m + 1 + j]
        R3[j] = arr3[m + 1 + j]
        R4[j] = arr4[m + 1 + j]
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr2[k] = L2[i]
            arr3[k] = L3[i]
            arr4[k] = L4[i]
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            arr3[k] = R3[j]
            arr4[k] = R4[j]
            j += 1
        k += 1
    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1
    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1
# Open file
fr = open("data.dat", "r")
# Initialize Arrays 
accholder = [] # Names of account holder
cardnums = [] # Card Numbers
cardtypes = [] # Types of card
expdates = [] # Expiry dates
lines = fr.readlines() # Reads the lines of the data file
first_line = lines.pop(0) # Throw away first line in data file
for i in lines:
    givenname, surname, cctype, ccnumber, exp_mo, exp_yr = i.strip().split(",") # Split the line
    name = givenname + ' ' + surname # Name of holder
    # Append data to lists
    accholder.append(name)
    cardnums.append(ccnumber)
    cardtypes.append(cctype)
    # Expiry date
    a = int(exp_mo)
    if a < 10:
        exp_mo = "0" + exp_mo
    date = exp_yr + exp_mo
    expdates.append(int(date)) # Append date to list
    
fr.close() # Close file

# Sort with merge sort
mergeSort(expdates, accholder, cardnums, cardtypes, 0, len(expdates) - 1)
outfile = "output.txt"
output = open(outfile, "w") # Opens output.txt in write mode
# Checks dates and outputs status accordingly
for i in range(len(expdates)):
    if expdates[i] > 202501:
        break
    else:
        cardstatus = "RENEW IMMEDIATELY"
    if expdates[i] < 202501:
        cardstatus = "EXPIRED"
    print("%-35s %-15s %-20s %-8s %-15s" % (accholder[i] + ":", cardtypes[i], "#" + cardnums[i], expdates[i], cardstatus))
    output.write("%-35s %-15s %-20s %-8s %-15s\n" % (accholder[i] + ":", cardtypes[i], "#" + cardnums[i], expdates[i], cardstatus)) # Write output to file
# Close the output file
output.close()
print("\nOutputted to %s file" % outfile)