#!/usr/bin/env python3

import os
import requests

# url to send data. NOTE: I found that the difference the trailing forward
# slash makes is a Server 500 error!
url = 'http://35.223.147.213/feedback/'

# path to files
path_to_files = '/data/feedback'

# list all .txt files in the path_to_files directory
list_of_files = os.listdir(path_to_files)
# print(list_of_files)

# read each  feedback and post to corpweb
for file in list_of_files:
    with open(os.path.join(path_to_files, file), 'r') as f:
        title, name, date, feedback = tuple(f.readlines())
        fb = {"title": title.strip(), "name": name.strip(), "date": date.strip(), "feedback": feedback.strip()}
        #print(fb)
        response = requests.post(url, json=fb)
        #print(response.json())
        if not response.ok:
            print("Could not add feedback. status: {}".format(response.status_code))
        else:
            print(response.status_code)

print("Done!")

