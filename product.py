# Name:         Kat Kime
# Date:         February 27, 2021
# Description:  Facilitates the creation and manipulation of product objects.
import json
from json import JSONEncoder


class Product:

    def __init__(self):
        self._item_type = None
        self._item_category = None
        self._uniq_id = None
        self._item_name = None
        self._number_of_reviews = None
        self._average_review_rating = None
        self._amazon_category_and_sub_category = None

    def convert_to_dict(self):
        """
        Converts this python object into a dictionary
        :return: Dictionary form of Python object
        """
        dictionary = {"item_type": self._item_type, "item_category": self._item_category, "item_name": self._item_name,
                      "average_review_rating": self._average_review_rating,
                      "number_of_reviews": self._number_of_reviews}

        return dictionary

    def set_item_type(self, item_type):
        self._item_type = item_type

    def set_item_category(self, category):
        self._item_category = category

    def set_uniq_id(self, uniq_id):
        self._uniq_id = uniq_id

    def set_item_name(self, name):
        self._item_name = name

    def set_number_of_reviews(self, num):
        self._number_of_reviews = num

    def set_average_review_rating(self, rating):
        self._average_review_rating = rating

    def set_amazon_category_and_sub_category(self, item_category):
        self._amazon_category_and_sub_category = item_category

        categories = item_category.split('>')
        categories[0] = categories[0][0:-1]

        self._item_category = categories[0]

    def get_item_type(self):
        return self._item_type

    def get_item_category(self):
        return self._item_category

    def get_uniq_id(self):
        return self._uniq_id

    def get_item_name(self):
        return self._item_name

    def get_number_of_reviews(self):
        return self._number_of_reviews

    def get_average_review_rating(self):
        return self._average_review_rating

    def get_amazon_category_and_sub_category(self):
        return self._amazon_category_and_sub_category
