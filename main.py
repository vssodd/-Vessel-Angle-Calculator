import math
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        displacement = float(entry_displacement.get())
        GM = float(entry_GM.get())
        ramps = ramp_var.get()

        y = 17.1
        Y = 24

        if ramps == 1:
            weight_of_Stern_ramp = 146
            length_of_center_to_Stern_ramp_weight = 16.1
            length_of_Stern_ramp = 32
            angle_degrees = 1.5

            heel_change_before_stern = round(math.atan(weight_of_Stern_ramp / 2 * length_of_center_to_Stern_ramp_weight / 2 / (displacement * GM)) * 100, 2)
            heel_change_after_stern = round(math.atan((weight_of_Stern_ramp * (length_of_center_to_Stern_ramp_weight / 2 + length_of_Stern_ramp / 2)) / (displacement * GM)) * 100, 2)
            change_of_ships_hull_side_height_stern = round(length_of_center_to_Stern_ramp_weight / 2 * math.tan(heel_change_after_stern - heel_change_before_stern), 2)

            stern_1 = math.tan(math.radians(angle_degrees)) * (displacement * GM)
            x = length_of_center_to_Stern_ramp_weight * stern_1 / (displacement * GM)
            b = (x * y / Y)

            result_text = f"⬛ Stern Ramp Calculation:\n" \
                          f"- Heel before: {heel_change_before_stern}°\n" \
                          f"- Heel after: {heel_change_after_stern}°\n" \
                          f"- Hull height change: {change_of_ships_hull_side_height_stern} m\n\n" \
                          f"⚙ Internal:\n" \
                          f"stern_1 = {round(stern_1, 2)}\n" \
                          f"x = {round(x * 100, 2)}\n" \
                          f"b = {round(b * 100, 2)}"

        elif ramps == 2:
            weight_of_Side_ramp = 31
            length_of_center_to_Side_ramp_weight = 26
            length_of_Side_ramp = 17.0

            heel_change_before_side = round(math.atan(weight_of_Side_ramp / 2 * length_of_center_to_Side_ramp_weight / 2 / (displacement * GM)) * 100, 2)
            heel_change_after_side = round(math.atan((weight_of_Side_ramp * (length_of_center_to_Side_ramp_weight / 2 + length_of_Side_ramp / 2)) / (displacement * GM)) * 100, 2)
            change_of_ships_hull_side_height_side = round(length_of_center_to_Side_ramp_weight / 2 * math.tan(heel_change_after_side - heel_change_before_side), 2)

            stern_1 = math.tan((1.5) * displacement * GM)

            result_text = f"⬛ Side Ramp Calculation:\n" \
                          f"- Heel before: {heel_change_before_side}°\n" \
                          f"- Heel after: {heel_change_after_side}°\n" \
                          f"- Hull height change: {change_of_ships_hull_side_height_side} m\n\n" \
                          f"⚙ Internal:\n" \
                          f"stern_1 = {round(stern_1, 2)}"

        messagebox.showinfo("Result", result_text)

    except Exception as e:
        messagebox.showerror("Error", f"Please enter valid numbers.\n{e}")

# ---------- GUI Setup ----------
window = tk.Tk()
window.title("Vessel Calculator")
window.geometry("440x320")
window.configure(bg="#f7f7f7")
window.attributes('-alpha', 0.0)  # Start fully transparent

font_label = ("Segoe UI", 10)
font_entry = ("Segoe UI", 11)
font_button = ("Segoe UI", 10, "bold")

# Fade-in animation (window fade from transparent to opaque)
def fade_in(alpha=0.0):
    alpha += 0.05
    if alpha <= 1.0:
        window.attributes('-alpha', alpha)
        window.after(25, lambda: fade_in(alpha))

# Hover effects for button
def on_enter(e):
    calculate_button.configure(bg="#005bb5")

def on_leave(e):
    calculate_button.configure(bg="#007aff")

# Frame container
container = tk.Frame(window, bg="#f7f7f7", padx=20, pady=20)
container.pack(expand=True, fill="both")

tk.Label(container, text="Vessel Displacement (tons):", font=font_label, bg="#f7f7f7").grid(row=0, column=0, sticky="w")
entry_displacement = tk.Entry(container, font=font_entry, bd=1, relief="flat")
entry_displacement.grid(row=0, column=1, pady=5, sticky="ew")

tk.Label(container, text="GM (metacentric height):", font=font_label, bg="#f7f7f7").grid(row=1, column=0, sticky="w")
entry_GM = tk.Entry(container, font=font_entry, bd=1, relief="flat")
entry_GM.grid(row=1, column=1, pady=5, sticky="ew")

tk.Label(container, text="Select ramp position:", font=font_label, bg="#f7f7f7").grid(row=2, column=0, sticky="w")
ramp_var = tk.IntVar(value=1)
ramp_frame = tk.Frame(container, bg="#f7f7f7")
ramp_frame.grid(row=2, column=1, pady=5, sticky="w")
tk.Radiobutton(ramp_frame, text="Stern Ramp", variable=ramp_var, value=1, bg="#f7f7f7", font=font_label).pack(side="left", padx=5)
tk.Radiobutton(ramp_frame, text="Side Ramp", variable=ramp_var, value=2, bg="#f7f7f7", font=font_label).pack(side="left", padx=5)

# Modern Apple-style button
calculate_button = tk.Button(container, text="Calculate", font=font_button, bg="#007aff", fg="white", activebackground="#005bb5", relief="flat", height=2, command=calculate)
calculate_button.grid(row=4, column=0, columnspan=2, pady=20, ipadx=10, sticky="ew")
calculate_button.bind("<Enter>", on_enter)
calculate_button.bind("<Leave>", on_leave)

# Grid layout
container.grid_columnconfigure(0, weight=1)
container.grid_columnconfigure(1, weight=2)

fade_in()  # Start animation
window.mainloop()
