import numpy as np
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)

def get_top_colors(image_path, num_colors=10):
    # Open image and convert to RGB
    img = Image.open(image_path).convert('RGB')
    # Resize to speed up processing without losing general color profile
    img.thumbnail((200, 200))
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Reshape the 3D array (height, width, RGB) into a 2D array (all_pixels, RGB)
    pixels = img_array.reshape(-1, 3)
    
    # Find unique rows (colors) and their counts
    unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)
    
    # Get indices of the most frequent colors
    top_indices = np.argsort(-counts)[:num_colors]
    top_colors = unique_colors[top_indices]
    
    # Convert RGB to HEX strings for CSS
    hex_colors = [
        '#{:02x}{:02x}{:02x}'.format(r, g, b) 
        for r, g, b in top_colors
    ]
    return hex_colors

@app.route("/", methods=["GET", "POST"])
def index():
    colors = []
    if request.method == "POST":
        file = request.files['file']
        if file:
            # In a real app, save securely; here we process directly
            colors = get_top_colors(file)
            
    return render_template("index.html", colors=colors)

if __name__ == "__main__":
    app.run(debug=True)