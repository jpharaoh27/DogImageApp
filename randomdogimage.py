import requests
from PIL import Image, ImageTk
import tkinter as tk
import io
import json

# Define the API endpoint that returns the image
API_ENDPOINT = "https://dog.ceo/api/breeds/image/random"

class ImageApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Random Dog Image Generator")
        self.image_label = tk.Label(master)
        self.image_label.pack()
        self.frame = tk.Frame(master)
        self.text_label = tk.Label(self.frame, text="App by Pharaoh")
        self.text_label.pack(side="left", padx=5, pady=5)
        self.refresh_button = tk.Button(self.frame, text="Refresh", command=self.refresh_image)
        self.refresh_button.pack()
        self.frame.pack(expand=True, fill="both", padx=10, pady=10)

    def refresh_image(self):
        # Download the image from the API endpoint
        API_DATA = requests.get(API_ENDPOINT)
        URL = API_DATA.json()['message']
        response = requests.get(URL)
        image_data = response.content

        # Open the image using PIL and convert it to a PhotoImage for tkinter
        pil_image = Image.open(io.BytesIO(image_data))
        tk_image = ImageTk.PhotoImage(pil_image)

        # Update the image label with the new image
        self.image_label.configure(image=tk_image)
        self.image_label.image = tk_image

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageApp(root)
    root.title = "Simple Random Dog Image App by Pharaoh"
    app.refresh_image()
    root.mainloop()
