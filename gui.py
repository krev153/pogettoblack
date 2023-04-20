import os
import subprocess
import tkinter as tk

# Create the tkinter window
window = tk.Tk()
window.geometry("500x500")

# Create the first input label and entry widget
label1 = tk.Label(window, text="Enter the first value:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

# Create the second input label and entry widget
label2 = tk.Label(window, text="Enter the second value:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

# Create a button to read the values
def read_values():
    value1 = entry1.get()
    value2 = entry2.get()
    print("Value 1:", value1)
    print("Value 2:", value2)
    subprocess.Popen(['python', 'main.py', value1, value2])


button = tk.Button(window, text="Salva i dati", command=read_values)
button.pack()

# Run the tkinter mainloop
window.mainloop()