import tkinter as tk
import time
import random

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Typing Speed Test")
        self.root.geometry("700x450")
        
        self.samples = [
            "The quick brown fox jumps over the lazy dog.",
            "Programming is the art of telling another human what one wants the computer to do.",
            "Consistency is the key to mastering any new skill in software development.",
            "Python is a versatile language used for web apps, data science, and automation."
        ]
        
        self.target_text = random.choice(self.samples)
        self.start_time = None
        
        # UI Elements
        self.label_title = tk.Label(root, text="Test Your Typing Speed", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=20)

        self.label_sample = tk.Label(root, text=self.target_text, font=("Arial", 14), wraplength=600, fg="blue")
        self.label_sample.pack(pady=20)

        self.entry = tk.Text(root, height=5, width=60, font=("Arial", 12))
        self.entry.pack(pady=10)
        # Bind the first keypress to start the timer
        self.entry.bind("<KeyPress>", self.start_timer)

        self.btn_reset = tk.Button(root, text="Reset / New Test", command=self.reset_test)
        self.btn_reset.pack(pady=10)

        self.result_label = tk.Label(root, text="WPM: 0 | Accuracy: 0%", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=20)

        # Check loop
        self.check_loop()

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def reset_test(self):
        self.start_time = None
        self.target_text = random.choice(self.samples)
        self.label_sample.config(text=self.target_text)
        self.entry.delete("1.0", tk.END)
        self.result_label.config(text="WPM: 0 | Accuracy: 0%", fg="black")

    def check_loop(self):
        current_text = self.entry.get("1.0", tk.END).strip()
        
        if self.start_time and current_text:
            elapsed_time = time.time() - self.start_time
            minutes = elapsed_time / 60
            
            # WPM Calculation: (Total characters / 5) / minutes
            words_typed = len(current_text) / 5
            wpm = round(words_typed / minutes) if minutes > 0 else 0
            
            # Accuracy Calculation
            correct_chars = 0
            for i, char in enumerate(current_text):
                if i < len(self.target_text) and char == self.target_text[i]:
                    correct_chars += 1
            
            accuracy = round((correct_chars / len(current_text)) * 100) if len(current_text) > 0 else 0
            
            self.result_label.config(text=f"WPM: {wpm} | Accuracy: {accuracy}%")
            
            # Check if finished
            if current_text == self.target_text:
                self.result_label.config(fg="green")
                self.start_time = None # Stop timer
                
        self.root.after(100, self.check_loop) # Run every 100ms

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
    