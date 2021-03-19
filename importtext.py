def save_file(filename):
    x = open(filename, 'r')  # import the .fna file
    x.readline()  # remove the first line which isn't genetic code
    a = x.read()  # store the file into a variable
    x.close()  # close the file

    text = a.replace("\n", "")  # remove all the line breaks

    return text
