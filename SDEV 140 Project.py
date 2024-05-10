import tkinter as tk  # Import the tkinter module as tk for easy access
from tkinter import messagebox  # Import the messagebox submodule from tkinter

class IceCreamOrderApp:
    """
    IceCreamOrderApp class defines the main application window and its functionalities.
    """

    def __init__(self, master):
        """
        Initialize the IceCreamOrderApp.

        Args:
            master (tk.Tk): The root window of the application.
        """
        self.master = master  # Initialize the root window
        self.master.title("Kevin's Creamy Confections Order Application")  # Set the title of the window
        self.master.geometry("800x900")  # Set the dimensions of the window

        # Initialize variables to store user inputs
        self.order_type_var = tk.StringVar()
        self.size_var = tk.StringVar()
        self.size_type_var = tk.StringVar()
        self.toppings_var = tk.StringVar()
        self.name_var = tk.StringVar()

        # Create UI widgets
        self.create_widgets()

    def create_widgets(self):
        """
        Create and layout the widgets for the application window.
        """
        # Label and Entry for Name
        name_label = tk.Label(self.master, text="Your Name:")  # Create a label for the name entry
        name_label.pack(pady=(10, 0))  # Pack the name label

        self.name_entry = tk.Entry(self.master, textvariable=self.name_var, validate="key", validatecommand=(self.master.register(self.validate_name), "%S"))  # Create an entry for user to input name
        self.name_entry.pack()  # Pack the name entry

        # Label and Radio Buttons for Order Type
        order_type_label = tk.Label(self.master, text="Order Type:")  # Create a label for the order type
        order_type_label.pack(pady=(10, 0))  # Pack the order type label

        order_frame = tk.Frame(self.master)  # Create a frame for order type radio buttons
        order_frame.pack(pady=5)  # Pack the order frame

        tk.Radiobutton(order_frame, text="Pick Up", variable=self.order_type_var, value="Pick Up").pack(anchor="w")  # Create a radio button for Pick Up
        tk.Radiobutton(order_frame, text="Dine In", variable=self.order_type_var, value="Dine In").pack(anchor="w")  # Create a radio button for Dine In

        # Label and Radio Buttons for Ice Cream Type
        ice_cream_type_label = tk.Label(self.master, text="Ice Cream Type:")  # Create a label for the ice cream type
        ice_cream_type_label.pack(pady=(10, 0))  # Pack the ice cream type label

        type_frame = tk.Frame(self.master)  # Create a frame for ice cream type radio buttons
        type_frame.pack(pady=5)  # Pack the type frame

        tk.Radiobutton(type_frame, text="Cone", variable=self.size_var, value="Cone").pack(anchor="w")  # Create a radio button for Cone
        tk.Radiobutton(type_frame, text="Sundae", variable=self.size_var, value="Sundae").pack(anchor="w")  # Create a radio button for Sundae

        # Label and Spinbox for Ice Cream Size
        size_label = tk.Label(self.master, text="Ice Cream Size:")  # Create a label for the ice cream size
        size_label.pack(pady=(10, 0))  # Pack the size label

        size_frame = tk.Frame(self.master)  # Create a frame for the size spinbox
        size_frame.pack(pady=5)  # Pack the size frame

        # Create a Spinbox widget for selecting size, placed inside a frame
        self.size_spinbox = tk.Spinbox(size_frame, from_=1, to=3, textvariable=self.size_type_var, validate="key", validatecommand=(self.master.register(self.validate_size), "%P"))
        self.size_spinbox.pack(anchor="w") # Pack the Spinbox widget to the frame, aligning it to the west (left) side

        # Label and Checkbuttons for Toppings
        toppings_label = tk.Label(self.master, text="Toppings:")  # Create a label for the toppings
        toppings_label.pack(pady=(10, 0))  # Pack the toppings label

        toppings_frame = tk.Frame(self.master)  # Create a frame for the toppings checkbuttons
        toppings_frame.pack(pady=5)  # Pack the toppings frame

        # Initialize variables to store topping selections
        self.nuts_var = tk.IntVar()
        self.chocolate_var = tk.IntVar()
        self.strawberry_var = tk.IntVar()
        self.pineapple_var = tk.IntVar()
        self.whipped_cream_var = tk.IntVar()
        self.sprinkles_var = tk.IntVar()
        self.sugar_cookies_var = tk.IntVar()
        self.bananas_var = tk.IntVar()
        self.cherry_var = tk.IntVar()

        # Create checkbuttons for various toppings
        tk.Checkbutton(toppings_frame, text="Nuts", variable=self.nuts_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Chocolate", variable=self.chocolate_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Strawberry Syrup", variable=self.strawberry_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Pineapple Syrup", variable=self.pineapple_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Whipped Cream", variable=self.whipped_cream_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Sprinkles", variable=self.sprinkles_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Sugar Cookies", variable=self.sugar_cookies_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Bananas", variable=self.bananas_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Cherry", variable=self.cherry_var).pack(anchor="w")

        # Buttons for submitting order and exiting application
        submit_button = tk.Button(self.master, text="Place Order", command=self.place_order)  # Create a button to place order
        submit_button.pack(pady=10)  # Pack the submit button

        exit_button = tk.Button(self.master, text="Exit", command=self.exit_application)  # Create a button to exit application
        exit_button.pack(pady=10)  # Pack the exit button

        # Load and display images
        self.image1 = tk.PhotoImage(file="cone.png")  # Load an image for Cone
        self.image2 = tk.PhotoImage(file="ice.png")  # Load an image for Ice Cream

        # Display images
        image_label1 = tk.Label(self.master, image=self.image1)  # Create a label to display image1
        image_label1.pack(side="left")  # Pack the label to the left

        image_label2 = tk.Label(self.master, image=self.image2)  # Create a label to display image2
        image_label2.pack(side="right")  # Pack the label to the right

    def validate_name(self, char):
        """
        Validate characters entered for the name.

        Args:
            char (str): The character to be validated.

        Returns:
            bool: True if the character is valid (a letter or space), False otherwise.
        """
        if char.isalpha() or char == " ":  # Check if the character is a letter or space
            return True
        messagebox.showerror("Error", "Please type in only letters and spaces.") #If false, display error message
        return False
    
    def validate_size(self, value): 
        try: # Attempt to convert the input value to an integer
            size = int(value)
            if 1 <= size <= 3: # Check if the converted size is within the valid range (1 to 3)
                return True # If size is valid, return True
            else: # If size is not within the valid range, show an error message and return False
                messagebox.showerror("Error", "Please enter a number between 1 and 3 for ice cream size.")
                return False
        except ValueError: # If conversion to integer fails, return False
            return False


    def place_order(self):
        """
        Process the order details and display them.
        """
        # Retrieve user inputs
        customer_name = self.name_var.get().strip()  # Get the customer name
        order_type = self.order_type_var.get()  # Get the order type
        ice_cream_type = self.size_var.get()  # Get the ice cream type
        ice_cream_size = self.size_type_var.get().strip()  # Get the ice cream size
        toppings = []  # Initialize a list to store selected toppings

        # Check which toppings are selected and add them to the list
        if self.nuts_var.get():
            toppings.append("Nuts")
        if self.chocolate_var.get():
            toppings.append("Chocolate")
        if self.strawberry_var.get():
            toppings.append("Strawberry Syrup")
        if self.pineapple_var.get():
            toppings.append("Pineapple Syrup")
        if self.whipped_cream_var.get():
            toppings.append("Whipped Cream")
        if self.sprinkles_var.get():
            toppings.append("Sprinkles")
        if self.sugar_cookies_var.get():
            toppings.append("Sugar Cookies")
        if self.bananas_var.get():
            toppings.append("Bananas")
        if self.cherry_var.get():
            toppings.append("Cherry")

        # Input validation
        if not (customer_name and order_type and ice_cream_type and ice_cream_size):
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        # Display order details in a new window
        self.show_order_details(customer_name, order_type, ice_cream_type, ice_cream_size, toppings)

    def show_order_details(self, customer_name, order_type, ice_cream_type, ice_cream_size, toppings):
        """
        Display the order details in a new window.

        Args:
            customer_name (str): The name of the customer.
            order_type (str): The type of order (Pick Up or Dine In).
            ice_cream_type (str): The type of ice cream (Cone or Sundae).
            ice_cream_size (str): The size of ice cream.
            toppings (list): List of selected toppings.
        """
        order_details_window = tk.Toplevel(self.master)  # Create a new window for order details
        order_details_window.title("Order Details")  # Set the title of the window
        order_details_window.geometry("400x300")  # Set the dimensions of the window

        # Display order details
        name_label = tk.Label(order_details_window, text="Customer Name: " + customer_name)  # Create a label for customer name
        name_label.pack(pady=5)  # Pack the name label

        order_type_label = tk.Label(order_details_window, text="Order Type: " + order_type)  # Create a label for order type
        order_type_label.pack(pady=5)  # Pack the order type label

        ice_cream_type_label = tk.Label(order_details_window, text="Ice Cream Type: " + ice_cream_type)  # Create a label for ice cream type
        ice_cream_type_label.pack(pady=5)  # Pack the ice cream type label

        ice_cream_size_label = tk.Label(order_details_window, text="Ice Cream Size: " + ice_cream_size)  # Create a label for ice cream size
        ice_cream_size_label.pack(pady=5)  # Pack the ice cream size label

        # Create a string representation of selected toppings
        if not toppings:
            toppings_text = "No toppings added"
        else:
            toppings_text = ", ".join(toppings)

        toppings_label = tk.Label(order_details_window, text="Toppings: " + toppings_text)  # Create a label for toppings
        toppings_label.pack(pady=5)  # Pack the toppings label

    def exit_application(self):
        """
        Exit the application.
        """
        self.master.destroy()  # Destroy the root window to exit the application

root = tk.Tk()  # Create the root window
app = IceCreamOrderApp(root)  # Initialize the IceCreamOrderApp
root.mainloop()  # Start the tkinter event loop
