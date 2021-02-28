# Name:         Kat Kime
# Date:         February 27, 2021
# Description:  Facilitates the creation and manipulation of life generator GUI objects.
import tkinter as tk
from os import path


class GeneratorGui:
    """
    Represents a GUI object.
    """

    def __init__(self, database):
        self._database = database
        self.launch_gui()

    def launch_gui(self):
        window = tk.Tk()
        self.setup_window(window)
        window.mainloop()

    def write_output(self, product_list, num):
        """
        Takes in a list of products and writes them to a CSV file
        :param product_list: list of products
        :param num: Number of products to generate
        """
        # if output.csv doesn't exist, add header

        if not path.exists("output.csv"):
            # open file
            outfile = open("output.csv", "a+")

            # write header
            outfile.write(self.get_header() + "\n")

            outfile.close()

        # open file
        outfile = open("output.csv", "a+")

        # write product info
        for product in product_list:
            outfile.write(product.get_item_type() + ",")
            outfile.write(product.get_item_category() + ",")
            outfile.write(str(num) + ",")
            outfile.write(product.get_item_name() + ",")
            outfile.write(str(product.get_average_review_rating()) + ",")
            outfile.write(str(product.get_number_of_reviews()) + "\n")

        outfile.close()

    def setup_window(self, window):
        """
        Sets up the intial window for the GUI
        """
        window.title("Top Toy Generator")

        def generate_results():
            def export():
                self.write_output(products, num_to_generate)

            item_type = "toys"

            # get the listbox selection
            item_category = lbx_category.get(lbx_category.curselection())

            # get the num to generate
            num_to_generate = int(en_amount.get())

            # call the database's get top items
            products = self._database.get_top_items(item_type, item_category, num_to_generate)

            header = "input_item_type,input_item_category,input_number_to_generate,output_item_name," \
                     "output_item_rating,output_item_num_reviews"

            lbl_header = tk.Label(master=frame, text=header)
            lbl_header.pack()

            # take product list and display in results
            for product in products:
                output = product.get_item_type() + "," + product.get_item_category() + "," + \
                         str(num_to_generate) + "," + product.get_item_name() + "," + \
                         str(product.get_average_review_rating()) + "," + str(product.get_number_of_reviews())
                temp = tk.Label(master=frame, text=output)
                temp.pack()

            btn_export = tk.Button(text="Export >>", width=20, command=export)
            btn_export.grid(row=2, column=2, sticky="n")

        # setting up grid
        window.rowconfigure([0, 1, 2, 3], minsize=50, weight=1)
        window.columnconfigure([0, 1, 2], minsize=50, weight=1)

        lbl_select = tk.Label(text="Select a Category")
        lbl_select.grid(row=0, column=0, sticky="s")

        lbl_output_amount = tk.Label(text="Output Amount")
        lbl_output_amount.grid(row=0, column=1, sticky="sew")

        lbx_category = tk.Listbox(master=window, selectmode="single")
        lbx_category.grid(row=1, column=0, sticky="n")

        en_amount = tk.Entry(master=window)
        en_amount.grid(row=1, column=1, sticky="n")

        btn_generate = tk.Button(text="Run >>", width=20, height=1, command=generate_results)
        btn_generate.grid(row=1, column=2, sticky="n")

        lbl_output = tk.Label(text="Results:")
        lbl_output.grid(row=2, column=0, sticky="s")

        frame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5, width=200)
        frame.grid(row=3, column=0, sticky="n")

        categories = list(self._database.get_categories().keys())
        categories.sort()

        for category in categories:
            lbx_category.insert('end', category)

    def get_header(self):
        """
        Returns a header for the output file
        :return: a header for the ouptut file
        """
        header = "input_item_type,input_item_category,input_number_to_generate,output_item_name,output_item_rating," \
                 "output_item_num_reviews"

        return header
