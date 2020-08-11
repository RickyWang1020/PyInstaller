"""
Function: tkinter window functions
Author: Xinran Wang
Date: 08/04/2020
"""

from tkinter import *
from tkinter.filedialog import askdirectory, askopenfilename
import os

# the location of .xml file
def select_file_path(tk_file_loc_var, initial_directory=os.getcwd()):
    """
    Let the user select the path of .xml file
    :param tk_file_loc_var: the variable that records the path selected
    :param initial_directory: the initial directory that will be shown on the selection window
    :return: None
    """
    selected_path = askopenfilename(initialdir=initial_directory, filetypes=[('XML Files', '*.xml'),('All files', '*')])
    tk_file_loc_var.set(selected_path)

# the target directory
def select_dir(tk_temp_dir_var, initial_directory=os.getcwd()):
    """
    Let the user select the path of target directory
    :param tk_temp_dir_var: the variable that records the path selected
    :param initial_directory: the initial directory that will be shown on the selection window
    :return: None
    """
    selected_dir = askdirectory(initialdir=initial_directory)
    tk_temp_dir_var.set(selected_dir)


def get_paths():
    """
    Show the path selection window and store the selected paths in variables
    :return: a tuple containing strings of data file location and target folder location
    """
    root = Tk()

    tk_file_loc = StringVar()
    tk_target_dir = StringVar()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width - 450) / 2)
    y = int((screen_height - 200) / 2)

    root.title("Create Folder: Source Data Location and Target Directory")
    root.geometry("%sx%s+%s+%s" % (450, 200, x, y))

    Label(root, text="Please select the data file you want to process (.xml): ").grid(row=0, padx=10, pady=5, sticky=W)
    Entry(root, textvariable=tk_file_loc).grid(row=1, column=0, padx=10, sticky=W+E)
    Button(root, text="Browse Computer", command=lambda: select_file_path(tk_file_loc)).grid(row=1, column=1, padx=10, pady=10, sticky=E)

    Label(root, text="Please assign the directory to put the processed data: ").grid(row=2, padx=10, pady=5, sticky=W)
    Entry(root, textvariable=tk_target_dir).grid(row=3, column=0, padx=10, sticky=W+E)
    Button(root, text="Browse Computer", command=lambda: select_dir(tk_target_dir)).grid(row=3, column=1, padx=10, pady=10)
    Button(root, text="Confirm and Start", command=root.quit).grid(row=5, columnspan=5, padx=10, pady=10, sticky=W+E)
    root.mainloop()

    file_loc_str = tk_file_loc.get()
    file_loc_str = file_loc_str.replace("/", "\\")

    target_dir_str = tk_target_dir.get()
    target_dir_str = target_dir_str.replace("/", "\\")

    try:
        opened = bool(root.winfo_viewable())
        root.destroy()
    except:
        return None

    return file_loc_str, target_dir_str

def further_procedure_path(original_data_path):
    root_restart = Tk()

    tk_default_data_path = StringVar()
    tk_default_data_path.set(original_data_path)
    tk_target_dir = StringVar()

    screen_width = root_restart.winfo_screenwidth()
    screen_height = root_restart.winfo_screenheight()

    x = int((screen_width - 450) / 2)
    y = int((screen_height - 250) / 2)

    root_restart.title("Create XML: Source Data Location and Target Directory")
    root_restart.geometry("%sx%s+%s+%s" % (450, 250, x, y))

    Label(root_restart, text="Please select the data file you want to process (.xml): ").grid(row=0, padx=10, pady=5, sticky=W)
    Label(root_restart, fg="red", text="The Default Data File is the One You Selected in Step 1!").grid(row=1, padx=10, pady=5, sticky=W)
    Entry(root_restart, textvariable=tk_default_data_path).grid(row=2, column=0, padx=10, sticky=W+E)
    Button(root_restart, text="Browse Computer", command=lambda: select_file_path(tk_default_data_path)).grid(row=2, column=1, padx=10, pady=10, sticky=E)

    Label(root_restart, text="Please assign the directory to put the processed data: ").grid(row=3, padx=10, pady=5, sticky=W)
    Entry(root_restart, textvariable=tk_target_dir).grid(row=4, column=0, padx=10, sticky=W+E)
    Button(root_restart, text="Browse Computer", command=lambda: select_dir(tk_target_dir)).grid(row=4, column=1, padx=10, pady=10)
    Button(root_restart, text="Confirm and Start", command=root_restart.quit).grid(row=6, columnspan=5, padx=10, pady=10, sticky=W+E)
    root_restart.mainloop()

    file_loc_str = tk_default_data_path.get()
    file_loc_str = file_loc_str.replace("/", "\\")

    target_dir_str = tk_target_dir.get()
    target_dir_str = target_dir_str.replace("/", "\\")

    try:
        opened = bool(root_restart.winfo_viewable())
        root_restart.destroy()
    except:
        print("Cannot generate new file because the window is closed...")
        return None

    return file_loc_str, target_dir_str

def check_box():
    check_window = Tk()

    screen_width = check_window.winfo_screenwidth()
    screen_height = check_window.winfo_screenheight()

    x = int((screen_width - 450) / 2)
    y = int((screen_height - 280) / 2)

    check_window.title("Create XML: Source Data Location and Target Directory")
    check_window.geometry("%sx%s+%s+%s" % (450, 280, x, y))

    tk_default_data_path = StringVar()
    tk_target_dir = StringVar()
    var1 = BooleanVar()
    var2 = BooleanVar()

    Label(check_window, text="Please select the data file you want to process (.xml): ").grid(row=0, padx=10, pady=5, sticky=W)
    Entry(check_window, textvariable=tk_default_data_path).grid(row=1, column=0, padx=10, sticky=W+E)
    Button(check_window, text="Browse Computer", command=lambda: select_file_path(tk_default_data_path)).grid(row=1, column=1, padx=10, pady=10, sticky=E)

    Label(check_window, text="Please assign the directory to put the processed data: ").grid(row=2, padx=10, pady=5, sticky=W)
    Entry(check_window, textvariable=tk_target_dir).grid(row=3, column=0, padx=10, sticky=W + E)
    Button(check_window, text="Browse Computer", command=lambda: select_dir(tk_target_dir)).grid(row=3, column=1, padx=10, pady=10)

    Checkbutton(check_window, text="Generate a folder containing all .Py files", variable=var1).grid(row=4, padx=10, pady=5, sticky=W)
    Checkbutton(check_window, text="Generate a .xml file containing all test cases", variable=var2).grid(row=5, padx=10, pady=5, sticky=W)

    Button(check_window, text="Confirm and Start", command=check_window.quit).grid(row=6, columnspan=4, padx=10, pady=10, sticky=W + E)

    check_window.mainloop()

    file_loc_str = tk_default_data_path.get()
    file_loc_str = file_loc_str.replace("/", "\\")

    target_dir_str = tk_target_dir.get()
    target_dir_str = target_dir_str.replace("/", "\\")

    try:
        opened = bool(check_window.winfo_viewable())
        check_window.destroy()
    except:
        print("Cannot generate new file because the window is closed...")
        return None

    var1_bool = var1.get()
    var2_bool = var2.get()

    return file_loc_str, target_dir_str, var1_bool, var2_bool
