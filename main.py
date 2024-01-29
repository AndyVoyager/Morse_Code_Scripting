from brain import morse_convert, play_morse_code
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

# ---------------------------------------------CONST: ------------------------------------------------------------------
BACKGROUND_COLOR = "#EEEDEB"
FONT_COLOR = "#747264"
LABEL_COLOR = "#E0CCBE"
FONT = ("Upright", 26, "bold")
FONT_BUTTON = ("Upright", 18, "bold")

# ---------------------------------------------Create UI: --------------------------------------------------------------
window = tk.Tk()
window.title("Morse Code")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.geometry("800x600+400+150")

canvas = tk.Canvas(window,
                   width=800,
                   height=600,
                   highlightthickness=0,
                   bg=BACKGROUND_COLOR)


# ---------------------------------------------Command functions:-------------------------------------------------------
def convert_to_morse():
    sentence = text_field.get()
    morse_code = morse_convert(sentence)
    morse_code_str = " ".join(morse_code)
    label_field.config(text=morse_code_str)


def play_morse():
    sentence = text_field.get()
    morse_code = morse_convert(sentence)
    play_morse_code(" ".join(morse_code))


def clear_text_field():
    text_field.delete(0, tk.END)
    label_field.config(text="")


# ---------------------------------------------Set a theme for the window-----------------------------------------------
style = ThemedStyle(window)
style.set_theme("breeze")

# ---------------------------------------------Set the same theme for ttk.Style-----------------------------------------
ttk_style = ttk.Style(window)
ttk_style.theme_use(style.theme_use())

ttk_style.configure("TEntry", padding=(5, 20, 5, 20))
ttk_style.configure("TButton", padding=(20, 20, 20, 20), font=FONT_BUTTON, foreground=FONT_COLOR)
ttk_style.configure("TLabel", padding=(10, 20, 10, 20), height=200)

# ---------------------------------------------Create the widgets: -----------------------------------------------------
text_field = ttk.Entry(window, style="TEntry", width=38, font=FONT, foreground=FONT_COLOR)
text_field.grid(row=0, column=0, columnspan=2, pady=20, sticky="w")

button_convert = ttk.Button(text="Convert to Morse Code", style="TButton", cursor="hand2", command=convert_to_morse,
                            width=18)
button_convert.grid(row=1, column=1, pady=20, sticky="e")

label_field = ttk.Label(window, style="TLabel", width=38, font=FONT, foreground=FONT_COLOR, wraplength=680)
label_field.grid(row=2, column=0, columnspan=2, pady=20, sticky="w")

button_play = ttk.Button(text="Play Morse Code", style="TButton", cursor="hand2", command=play_morse, width=18)
button_play.grid(row=3, column=1, pady=20, sticky="e")

button_clean = ttk.Button(text="Clean", style="TButton", cursor="hand2", command=clear_text_field, width=18)
button_clean.grid(row=3, column=0, pady=20, sticky="w")

# ---------------------------------------------------------------- Terminal Version ------------------------------------
# Input a sentence you want to convert to Morse Code:
# sentence = input("Please, Input the sentence You would like to convert to Morse Code:\n")

# morse_code = morse_convert(sentence)
# morse_code = " ".join(morse_code)
#
# print(f"The Sentence:\n{sentence}\nMorse Code:\n{morse_code}")
#
# play_morse_code(morse_code)

window.update()
tk.mainloop()
