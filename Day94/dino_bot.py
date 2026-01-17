import pyautogui
from PIL import ImageGrab, ImageOps
import time

# Give yourself time to switch to the game window
print("Starting in 3 seconds... Switch to the game!")
time.sleep(3)

def restart_game():
    # Clicks the 'Replay' button position (coordinates vary by screen)
    pyautogui.click(480, 380) 

def press_space():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')
    print("Jump!")

def get_pixel_data():
    # 1. Define the 'Search Box' in front of the Dino
    # Coordinates: (left_x, top_y, right_x, bottom_y)
    # These coordinates depend on your screen resolution and window size
    box = (450, 410, 500, 450) 
    
    # 2. Grab the image of that box
    image = ImageGrab.grab(box)
    
    # 3. Convert to Grayscale for easier math
    gray_image = ImageOps.grayscale(image)
    
    # 4. Sum up all pixel values. 
    # If the box is empty (white), the sum is high. 
    # If a cactus (dark) enters, the sum drops.
    pixel_sum = sum(map(sum, gray_image.getdata()))
    return pixel_sum

def run_bot():
    print("Bot is running...")
    # Initial 'empty' box value
    empty_value = get_pixel_data()
    
    while True:
        current_value = get_pixel_data()
        
        # If the pixel sum changes significantly, an obstacle is detected
        if current_value != empty_value:
            press_space()
            # Small delay to prevent double-jumping
            time.sleep(0.1)

if __name__ == "__main__":
    # Note: You need to calibrate the 'box' coordinates for your specific screen
    run_bot()