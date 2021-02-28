# Name:         Kat Kime
# Date:         February 14, 2021
# Description:  Takes an input of product data and generates the top X products.
import csv
from os import path
import sys
from database import Database
from generator_gui import GeneratorGui
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def address_toy_match():
    # Get the request
    req = request.get_json()        # { "addresses": [address_1, address_2, address_3, ..., address_n] }
    print(req)

    # Parse the request
    addresses = req["addresses"]
    address_toy_pairs = get_address_toy_pairs(addresses)

    # Send JSON file of address, toy pairs
    address_toy_object = {"address_toys": address_toy_pairs}            # address_toy_pairs = [[address_1, toy_1], [address_2, toy_2], ..., [address_n, toy_n]]

    return address_toy_object, 200


def get_address_toy_pairs(addresses):
    """
    Receives a list of addresses and returns a list of address-toy pairs
    :param addresses: Given list of addresses
    :return: List of address-toy pairs
    """
    # get number of addresses
    num_of_people = len(addresses)

    # get toy category
    toy_category = ""

    # get toys
    toys = get_top_toys(toy_category, num_of_people)

    # match addresses to toys
    address_toy_pairs = match_address_to_toys(addresses, toys)

    # return address-toy pairs
    return address_toy_pairs


def match_address_to_toys(addresses, toys):
    """
    Matches a list of addresses to a list of toys
    :param addresses: List of addresses to be matched
    :param toys: List of toys to be matched
    :return: List of address-toy pairs
    """


def get_top_toys(toy_category, num_of_people):
    """
    Generates a list of top toys in given toy category
    :param toy_category: User-defined toy category
    :param num_of_people: User-defined number of people to generate toys for
    :return: List of top toys in given category
    """


def parse_file(infile):
    """
    Takes a csv file and translates the data into requirements
    :param infile: Given input file that lists user requests
    :return:
    """

    # process the file
    file = open(infile)
    input_reader = csv.reader(file)
    request_list = list(input_reader)
    request_list = request_list[1:]         # remove the header

    return request_list


def write_output(product_list, num):
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
        outfile.write(get_header() + "\n")

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


def get_header():
    """
    Returns a header for the output file
    :return: a header for the ouptut file
    """
    header = "input_item_type,input_item_category,input_number_to_generate,output_item_name,output_item_rating," \
             "output_item_num_reviews"

    return header


def main():

    """item_type = 0
    item_category = 1
    num_to_generate = 2
    file_input = ""

    # create database
    database = Database()

    if len(sys.argv) <= 1:  # if no input file, then set to None and start GUI
        generator = GeneratorGui(database)

    else:                   # otherwise, use given input file
        file_input = sys.argv[1]

        # get requests
        requests = parse_file(file_input)

        # for each request, get top products and write to file
        for request in requests:
            num = int(request[num_to_generate])

            top_products = database.get_top_items(request[item_type], request[item_category], num)
            write_output(top_products, num)"""


# starter code
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7654)
    # main()

