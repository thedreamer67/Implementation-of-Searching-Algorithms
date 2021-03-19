# RABIN KARP
import re

# Define the function to calculate the hash value of a given sequence taken in as the argument of the function
def convert(sequence):
    hashno = 0     # Initialising hash value to 0
    # Assigning values for each of the DNA/RNA Bases
    switcher = {
        'G':1,
        'A':2,
        'C':3,
        'T':0,
        'U':0
    }

    for i in range(len(sequence)):
        # Calculating the hash value by mulitplying the value assigned to the DNA/RNA Base in the Switcher block by 4 raised to the power of the index position
        # of each of the DNA/RNA Bases in the sequence string (from Right to Left).
        hashno = (hashno*5 + switcher.get(sequence[i], 4))%101
    return hashno


# Define the function to search for the needle (pattern) in the haystack (text)
def rabin_karp(needle, haystack):
    size_m = len(needle)   # Size of needle
    size_n = len(haystack) # Size of haystack

    list_of_indices = []  # Empty list to append the index positions of successful comparisons
    answer = ""
    text_hash = 0 # Hash value for text/haystack
    needle_hash = 0 # Hash value for pattern/needle
    q = 101 # Prime number used for modulus
    multiplier = 1

    switcher = {
        'G':1,
        'A':2,
        'C':3,
        'T':0,
        'U':0
    }

    for i in range(size_m-1):
        multiplier = (multiplier*5)%q # The value of multiplier would be "pow(d, size_m-1)%q"

    # Calculate the hash value of the needle and of the first seach window in the text
    for i in range(size_m):
        needle_hash = (5*needle_hash + switcher.get(needle[i], 4))%q # Store the hash value of the needle into needle_hash
        text_hash = (5*text_hash + switcher.get(haystack[i], 4))%q # Obtain the hash value of the first search window in the text

    if needle_hash == text_hash: # If hash values of the needle and the 'm' lengthed haystack pattern are the same:
        valid = True # Variable valid to indicate that the pattern of DNA Base comparing is valid
        for j in range(size_m):
            # If the sequence of the DNA Bases of the needle and the haystack do not match, value of valid is changed to False
            if haystack[i+j] != needle[j]:
                valid = False
                break
        # If valid is True then the index positions of successful comparisons are appended to the list containing indices of the text at which the pattern is found
        if valid:
            list_of_indices.append(0)

    for i in range(1, size_n-size_m+1):
        text_hash = (5*(text_hash-switcher.get(haystack[i-1], 4)*multiplier) + switcher.get(haystack[i+size_m-1], 4))%q
        if needle_hash == text_hash: # If hash values of the needle and the 'm' lengthed haystack pattern are the same:
            valid = True # Variable valid to indicate that the pattern of DNA Base comparing is valid
            for j in range(size_m):
                # If the sequence of the DNA Bases of the needle and the haystack do not match, value of valid is changed to False
                if haystack[i+j] != needle[j]:
                    valid = False
                    break
            # If valid is True then the index positions of successful comparisons are appended to the list containing indices of the text at which the pattern is found
            if valid:
                list_of_indices.append(i)

    # Return results of the search
    string_of_indices = " ".join([str(num) for num in list_of_indices])
    string_of_indices = re.sub("\s+", ", ", string_of_indices)
    answer = "Pattern " + needle + " appears in the text at the index/indices: " + string_of_indices
    return answer
