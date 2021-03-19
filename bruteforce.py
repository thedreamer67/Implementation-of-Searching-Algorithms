# BRUTE FORCE
import re

def brute_force(pattern, text):
    t_size = len(text)
    p_size = len(pattern)
    last_i = t_size - p_size
    start = 0
    list_of_indices = []
    answer = ""

    # index each search window starts from
    for start in range(0, last_i+1):
        count=0
        # searching within each search window
        for i in range(0, p_size):
            if text[start+i] == pattern[i]:
                count+=1
            else:
                break
        if count == p_size:
            list_of_indices.append(start)

    # return results of the search
    string_of_indices = " ".join([str(num) for num in list_of_indices])
    string_of_indices = re.sub("\s+", ", ", string_of_indices)
    answer = "Pattern " + pattern + " appears in the text at the index/indices: " + string_of_indices
    return answer
