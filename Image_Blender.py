import numpy as np
import tkinter as tk  # Import the Tkinter library for GUI
from tkinter import filedialog, messagebox  # Import file dialog and message box modules
from PIL import Image, ImageTk, ImageEnhance  # Import necessary modules from PIL
from tkinter import ttk  # Import themed Tkinter widgets


class ImageBlenderApp:
    def __init__(self, master):
        # Initialize the GUI application
        self.master = master
        self.master.title("Image Blender")  # Set the title of the application window
        self.master.geometry("800x800")  # Set the initial size of the window
        self.master.configure(bg="#333333")  # Set background color

        # Initialize variables to store images and file names
        self.image1 = None
        self.image2 = None
        self.blended_image = None
        self.image1_name = tk.StringVar()
        self.image2_name = tk.StringVar()
        self.save_name = tk.StringVar()

        # Configure the style of themed buttons
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#000000", foreground="#39FF14", font=('Arial', 10))

        # Create the main frame for the GUI
        self.frame = tk.Frame(master, bg="#333333")
        self.frame.pack(expand=True, fill="both", padx=50, pady=50)

        # Buttons to load images
        self.image1_button = ttk.Button(self.frame, text="Load 1", command=self.load_1)
        self.image1_button.grid(row=0, column=0, pady=(0, 10), padx=10, sticky="ew")

        self.plus_label = tk.Label(self.frame, text="+", bg="#333333", fg="#39FF14", font=('Arial', 20, 'bold'))
        self.plus_label.grid(row=0, column=1, pady=(0, 10))

        self.image2_button = ttk.Button(self.frame, text="Load 2", command=self.load_2)
        self.image2_button.grid(row=0, column=2, pady=(0, 10), padx=10, sticky="ew")

        # Labels to display loaded image names
        self.image1_name_label = tk.Label(self.frame, textvariable=self.image1_name, bg="#333333", fg="#39FF14")
        self.image1_name_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="ew")

        self.plus_label2 = tk.Label(self.frame, text=" ", bg="#333333")
        self.plus_label2.grid(row=1, column=1, pady=(0, 10))

        self.image2_name_label = tk.Label(self.frame, textvariable=self.image2_name, bg="#333333", fg="#39FF14")
        self.image2_name_label.grid(row=1, column=2, pady=(0, 10), padx=10, sticky="ew")

        # Buttons for image blending and boosting
        self.blend_button = ttk.Button(self.frame, text="Blend", command=self.blend)
        self.blend_button.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

        self.boost_button = ttk.Button(self.frame, text="Boost", command=self.boost)
        self.boost_button.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        # Entry widget and button for saving the blended image
        self.save_label = tk.Label(self.frame, text="Save as:", bg="#333333", fg="#39FF14")
        self.save_label.grid(row=4, column=0, pady=10, padx=10, sticky="ew")

        self.save_entry = ttk.Entry(self.frame, textvariable=self.save_name)
        self.save_entry.grid(row=4, column=1, pady=10, padx=10, sticky="ew")

        self.save_button = ttk.Button(self.frame, text="Save", command=self.save)
        self.save_button.grid(row=4, column=2, pady=10, padx=10, sticky="ew")

        # Label to display the resulting blended image
        self.result_label = tk.Label(self.frame)
        self.result_label.grid(row=5, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

    # Method to load the first image
    def load_1(self):
        path = filedialog.askopenfilename()
        if path:
            image = Image.open(path)
            self.image1 = np.array(image)
            self.image1 = self.image1[:, :, :3]
            self.image1_name.set("Image 1: " + path.split("/")[-1])

    # Method to load the second image
    def load_2(self):
        path = filedialog.askopenfilename()
        if path:
            image = Image.open(path)
            self.image2 = np.array(image)
            self.image2 = self.image2[:, :, :3]
            self.image2_name.set("Image 2: " + path.split("/")[-1])

    # Method to blend the loaded images
    def blend(self):
        if self.image1 is not None and self.image2 is not None:
            alpha = 0.5
            self.blended_image = (alpha * self.image1 + (1 - alpha) * self.image2).astype(np.uint8)
            result_image = Image.fromarray(self.blended_image)
            self.display(result_image)
        else:
            print("Load both images first.")

    # Method to boost the color of the blended image
    def boost(self):
        if self.blended_image is not None:
            image = Image.fromarray(self.blended_image)
            enhancer = ImageEnhance.Color(image)
            boosted_image = enhancer.enhance(1.3)
            self.display(boosted_image)
        else:
            print("Blend the images first.")

    # Method to save the blended image
    def save(self):
        if self.blended_image is not None:
            filename = self.save_name.get()
            if filename:
                path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
                if path:
                    try:
                        image = Image.fromarray(self.blended_image)
                        image.save(path)
                        print(f"Saved as {filename}")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                else:
                    print("Provide a valid file name.")
            else:
                print("Enter a file name.")
        else:
            print("No image to save.")

    # Method to display the resulting image on the GUI
    def display(self, image):
        image = ImageTk.PhotoImage(image)
        if hasattr(self, "result_image_label"):
            self.result_image_label.destroy()
        self.result_image_label = tk.Label(self.frame, image=image, bg="#333333")
        self.result_image_label.image = image
        self.result_image_label.grid(row=6, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")


def main():
    root = tk.Tk()  # Create the root window
    app = ImageBlenderApp(root)  # Create an instance of the ImageBlenderApp
    root.mainloop()  # Enter the Tkinter event loop


if __name__ == "__main__":
    main()  # Run the main function when the script is executed
