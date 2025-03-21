import tkinter as tk
from tkinter import ttk


class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Währungsrechner: Euro zu Yen")
        self.root.geometry("900x300")

        self.label_title = tk.Label(root, text="Euro zu Yen Umrechner", font=("Arial", 20))
        self.label_title.pack(pady=10)

        self.label_euro = tk.Label(root, text="Betrag in Euro:", font=("Arial", 16))
        self.label_euro.pack(pady=5)

        self.entry_euro = tk.Entry(root, font=("Arial", 16))
        self.entry_euro.pack(pady=5)

        self.button_convert = tk.Button(root, text="Umrechnen", font=("Arial", 16), command=self.convert_to_yen)
        self.button_convert.pack(pady=10)

        self.label_result = tk.Label(root, text="Ergebnis in Yen: ", font=("Arial", 16))
        self.label_result.pack(pady=10)

    def convert_to_yen(self):
        try:
            euro = float(self.entry_euro.get())
            yen = euro * 145  # Beispiel-Wechselkurs: 1 Euro = 145 Yen
            self.label_result.config(text=f"Ergebnis in Yen: {yen:.2f}")
        except ValueError:
            self.label_result.config(text="Bitte eine gültige Zahl eingeben!")


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()