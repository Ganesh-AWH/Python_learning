import PyPDF2
from gtts import gTTS
import os

def pdf_to_audiobook(pdf_filename, output_audio):
    # 1. Open the PDF file
    try:
        with open(pdf_filename, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            full_text = ""

            # 2. Extract text from each page
            print("Extracting text from PDF...")
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    full_text += text + " "

            if not full_text.strip():
                print("No text found in PDF. It might be an image-based PDF.")
                return

            # 3. Convert text to speech
            print("Converting text to speech (this may take a minute)...")
            tts = gTTS(text=full_text, lang='en')
            
            # 4. Save the audio file
            tts.save(output_audio)
            print(f"Success! Your audiobook is saved as: {output_audio}")
            
            # Optional: Play the file immediately (works on Mac/Windows)
            # os.system(f"start {output_audio}") 

    except FileNotFoundError:
        print("Error: The PDF file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Change 'my_book.pdf' to your actual file name
    pdf_to_audiobook("my_book.pdf", "audiobook.mp3")