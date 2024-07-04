#PASSWORD GENERATOR
import tkinter as tk
import random

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("300x250")
        self.window.configure(background="#f0f0f0")  # light gray background

        self.label = tk.Label(self.window, text="PASSWORD GENERATOR", font=("Helvetica", 18, "bold"), fg="red", bg="#f0f0f0")  # blue font on light gray background
        self.label.pack(pady=10)

        self.number_letter_label = tk.Label(self.window, text="Enter the length of alphabets:", font=("Helvetica", 12), fg="#333", bg="#f0f0f0")  # dark gray font on light gray background
        self.number_letter_label.pack()
        self.number_letter_entry = tk.Entry(self.window, width=20, font=("Helvetica", 12), fg="#333", bg="#fff")  # white background with dark gray font
        self.number_letter_entry.pack()

        self.number_digits_label = tk.Label(self.window, text="Enter the length of digits:", font=("Helvetica", 12), fg="#333", bg="#f0f0f0")  # dark gray font on light gray background
        self.number_digits_label.pack()
        self.number_digits_entry = tk.Entry(self.window, width=20, font=("Helvetica", 12), fg="#333", bg="#fff")  # white background with dark gray font
        self.number_digits_entry.pack()

        self.number_special_characters_label = tk.Label(self.window, text="Enter the length of symbols:", font=("Helvetica", 12), fg="#333", bg="#f0f0f0")  # dark gray font on light gray background
        self.number_special_characters_label.pack()
        self.number_special_characters_entry = tk.Entry(self.window, width=20, font=("Helvetica", 12), fg="#333", bg="#fff")  # white background with dark gray font
        self.number_special_characters_entry.pack()

        self.generate_button = tk.Button(self.window, text="Generate Password", command=self.generate_password, font=("Helvetica", 12, "bold"), fg="#fff", bg="blue")  # green button with white font
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self.window, text="", font=("Helvetica", 16), fg="#333", bg="#f0f0f0")  # dark gray font on light gray background
        self.password_label.pack()

    def generate_password(self):
        uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        digits = [str(i) for i in range(10)]
        special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_']
        letter = uppercase_letters + lowercase_letters

        number_letter = int(self.number_letter_entry.get())
        number_digits = int(self.number_digits_entry.get())
        number_special_characters = int(self.number_special_characters_entry.get())

        password_list = []
        password = ""

        for i in range(0, number_letter):
            char = random.choice(letter)
            password_list += char

        for i in range(0, number_digits):
            char = random.choice(digits)
            password_list += char

        for i in range(0, number_special_characters):
            char = random.choice(special_characters)
            password_list += char

        random.shuffle(password_list)
        for i in password_list:
            password += i

        self.password_label.config(text="Your password is: " + password)

    def run(self):
        self.window.mainloop()

generator = PasswordGenerator()
generator.run()
