#!/usr/bin/env python3
import tkinter as tk
import csv
import random
import sys
from flask import Flask, jsonify, request
import json
import requests

inputList = []


window = tk.Tk()
random.seed()
fullAddress = []
states = [
'Alaska',
'Arizona',
'California',
'Colorado',
'Hawaii',
'Idaho',
'Montana',
'New Mexico',
'Nevada',
'Oregon',
'Utah',
'Washington',
'Wyoming'
]

stateDict = {
'Alaska': 'ak.csv',
'Arizona': 'az.csv',
'California': 'ca.csv',
'Colorado': 'co.csv',
'Hawaii': 'hi.csv',
'Idaho': 'id.csv',
'Montana': 'mt.csv',
'New Mexico': 'nm.csv',
'Nevada': 'nv.csv',
'Oregon': 'or.csv',
'Utah': 'ut.csv',
'Washington': 'wa.csv',
'Wyoming': 'wy.csv'
}

def getInfo(state, num):
    state = stateDict[state]
    addylist = []
    outList= []
    file = open(state, 'r')
    reader = csv.reader(file, delimiter=',')
    rowCount = len(list(reader))
    file.close()
    file = open(state, 'r')
    line = 0
    new = csv.reader(file, delimiter=',')
    for row in new:
        if line == 0:
            line += 1
        else:
            addylist.append(row)    
    file.close()
    for x in range(num):
        addynum = random.randrange(rowCount)
        outList.append(addylist[addynum])
    return outList


def submitInfo(event):
    state = variable.get()
    addycount = int(num.get())
    infoList = getInfo(state, addycount)
    addressList = tk.Listbox(width=50)
    for idx, val in enumerate(infoList):
        addressList.insert(idx, val[0] + ' ' + val[1] + ' ' + val[2] + ' ' + val[3] + ' ' + val[4])    
    addressList.pack()
    output(state, addycount, infoList)

    address_toy_pairs = sendRequest(state, addycount)
    addressToyList = tk.Listbox(width=150)
    for idx, val in enumerate(address_toy_pairs):
        addressToyList.insert(idx, val)
    addressToyList.pack()
    window.update()
    return



def output(state, num, infoList):
    outfile = open('../output.csv', 'w')
    names = ['input_state','input_number_to_generate','output_content_type','output_content_value']
    writer = csv.DictWriter(outfile, fieldnames=names, lineterminator = '\n')
    writer.writeheader()
    info = []
    for x in range(len(infoList)):
        info.append(infoList[x][0] + ' ' + infoList[x][1] + ' ' + infoList[x][2] + ' ' + infoList[x][3] + ' ' + infoList[x][4])
    for i in info:
        writer.writerow({'input_state':state,'input_number_to_generate':num,'output_content_type':'street address','output_content_value':i})

def requestSetup(state, num):
    addressList = []
    for addy in getInfo(state, num):
        string = ""
        for x in addy:
            string += x + " "       
        addressList.append(string)
    addresses = {"addresses": addressList}
    parameters = json.dumps(addresses)
    return parameters

def sendRequest(state, num):
    # testing parameters
    parameters = requestSetup(state, num)
    response = requests.post('http://127.0.0.1:7654', data=parameters)
    data = json.loads(response.text)
    if (data["address_toys"]):
        address_toy_pairs = []
        print("Received address toy pairs")
        print("Here is the list: ")
        for item in data["address_toys"]:
            string = item[0]
            string += " Item: " + item[1]['item_name']
            address_toy_pairs.append(string)
            print(string)
    return address_toy_pairs


if len(sys.argv) == 2:
    if (sys.argv[1] == "comms"):
        print("nah")
    else:
        infile = open(sys.argv[1], 'r')
        inreader = csv.reader(infile, delimiter=',')
        line = 0
        for row in inreader:
            if line == 0:
                line += 1
            else:
                inputList.append(row)
        outfile = open('../output.csv', 'w')
        names = ['input_state','input_number_to_generate','output_content_type','output_content_value']
        writer = csv.DictWriter(outfile, fieldnames=names, lineterminator = '\n')
        writer.writeheader()
        for i in inputList:
            infoList = getInfo(i[0],int(i[1]))
            '''
            address = []
            for x in range(len(infoList)):
                address.append(infoList[x][0] + ' ' + infoList[x][1] + ' ' + infoList[x][2] + ' ' + infoList[x][3] + ' ' + infoList[x][4])
            '''
            output(i[0], i[1], infoList)
        outfile.close()
        infile.close()
else:
    variable = tk.StringVar(window)
    variable.set(states[0])
    selectState = tk.OptionMenu(window, variable, *states)
    greeting = tk.Label(text="Person Generator")
    selectLabel = tk.Label(text="Please Select the state you would like to get results from")
    numLabel = tk.Label(text="Please type the number of addresses you would like to receive")
    num = tk.Entry()
    submit = tk.Button(text="Submit")
    submit.bind("<Button-1>", submitInfo)


    greeting.pack()
    selectLabel.pack()
    selectState.pack()
    numLabel.pack()
    num.pack()
    submit.pack()
    window.mainloop()