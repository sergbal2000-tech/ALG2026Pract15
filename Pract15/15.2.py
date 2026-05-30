import tkinter as tk
from tkinter import messagebox
import requests
import random
import json


class HistoryFactsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Исторические факты")
        self.root.geometry("500x400")

        title_label = tk.Label(root,text="Исторические факты",font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        refresh_button = tk.Button(root,text="Получить новые факты",command=self.load_facts,bg="lightblue",font=("Arial", 12))
        refresh_button.pack(pady=10)

        self.facts_frame = tk.Frame(root)
        self.facts_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.load_facts()

    def get_random_date(self):
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return month, day

    def load_facts(self):
        try:
            for widget in self.facts_frame.winfo_children():
                widget.destroy()
            facts = []
            while len(facts) < 2:
                month, day = self.get_random_date()
                url = f"https://history.muffinlabs.com/date/{month}/{day}"

                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    events = data['data']['Events']
                    random_event = random.choice(events)
                    fact = f"{random_event['year']}: {random_event['text']}"
                    if fact not in facts:
                        facts.append(fact)
            for i, fact in enumerate(facts, 1):
                fact_label = tk.Label(self.facts_frame,text=f"{i}. {fact}",wraplength=450,justify="left",font=("Arial", 10),bg="white",relief="solid",padx=10,pady=5)
                fact_label.pack(fill="x", pady=5)

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить факты: {e}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HistoryFactsApp(root)
    root.mainloop()