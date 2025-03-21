import tkinter as tk
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Währungsrechner")
        self.root.geometry("900x300")

        self.label_title = tk.Label(root, text="Währungsrechner", font=("Arial", 20))
        self.label_title.pack(pady=10)

        self.label_euro = tk.Label(root, text="Betrag in Euro:", font=("Arial", 16))
        self.label_euro.pack(pady=5)

        self.entry_euro = tk.Entry(root, font=("Arial", 16))
        self.entry_euro.pack(pady=5)

        self.currencies = ["EUR", "JPY", "SEK"]
        self.currency_var = tk.StringVar(value=self.currencies[0])

        self.currency_menu = tk.OptionMenu(root, self.currency_var, *self.currencies)
        self.currency_menu.pack(pady=5)

        self.button_convert = tk.Button(root, text="Umrechnen", font=("Arial", 16), command=self.convert_currency)
        self.button_convert.pack(pady=10)

        self.label_result = tk.Label(root, text="Ergebnis: ", font=("Arial", 16))
        self.label_result.pack(pady=10)

    def get_exchange_rate(self, target_currency):
        api_key = "fca_live_FjbXC07DC3EXl9pXvlgbMDwtj0q8xcdqlozHO2Aw"
        url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&base_currency=EUR"
        response = requests.get(url)
        data = response.json()
        return data['data'][target_currency]

    def convert_currency(self):
        try:
            euro = float(self.entry_euro.get())
            target_currency = self.currency_var.get()
            exchange_rate = self.get_exchange_rate(target_currency)
            converted_amount = euro * exchange_rate
            self.label_result.config(text=f"Ergebnis: {converted_amount:.2f} {target_currency}")
        except ValueError:
            self.label_result.config(text="Bitte eine gültige Zahl eingeben!")
        except Exception as e:
            self.label_result.config(text=f"Fehler: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()