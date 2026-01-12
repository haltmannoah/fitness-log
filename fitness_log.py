import tkinter as tk

root = tk.Tk()
root.title("Fitness Log")
root.geometry("520x360")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Fitness Log", font=("Arial", 18, "bold"))
title.pack(pady=(12, 6))

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(padx=16, pady=8, fill="x")
sets = []

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
# Log label
log_label = tk.Label(root, text="Session Log:", font=("Arial", 12, "bold"))
log_label.pack(anchor="w", padx=16)

# Log frame
log_frame = tk.Frame(root)
log_frame.pack(padx=16, pady=(6, 12), fill="both", expand=True)

# Listbox 
log_listbox = tk.Listbox(log_frame, height=10)
log_listbox.pack(side="left", fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(log_frame, orient="vertical", command=log_listbox.yview)
scrollbar.pack(side="right", fill="y")
log_listbox.config(yscrollcommand=scrollbar.set)


# 
def on_add_set():
    exercise = exercise_entry.get().strip()
    weight = weight_entry.get().strip()
    reps = reps_entry.get().strip()

    # validation 
    if exercise == "" or weight == "" or reps == "":
        print("Fill all fields.")
        return
    if not weight.isdigit() or not reps.isdigit():
        print("Weight and reps must be whole numbers.")
        return

    weight = int(weight)
    reps = int(reps)

    # store it in memory
    sets.append([exercise, weight, reps])

    # show it in the UI
    line = f"{exercise} | {weight} | {reps}"
    log_listbox.insert(tk.END, line)

    # inputs for next set
    exercise_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)
    exercise_entry.focus()
    
add_button = tk.Button(root, text="Add Set", command=on_add_set, width=12)
add_button.pack(pady=(0, 10))


root.mainloop()
