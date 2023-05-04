import os
import subprocess
import tkinter as tk

# Create the tkinter window
window = tk.Tk()
window.geometry("500x300")
window.title("My Application")

# Create the first input label and entry widget
label1 = tk.Label(window, text="Cognome:", font=("Helvetica", 12))
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(window, font=("Helvetica", 12))
entry1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
entry1.config(validate="key", validatecommand=(window.register(lambda s: s.isalpha()), '%S'))

# Create the second input label and entry widget
label2 = tk.Label(window, text="Cicli:", font=("Helvetica", 12))
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(window, font=("Helvetica", 12))
entry2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
entry2.config(validate="key", validatecommand=(window.register(lambda s: s.isnumeric()), '%S'))

label3 = tk.Label(window, text="Quadranti nella metà superiore:", font=("Helvetica", 12))
label3.grid(row=2, column=0, padx=10, pady=10)
entry3 = tk.Entry(window, font=("Helvetica", 12))
entry3.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
entry3.config(validate="key", validatecommand=(window.register(lambda s: s.isnumeric()), '%S'))

# Create radio buttons
var = tk.StringVar()
var.set("left")
rb1 = tk.Radiobutton(window, text="Sinistra", font=("Helvetica", 12), variable=var, value="left")
rb1.grid(row=3, column=0, padx=10, pady=10)
rb2 = tk.Radiobutton(window, text="Destra", font=("Helvetica", 12), variable=var, value="right")
rb2.grid(row=3, column=1, padx=10, pady=10)

# Create a button to read the values
def read_values():
    value1 = entry1.get()
    value2 = entry2.get()
    value3 = entry3.get()


    # Write values to file
    with open("values.txt", "w") as f:
        f.write("Cognome: {}\n".format(value1))
        f.write("Cicli: {}\n".format(value2))
        f.write("Selected radio button: {}\n".format(var.get()))
        f.write("Quadranti: {}\n".format(value3))


    window.destroy()


    #subprocess.Popen(['python', 'main.py', value1, value2])

button = tk.Button(window, text="Salva Dati", font=("Helvetica", 14), command=read_values)
button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the tkinter mainloop
window.mainloop()
