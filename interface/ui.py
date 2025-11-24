import tkinter as tk
from tkinter import messagebox

from add import add
from multiply import multiply
from subtract import subtract
from divide import divide

def calculate(operation):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawne liczby!")
        return

    try:
        if operation == "add":
            result = add(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "divide":
            result = divide(a, b)
    except NotImplementedError as e:
        messagebox.showwarning("Funkcja nie gotowa", str(e))
        return

    messagebox.showinfo("Wynik", f"Wynik: {result}")

root = tk.Tk()
root.title("Kalkulator")

label_a = tk.Label(root, text="Liczba A:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Liczba B:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

btn_add = tk.Button(root, text="Dodawanie", command=lambda: calculate("add"))
btn_add.pack(pady=5)

btn_mul = tk.Button(root, text="Mnożenie", command=lambda: calculate("multiply"))
btn_mul.pack(pady=5)

btn_sub = tk.Button(root, text="Odejmowanie", command=lambda: calculate("subtract"))
btn_sub.pack(pady=5)

btn_div = tk.Button(root, text="Dzielenie", command=lambda: calculate("divide"))
btn_div.pack(pady=5)

root.mainloop()
