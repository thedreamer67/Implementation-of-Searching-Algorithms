# KMP
import re

# function to pre-process the pattern
def compute_LPS(pat):

    m = len(pat)
    lps = [0]*m

    # index 0 will always be 0, so starts at index 1
    i = 1
    j = 0

    while i<m:
        if pat[i] == pat[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        # mismatch
        else:
            if j == 0:
                lps[i] = 0
                i += 1
            # check the index of prev possible prefix if len == 1
            else:
                j = lps[j-1]
    return lps


# function to search for pattern in text
def search_KMP(pat, text):

    # calculate length of text and query pattern
    n = len(text)
    m = len(pat)

    list_of_indices = []
    answer = ""

    lps = compute_LPS(pat)
    i=0 # index for text
    j=0 # index for pat

    while i<n:
        # if match, increment 1 for both index
        if pat[j] == text[i]:
            i += 1
            j += 1
        # mismatch occurs
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1] # lps will tell from where to compare next
        # the pattern is found
        if j == m:
            list_of_indices.append(i-j)
            # to find more patterns
            j = lps[j-1]


    # return results of the search
    string_of_indices = " ".join([str(num) for num in list_of_indices])
    string_of_indices = re.sub("\s+", ", ", string_of_indices)
    answer = "Pattern " + pat + " appears in the text at the index/indices: " + string_of_indices
    return answer
