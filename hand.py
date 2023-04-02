import tkinter as tk
from tkinter import filedialog

# Define the function to select the first file
def select_file1():
    global file_path1
    file_path1 = filedialog.askopenfilename()
    file_path1_label.config(text=file_path1)

# Define the function to select the second file
def select_file2():
    global file_path2
    file_path2 = filedialog.askopenfilename()
    file_path2_label.config(text=file_path2)

# Define the validation function
def validate():
    global file_path1, file_path2
    if file_path1 != "" and file_path2 != "":
        with open(file_path1, "r") as f1:
            content1 = f1.read()
        with open(file_path2, "w") as f2:
            f2.write(content1)
        success_label.config(text="Success", fg="green")
        window.after(5000, lambda: success_label.config(text=""))

# Create a tkinter window
window = tk.Tk()
window.title("HaND change save file")

# Add widgets to select two files
file1_button = tk.Button(window, text="Select the save file", command=select_file1)
file1_button.pack()

file_path1_label = tk.Label(window, text="")
file_path1_label.pack()

file2_button = tk.Button(window, text="Select the file you want to overwrite", command=select_file2)
file2_button.pack()

Label_under_file2 = tk.Label(window, text="File is usually located in C:\\Users\\YourUsername\\AppData\\LocalLow\\MagicDesignStudio\\HaveANiceDeath\\Normal_save_game_0.gd")
Label_under_file2.pack()

file_path2_label = tk.Label(window, text="")
file_path2_label.pack()

# Add a "Validate" button
validate_button = tk.Button(window, text="Validate", command=validate)
validate_button.pack()

# Add a success message
success_label = tk.Label(window, text="")
success_label.pack()

# Add a "Quit" button
quit_button = tk.Button(window, text="Quit", command=window.quit)
quit_button.pack()

# Launch the window
window.mainloop()