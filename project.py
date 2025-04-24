import tkinter as tk
from tkinter import messagebox

def calculate_compound_interest():
     try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        times_compounded = int(times_entry.get())
        years = int(years_entry.get())

        amount = principal * (1 + (rate / (100 * times_compounded))) ** (times_compounded * years)
        interest = amount - principal

        messagebox.showinfo("Result", f"Total Amount: ${amount:.2f}\nCompound Interest: ${interest:.2f}")
     except ValueError:
         messagebox.showerror("Input Error", "Please enter valid numerical values.")

root = tk.Tk()
root.title("Compound Interest Calculator")

tk.Label(root, text="Principal Amount ($):").grid(row=0, column=0, padx=10, pady=10)

principal_entry = tk.Entry(root)


principal_entry.grid(row=0, column=1)

tk.Label(root, text="Annual Interest Rate (%):").grid(row=1, column=0, padx=10, pady=10)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1)

tk.Label(root, text="Times Compounded per Year:").grid(row=2, column=0, padx=10, pady=10)
times_entry = tk.Entry(root)
times_entry.grid(row=2, column=1)

tk.Label(root, text="Number of Years:").grid(row=3, column=0, padx=10, pady=10)
years_entry = tk.Entry(root)
years_entry.grid(row=3, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_compound_interest)
calculate_button.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()