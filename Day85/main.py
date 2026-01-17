import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Image Watermarker")
        self.root.geometry("400x250")

        # UI Elements
        self.label = tk.Label(root, text="Step 1: Select an Image", font=("Arial", 12))
        self.label.pack(pady=10)

        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=5)

        self.wm_label = tk.Label(root, text="Step 2: Enter Watermark Text")
        self.wm_label.pack(pady=5)
        
        self.text_entry = tk.Entry(root, width=30)
        self.text_entry.insert(0, "Copyright © 2024")
        self.text_entry.pack(pady=5)

        self.process_btn = tk.Button(root, text="Add Watermark & Save", command=self.add_watermark, bg="green", fg="white")
        self.process_btn.pack(pady=20)

        self.file_path = ""

    def upload_image(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.file_path:
            self.label.config(text=f"Selected: {self.file_path.split('/')[-1]}")

    def add_watermark(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please upload an image first!")
            return

        watermark_text = self.text_entry.get()
        
        try:
            # Open the image
            with Image.open(self.file_path).convert("RGBA") as base:
                # Make a blank image for the text, initialized to transparent text color
                txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

                # Get a font (using default if custom not found)
                try:
                    font = ImageFont.truetype("arial.ttf", 40)
                except IOError:
                    font = ImageFont.load_default()

                d = ImageDraw.Draw(txt)

                # Position text at bottom right
                width, height = base.size
                d.text((width - 400, height - 100), watermark_text, fill=(255, 255, 255, 128), font=font)

                out = Image.alpha_composite(base, txt)
                
                # Save the result
                save_path = filedialog.asksaveasfilename(defaultextension=".png")
                if save_path:
                    out.convert("RGB").save(save_path)
                    messagebox.showinfo("Success", "Watermark added and image saved!")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()