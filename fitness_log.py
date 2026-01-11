import tkinter as tk

root = tk.Tk()
root.title("Fitness Log")
root.geometry("400x300")

label = tk.Label(
    root,
    text="Fitness Log\n(v0)",
    font=("Arial", 18)
)
label.pack(pady=40)

root.mainloop()
