# to create GUI using tkinter
import time
import tkinter as tk
from tkinter import filedialog
# import searching algorithm functions and text processing function
from bruteforce import brute_force
from kmp import compute_LPS, search_KMP
from rabinkarp import rabin_karp, convert
from importtext import save_file


# initialise variables used in the upload and searching algorithm functions
text_to_search=""
pattern_from_file=""


# define the functions for uploading .fna file for text and pattern
def UploadText():
    global text_to_search
    text_fna_filename = filedialog.askopenfilename(filetypes=(("FASTA files", "*.fna"), ("all files", "*.*")))
    print('Selected:', text_fna_filename)
    tselection = "Selected: " + text_fna_filename
    label_file = tk.Label(frame, text=tselection, fg='#303030', bg='#80c1ff', font=('Helvetica', 9))
    label_file.place(rely=0.18, relwidth=1, relheight=0.1)
    text_to_search = save_file(text_fna_filename)

def UploadPattern():
    global pattern_from_file
    pattern_fna_filename = filedialog.askopenfilename(filetypes=(("FASTA files", "*.fna"), ("all files", "*.*")))
    print("Selected:", pattern_fna_filename)
    pselection = "Selected: " + pattern_fna_filename
    label_pattern = tk.Label(frame, text=pselection, fg='#303030', bg='#80c1ff', font=('Helvetica', 9))
    label_pattern.place(rely=0.70, relwidth=1, relheight=0.1)
    pattern_from_file = save_file(pattern_fna_filename)


# define the functions to be called for each of the searching algorithms when their respective button is clicked
def bf(pattern):
    # account for errors (with regard to input from user)
    if text_to_search == "":
        result_label['text'] = "Please upload a .fna text file before proceeding."
    elif pattern_entry.get() == "" and pattern_from_file == "":
        result_label['text'] = "Please enter a search pattern or upload a .fna pattern file before proceeding."
    elif pattern_entry.get() != "" and pattern_from_file != "":
        result_label['text'] = "Please only enter a search pattern OR upload a .fna pattern file (do not do both)"
    else:
        if pattern_from_file != "":
            pattern = pattern_from_file
        start_time = time.time()
        result = brute_force(pattern, text_to_search)
        print("--- %s seconds ---" % (time.time() - start_time))
        result_label['text'] = "Brute Force Algoithm called with pattern " + pattern + "\nResults: " + result

def kmp(pattern):
    # account for errors (with regard to input from user)
    if text_to_search == "":
        result_label['text'] = "Please upload a .fna text file before proceeding."
    elif pattern_entry.get() == "" and pattern_from_file == "":
        result_label['text'] = "Please enter a search pattern or upload a .fna pattern file before proceeding."
    elif pattern_entry.get() != "" and pattern_from_file != "":
        result_label['text'] = "Please only enter a search pattern OR upload a .fna pattern file (do not do both)"
    else:
        if pattern_from_file != "":
            pattern = pattern_from_file
        start_time = time.time()
        result = search_KMP(pattern, text_to_search)
        print("--- %s seconds ---" % (time.time() - start_time))
        result_label['text'] = "KMP Algoithm called with pattern " + pattern + "\nResults: " + result

def rk(pattern):
    # account for errors (with regard to input from user)
    if text_to_search == "":
        result_label['text'] = "Please upload a .fna text file before proceeding."
    elif pattern_entry.get() == "" and pattern_from_file == "":
        result_label['text'] = "Please enter a search pattern or upload a .fna pattern file before proceeding."
    elif pattern_entry.get() != "" and pattern_from_file != "":
        result_label['text'] = "Please only enter a search pattern OR upload a .fna pattern file (do not do both)"
    else:
        if pattern_from_file != "":
            pattern = pattern_from_file
        hash_number = convert(pattern)
        start_time = time.time()
        result = rabin_karp(pattern, text_to_search)
        print("--- %s seconds ---" % (time.time() - start_time))
        result_label['text'] = "Rabin-Karp Algorithm called with pattern " + pattern + " which has a hash value of " + str(hash_number) + "\nResults: " + result





# GUI
# create root window
root = tk.Tk()
root.title("Searching Algorithms") # title of root window
# set the dimensions of the root window and the place the window will appear at
WIDTH=700
HEIGHT=500
POSX=150
POSY=50
root.wm_geometry("%dx%d+%d+%d" % (WIDTH,HEIGHT,POSX,POSY))
root.iconbitmap('./search.ico')


# add widgets here
# main frame
frame = tk.Frame(root, bg='#80c1ff', bd=20)
frame.place(relx=0.5, rely=0, relwidth=0.996, relheight=0.45, anchor='n')


# upload text label and button
upload_label = tk.Label(frame, text="Upload a .fna flie as the text to search from", bg='#80c1ff', font=('Helvetica', 10), anchor='nw')
upload_label.place(relwidth=0.40, relheight=0.12)

text_button = tk.Button(frame, text="Upload Text", font=("Helvetica", 10), command=UploadText)
text_button.place(relx=0.42, relwidth=0.15, relheight=0.12)


# enter/upload pattern label, entry box and button
pattern_label = tk.Label(frame, text="Enter the pattern you want to search OR Upload a .fna file as the pattern you want to search", bg='#80c1ff', font=('Helvetica', 10), anchor='nw')
pattern_label.place(rely=0.33, relwidth=1, relheight=0.12)

pattern_entry = tk.Entry(frame, font=("Helvetica", 10))
pattern_entry.place(rely=0.52, relwidth=0.72, relheight=0.12)

or_label = tk.Label(frame, text="OR", bg='#80c1ff', font=('Helvetica', 10))
or_label.place(relx=0.74, rely=0.52, relwidth=0.04, relheight=0.12)

pattern_button = tk.Button(frame, text="Upload Pattern", font=('Helvetica', 10), command=UploadPattern)
pattern_button.place(relx=0.80, rely=0.52, relwidth=0.17, relheight=0.12)


# choosing search algorithm label and buttons
search_label = tk.Label(frame, text="Search using:", bg='#80c1ff', font=('Helvetica', 10), anchor='nw')
search_label.place(rely=0.9, relwidth=0.15, relheight=0.12)

bf_button = tk.Button(frame, text="Brute Force", font=('Helvetica', 10), command=lambda: bf(pattern_entry.get().upper()))
bf_button.place(relx=0.16, rely=0.9, relwidth=0.15, relheight=0.12)

kmp_button = tk.Button(frame, text="KMP", font=('Helvetica', 10), command=lambda: kmp(pattern_entry.get().upper()))
kmp_button.place(relx=0.35, rely=0.9, relwidth=0.1, relheight=0.12)

rk_button = tk.Button(frame, text="Rabin-Karp", font=('Helvetica', 10), command=lambda: rk(pattern_entry.get().upper()))
rk_button.place(relx=0.49, rely=0.9, relwidth=0.15, relheight=0.12)


# implementing a scrollbar for the results label widget (using a separate frame and canvas)
scroll_frame = tk.Frame(root)
scroll_frame.place(relx=0.5, rely=0.45, relwidth=1, relheight=0.55, anchor='n')
canvas = tk.Canvas(scroll_frame)
canvas.pack(side='left', fill='both', expand=1)
scrollbar = tk.Scrollbar(scroll_frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side='right', fill='y')
canvas.configure(yscrollcommand=scrollbar.set)
label_frame = tk.Frame(canvas)
canvas.create_window((0,0), window=label_frame, anchor='nw')
label_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))


# result label
result_label = tk.Label(label_frame, font=('Helvetica', 10), anchor='nw', justify='left', bd=10, wraplength=650)
result_label.pack()


root.mainloop()
