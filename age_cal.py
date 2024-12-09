import tkinter as tk
from tkinter import ttk
from datetime import datetime

class AgeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")  # Light gray background

        # Title Label with a pop of color
        self.title_label = ttk.Label(root, text="Age Calculator", font=("Helvetica", 20, "bold"), background="#f0f0f0", foreground="#007bff")  # Blue text
        self.title_label.pack(pady=20)

        # Date of Birth Entry with a hint of green
        self.dob_label = ttk.Label(root, text="Enter your Date of Birth:", background="#f0f0f0", foreground="#008d39")  # Green text
        self.dob_label.pack(pady=10)

        # Frame for Day, Month, Year Entries with a touch of yellow
        self.dob_frame = ttk.Frame(root, padding=10, relief=tk.RIDGE, borderwidth=2, style="My.TFrame")  # Custom frame style
        self.dob_frame.pack(pady=10)

        # Day Entry
        self.day_label = ttk.Label(self.dob_frame, text="Day:", background="#f0f0f0", foreground="#007bff")  # Blue text
        self.day_label.pack(side=tk.LEFT, padx=10)
        self.day_entry = ttk.Entry(self.dob_frame, font=("Helvetica", 14), width=5, style="My.TEntry")  # Custom entry style
        self.day_entry.pack(side=tk.LEFT, padx=10)

        # Month Entry
        self.month_label = ttk.Label(self.dob_frame, text="Month:", background="#f0f0f0", foreground="#008d39")  # Green text
        self.month_label.pack(side=tk.LEFT, padx=10)
        self.month_entry = ttk.Entry(self.dob_frame, font=("Helvetica", 14), width=5, style="My.TEntry")  # Custom entry style
        self.month_entry.pack(side=tk.LEFT, padx=10)

        # Year Entry
        self.year_label = ttk.Label(self.dob_frame, text="Year:", background="#f0f0f0", foreground="#007bff")  # Blue text
        self.year_label.pack(side=tk.LEFT, padx=10)
        self.year_entry = ttk.Entry(self.dob_frame, font=("Helvetica", 14), width=10, style="My.TEntry")  # Custom entry style
        self.year_entry.pack(side=tk.LEFT, padx=10)

        # Calculate Button with a pop of orange
        self.calculate_button = ttk.Button(root, text="Calculate Age", command=self.calculate_age, style="My.TButton")  # Custom button style
        self.calculate_button.pack(pady=20)

        # Result Label with a touch of purple
        self.result_label = ttk.Label(root, text="", font=("Helvetica", 14), background="#f0f0f0", foreground="#6B7280")  # Purple text
        self.result_label.pack(pady=10)

    def calculate_age(self):
        day = self.day_entry.get()
        month = self.month_entry.get()
        year = self.year_entry.get()
        dob_str = f"{year}-{month}-{day}"
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d")
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            months = (today.month + 12 * today.year) - (dob.month + 12 * dob.year)
            days = (today - dob).days % 365
            self.result_label.config(text=f"You are {age} years, {months % 12} months, and {days} days old.")
        except ValueError:
            self.result_label.config(text="Invalid Date Format! Use YYYY-MM-DD.")

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.configure("My.TFrame", padding=10, relief=tk.RIDGE, borderwidth=2, background="#f0f0f0")
    style.configure("My.TEntry", padding=10, relief=tk.FLAT, font=("Helvetica", 14))
    style.configure("My.TButton", padding=10, relief=tk.RAISED, font=("Helvetica", 14), foreground="#FFA07A")  # Orange text
    app = AgeCalculatorApp(root)
    root.mainloop()