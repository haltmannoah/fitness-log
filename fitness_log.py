import tkinter as tk

root = tk.Tk()
root.title("Fitness Log")
root.geometry("520x360")
root.resizable(False, False)

sets = []

top = tk.Frame(root)
top.pack(fill="x", padx=16, pady=10)

title = tk.Label(top, text="Fitness Log", font=("Arial", 18, "bold"))
title.pack(anchor="w")

input_frame = tk.Frame(top)
input_frame.pack(fill="x", pady=(10, 0))

# Exercise
tk.Label(input_frame, text="Exercise:").grid(row=0, column=0, sticky="w")
exercise_entry = tk.Entry(input_frame, width=28)
exercise_entry.grid(row=1, column=0, padx=(0, 12), pady=(2, 8), sticky="w")

# Weight
tk.Label(input_frame, text="Weight:").grid(row=0, column=1, sticky="w")
weight_entry = tk.Entry(input_frame, width=10)
weight_entry.grid(row=1, column=1, padx=(0, 12), pady=(2, 8), sticky="w")

# Reps
tk.Label(input_frame, text="Reps:").grid(row=0, column=2, sticky="w")
reps_entry = tk.Entry(input_frame, width=10)
reps_entry.grid(row=1, column=2, pady=(2, 8), sticky="w")

status_label = tk.Label(top, text="", fg="red")
status_label.pack(anchor="w", pady=(0, 6))

def on_add_set():
    exercise = exercise_entry.get().strip()
    weight = weight_entry.get().strip()
    reps = reps_entry.get().strip()

    if exercise == "" or weight == "" or reps == "":
        status_label.config(text="Fill all fields.", fg="red")
        return

    if not weight.isdigit() or not reps.isdigit():
        status_label.config(text="Weight and reps must be whole numbers.", fg="red")
        return

    weight_i = int(weight)
    reps_i = int(reps)

    sets.append([exercise, weight_i, reps_i])

    line = f"{exercise} | {weight_i} | {reps_i}"
    log_listbox.insert(tk.END, line)

    exercise_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)
    exercise_entry.focus()

    status_label.config(text="Set added!", fg="green")

add_button = tk.Button(top, text="Add Set", command=on_add_set, width=12)
add_button.pack(anchor="w", pady=(0, 6))


bottom = tk.Frame(root)
bottom.pack(fill="both", expand=True, padx=16, pady=(0, 12))

log_label = tk.Label(bottom, text="Session Log:", font=("Arial", 12, "bold"))
log_label.pack(anchor="w")

log_frame = tk.Frame(bottom)
log_frame.pack(fill="both", expand=True, pady=(6, 0))

log_listbox = tk.Listbox(log_frame, height=10)
log_listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(log_frame, orient="vertical", command=log_listbox.yview)
scrollbar.pack(side="right", fill="y")
log_listbox.config(yscrollcommand=scrollbar.set)

exercise_entry.focus()
root.mainloop()
