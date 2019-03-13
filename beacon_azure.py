# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:01:36 2019

@author: AOR2KOR aka Rohan Saha - SimpleParadox
"""


# Importing modules. Note: You will see errors for the imports because the modules are for micropython.
import urequests as requests 
import network
import ujson as json
import ubinascii
import gc

# Making sure the WiFi Module(Network Interface Card) is active
nic = network.WLAN(network.STA_IF)
nic.active(True)

# Defining the Endpoint. Which is the API.
url = 'https://beaconapi-simpleparadox.azurewebsites.net/addtask'

# Connecting to an access point
if not nic.isconnected():
    nic.connect('<ap_name>', '<password>')

count = 1

while 1:
    # Run indefinitely while the power the supplied to the module.

    # Scanning the environment for accesspoints
    scan_results = nic.scan()
    results_length = len(scan_results)
    data = {}

    # Formatting the data before sending to Azure
    for i in range(results_length):
        data[str(ubinascii.hexlify(scan_results[i][1]))[1:]] = str(scan_results[i][3])
    
    # Formatting the data according to the data model set in the API.
    payload = {'name':str(count), 'category': str(data)}

    # Trying a post request to the url specified.
    try:
        requests.post(url, '<data>')
    except Exception as e:
        # Log errors
        print(e)
    # Deleting the variables to save memory.
    del data
    del scan_results
    gc.collect() # Collecting any garbage if created.
        