import tkinter as tk

class IceCreamOrderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kevin's Creamy Confections Order Application")
        self.master.geometry("600x400")

        self.order_type_var = tk.StringVar()
        self.size_var = tk.StringVar()
        self.toppings_var = tk.StringVar()

        self.create_widgets()


    def create_widgets(self):

        # Label for Order Type
        order_type_label = tk.Label(self.master, text="Order Type:")
        order_type_label.pack(pady=(10, 0))

        # Order Type
        order_frame = tk.Frame(self.master)
        order_frame.pack(pady=5)
        tk.Radiobutton(order_frame, text="Pick Up", variable=self.order_type_var, value="Pick Up").pack(anchor="w")
        tk.Radiobutton(order_frame, text="Dine In", variable=self.order_type_var, value="Dine In").pack(anchor="w")

        # Label for Ice Cream Size
        size_label = tk.Label(self.master, text="Ice Cream Size:")
        size_label.pack(pady=(10, 0))

        # Ice Cream Size
        size_frame = tk.Frame(self.master)
        size_frame.pack(pady=5)
        tk.Radiobutton(size_frame, text="One Scoop", variable=self.size_var, value="One Scoop").pack(anchor="w")
        tk.Radiobutton(size_frame, text="Two Scoops", variable=self.size_var, value="Two Scoops").pack(anchor="w")
        tk.Radiobutton(size_frame, text="Three Scoops", variable=self.size_var, value="Three Scoops").pack(anchor="w")

        # Label for Toppings
        toppings_label = tk.Label(self.master, text="Toppings:")
        toppings_label.pack(pady=(10, 0))

        # Toppings
        toppings_frame = tk.Frame(self.master)
        toppings_frame.pack(pady=5)
        self.nuts_var = tk.IntVar()
        self.chocolate_var = tk.IntVar()
        self.strawberry_var = tk.IntVar()
        self.pineapple_var = tk.IntVar()
        self.whipped_cream_var = tk.IntVar()
        self.sprinkles_var = tk.IntVar()
        self.sugar_cookies_var = tk.IntVar()
        self.bananas_var = tk.IntVar()
        self.cherry_var = tk.IntVar()

        tk.Checkbutton(toppings_frame, text="Nuts", variable=self.nuts_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Chocolate", variable=self.chocolate_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Strawberry Syrup", variable=self.strawberry_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Pineapple Syrup", variable=self.pineapple_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Whipped Cream", variable=self.whipped_cream_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Sprinkles", variable=self.sprinkles_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Sugar Cookies", variable=self.sugar_cookies_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Bananas", variable=self.bananas_var).pack(anchor="w")
        tk.Checkbutton(toppings_frame, text="Cherry", variable=self.cherry_var).pack(anchor="w")

        # Submit Button
        submit_button = tk.Button(self.master, text="Place Order", command=self.place_order)
        submit_button.pack(pady=10)

        # Exit Button
        exit_button = tk.Button(self.master, text="Exit", command=self.exit_application)
        exit_button.pack(pady=10)

    def place_order(self):
        order_type = self.order_type_var.get()
        ice_cream_size = self.size_var.get()
        toppings = []
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

        # Process the order 
        print("Order Type:", order_type)
        print("Ice Cream Size:", ice_cream_size)
        print("Toppings:", ', '.join(toppings))

    def exit_application(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = IceCreamOrderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()