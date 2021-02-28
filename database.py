# Name:         Kat Kime
# Date:         February 27, 2021
# Description:  Facilitates the creation and manipulation of database objects.

import csv
from product import Product


class Database:
    """
    Represents a database that holds all the product information from the Amazon Co-Ecommerce sample file.
    """

    def __init__(self, database_file="amazon_co-ecommerce_sample.csv"):
        """
        Initializes a Database instance.
        :param database_file: Source file for e-commerce data. By default, this is set to amazon_co-ecommerce_sample.csv
        """
        self._database_file = database_file
        self._categories = {}

        self._UNIQ_ID = 0
        self._PRODUCT_NAME = 1
        self._NUMBER_OF_REVIEWS = 5
        self._AVERAGE_REVIEW_RATING = 7
        self._AMAZON_CATEGORY_AND_SUB_CATEGORY = 8

        # Parse the database file and add all products to their respective categories
        self.process_products(database_file)

    def process_products(self, infile):
        """
        Takes a file and stores information into the database.
        :param infile: Given input file
        """
        # create an array of product info
        product_array = self.parse_file(infile)
        product_array = product_array[1:]   # remove the header

        # create a list of products
        product_lists = self.create_products(product_array)

        # put product into categories dictionary
        self.categorize_products(product_lists)

    def categorize_products(self, product_lists):
        """
        Put products into the category list
        :param product_lists: List of products created from the product array.
        """
        # iterate through the list of products
        for product in product_lists:

            # if category is in the dictionary, just append
            category = product.get_item_category().lower()

            if category == "":
                category = "general"

            if category in self._categories:
                self._categories[category].append(product)

            # if not, then create a list and add it to the category
            else:
                self._categories[category] = []
                self._categories[category].append(product)

    def parse_file(self, infile):
        """
        Takes in an input file and returns a product array
        :param infile: Given database file
        :return: An array of products
        """

        file = open(infile)
        amazon_reader = csv.reader(file)

        product_array = list(amazon_reader)

        file.close()

        return product_array

    def create_products(self, product_array):
        """
        Takes an array, then returns a list of products.
        :param product_array: An array of product info
        :return: List of products
        """
        products = []

        for product_data in product_array:
            product = Product()

            # set product attributes
            product.set_uniq_id(product_data[self._UNIQ_ID])
            product.set_item_name(product_data[self._PRODUCT_NAME])

            num_reviews = product_data[self._NUMBER_OF_REVIEWS].replace(',', '')

            if num_reviews:
                product.set_number_of_reviews(int(num_reviews))

            else:
                product.set_number_of_reviews(0)

            avg_reviews = product_data[self._AVERAGE_REVIEW_RATING][:3]
            if avg_reviews:
                product.set_average_review_rating(float(product_data[self._AVERAGE_REVIEW_RATING][:3]))

            else:
                product.set_average_review_rating(0)
            product.set_amazon_category_and_sub_category(product_data[self._AMAZON_CATEGORY_AND_SUB_CATEGORY])
            product.set_item_type("toys")

            products.append(product)

        return products

    def get_top_items(self, item_type, item_category, num_to_generate):
        """
        Returns top items in a given category and type.
        :param item_type: User-defined item type
        :param item_category: User-defined item category
        :param num_to_generate: User-defined top number of items to generate
        :return: An array list of top items
        """
        category = item_category.lower()
        products = self._categories[category]

        # sort category by unique id
        self.sort_by_id(products)

        # sort category by number of reviews
        self.sort_by_num_reviews(products)

        # take top x * 10
        products = products[:num_to_generate * 10]

        # sort top x*10 by unique id
        self.sort_by_id(products)

        # sort by average review rating
        self.sort_by_avg_rating(products)

        return products

    def sort_by_id(self, product_list):
        """
        Sorts a list of products by unique ID.
        :param product_list: List of products.
        """
        if len(product_list) > 1:
            # get the mid, left, and right
            mid = len(product_list) // 2
            left = product_list[:mid]
            right = product_list[mid:]

            # sort left
            self.sort_by_id(left)

            # sort right
            self.sort_by_id(right)

            # merge values
            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i].get_uniq_id() < right[j].get_uniq_id():
                    product_list[k] = left[i]
                    i += 1

                else:
                    product_list[k] = right[j]
                    j += 1

                k += 1

            while i < len(left):
                product_list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                product_list[k] = right[j]
                j += 1
                k += 1

    def sort_by_num_reviews(self, product_list):
        """
        Returns a sorted list of products by number of reviews
        :param product_list: List of products.
        """
        if len(product_list) > 1:
            # get the mid, left, and right
            mid = len(product_list) // 2
            left = product_list[:mid]
            right = product_list[mid:]

            # sort left
            self.sort_by_num_reviews(left)

            # sort right
            self.sort_by_num_reviews(right)

            # merge values
            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i].get_number_of_reviews() > right[j].get_number_of_reviews():
                    product_list[k] = left[i]
                    i += 1

                else:
                    product_list[k] = right[j]
                    j += 1

                k += 1

            while i < len(left):
                product_list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                product_list[k] = right[j]
                j += 1
                k += 1

    def sort_by_avg_rating(self, product_list):
        """
        Returns a sorted list of products by average review rating.
        :param product_list: List of products
        """
        if len(product_list) > 1:
            # get the mid, left, and right
            mid = len(product_list) // 2
            left = product_list[:mid]
            right = product_list[mid:]

            # sort left
            self.sort_by_avg_rating(left)

            # sort right
            self.sort_by_avg_rating(right)

            # merge values
            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i].get_average_review_rating() > right[j].get_average_review_rating():
                    product_list[k] = left[i]
                    i += 1

                else:
                    product_list[k] = right[j]
                    j += 1

                k += 1

            while i < len(left):
                product_list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                product_list[k] = right[j]
                j += 1
                k += 1

    def get_categories(self):
        """
        Retuns the database's categories
        :return: database's categories
        """
        return self._categories
