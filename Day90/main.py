import tkinter as tk

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")
        self.root.geometry("800x600")

        self.timer = None
        self.seconds_left = 5  # The danger threshold

        # UI Components
        self.label = tk.Label(
            root, 
            text="Don't stop typing... you have 5 seconds.", 
            font=("Helvetica", 16),
            fg="red"
        )
        self.label.pack(pady=20)

        self.text_area = tk.Text(root, font=("Georgia", 14), wrap='word', undo=True)
        self.text_area.pack(padx=20, pady=20, expand=True, fill='both')
        
        # Focus the text area immediately
        self.text_area.focus_set()

        # Bind any keypress to the reset_timer function
        self.text_area.bind("<Key>", self.reset_timer)

    def reset_timer(self, event=None):
        # Cancel the existing timer if it exists
        if self.timer is not None:
            self.root.after_cancel(self.timer)
        
        # Start a new countdown
        self.timer = self.root.after(5000, self.delete_text)

    def delete_text(self):
        # The user stopped for 5 seconds—wipe everything
        self.text_area.delete("1.0", tk.END)
        self.label.config(text="TIME'S UP! Everything was deleted. Start again!")
        self.timer = None

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()