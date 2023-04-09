import tkinter as tk

# Create the tkinter window
window = tk.Tk()
window.geometry("500x500")

# Create a validation function for entry1
def validate_entry1(text):
    if text.isalpha() or text == "":
        return True
    else:
        return False

# Create the first input label and entry widget with validation
label1 = tk.Label(window, text="Cognome:")
label1.pack()
vcmd = (window.register(validate_entry1), '%P')
entry1 = tk.Entry(window, validate="key", validatecommand=vcmd)
entry1.pack()

# Create a validation function for entry2
def validate_entry2(text):
    if text.isdigit() or text == "":
        return True
    else:
        return False

# Create the second input label and entry widget with validation
label2 = tk.Label(window, text="Numero di esperimenti:")
label2.pack()
vcmd = (window.register(validate_entry2), '%P')
entry2 = tk.Entry(window, validate="key", validatecommand=vcmd)
entry2.pack()

# Create a button to read the values and close the window
def read_values():
    value1 = entry1.get()
    value2 = entry2.get()
    if value1 and value2:
        with open('values.txt', 'w') as f:
            f.write(f"Value 1: {value1}\n")
            f.write(f"Value 2: {value2}\n")

        window.destroy()

button = tk.Button(window, text="Read Values", command=read_values)
button.pack()

# Run the tkinter mainloop
window.mainloop()
