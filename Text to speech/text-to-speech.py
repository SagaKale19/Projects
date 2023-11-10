import tkinter as tk
from tkinter import scrolledtext
import pyttsx3

def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    rate = int(rate_entry.get()) if rate_entry.get().isdigit() else 150

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set speech rate (speed)
    engine.setProperty('rate', rate)

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

# Create the main application window
app = tk.Tk()
app.title("Text-to-Speech Application")

# Create and place widgets in the window
text_label = tk.Label(app, text="Enter text:")
text_label.pack(pady=10)

text_entry = scrolledtext.ScrolledText(app, height=5, width=40, wrap=tk.WORD)
text_entry.pack(pady=10)

rate_label = tk.Label(app, text="Speech rate:")
rate_label.pack(pady=5)

rate_entry = tk.Entry(app)
rate_entry.pack(pady=10)

speak_button = tk.Button(app, text="Speak", command=text_to_speech)
speak_button.pack(pady=20)

# Run the application
app.mainloop()
