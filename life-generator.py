# Name:         Kat Kime
# Date:         February 14, 2021
# Description:  Takes an input of product data and generates the top X products.
import csv
from os import path
from database import Database
from flask import Flask, request, jsonify
import json
from json import JSONEncoder

app = Flask(__name__)


@app.route("/", methods=['POST'])
def address_toy_match():

    # Get the request
    req = request.data.decode('utf-8')
    req = json.loads(req)

    # Parse the request
    addresses = req["addresses"]
    toy_category = "Hobbies"        # Need to figure out how this will be received

    address_toy_pairs = get_address_toy_pairs(addresses, toy_category)
    print(address_toy_pairs)

    # Send JSON file of address, toy pairs
    address_toy_object = {"address_toys": address_toy_pairs}            # address_toy_pairs = [[address_1, toy_1], [address_2, toy_2], ..., [address_n, toy_n]]
    return json.dumps(address_toy_object)


def get_address_toy_pairs(addresses, toy_category):
    """
    Receives a list of addresses and returns a list of address-toy pairs
    :param addresses: Given list of addresses
    :param toy_category: User-defined category of toys from which to generate top toys from
    :return: List of address-toy pairs
    """
    # get number of addresses
    num_of_people = len(addresses)

    # get toys
    toys = get_top_toys(toy_category, num_of_people)                # encode each toy toys

    # match addresses to toys
    address_toy_pairs = match_address_to_toys(addresses, toys)

    # return address-toy pairs
    return address_toy_pairs


def get_top_toys(toy_category, num_of_people):
    """
    Generates a list of top toys in given toy category
    :param toy_category: User-defined toy category
    :param num_of_people: User-defined number of people to generate toys for
    :return: List of top toys in given category
    """
    # create a database
    toy_database = Database()

    # get top toys
    top_toys = toy_database.get_top_items("toys", toy_category, num_of_people)

    # convert toys to dictionaries
    convert_toys_to_dicts(top_toys)

    # return top toys
    return top_toys


def convert_toys_to_dicts(toys):
    """
    Converts a list of toys to their dictionary form
    :param toys: Given list of toys to convert
    """
    index = 0

    while index < len(toys):
        toys[index] = toys[index].convert_to_dict()
        index += 1


def match_address_to_toys(addresses, toys):
    """
    Matches a list of addresses to a list of toys
    :param addresses: List of addresses to be matched
    :param toys: List of toys to be matched
    :return: List of address-toy pairs
    """
    add_index = 0
    toy_index = 0

    address_toy_pairs = []

    # iterate through address list
    while add_index < len(addresses) and toy_index < len(toys):
        address_toy = [addresses[add_index], toys[toy_index]]
        address_toy_pairs.append(address_toy)

        add_index += 1
        toy_index += 1

    return address_toy_pairs


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

