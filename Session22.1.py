"""
 Mutlithreading
 It is uesd so that the load on decreases

 As we are printing covid cases data,it is a very huge data,so we make a 2 child threads who will share the
 load. And the process(both child threads i.e. class printer,fetch_data  run parallely

 So the output will be in mixed form.
 threads has two types for running - Asynchronous -> objects runs parallely
 - Synchronous -> when one object finished it's execution,then the other will start


"""

import requests
import json
import threading

class Printer(threading.Thread):

    def __init__(self, document_name=None, num_of_copies=1):

        # execute the constructor of Thread Class. Mandatory
        super().__init__()

        self.document_name = document_name
        self.num_of_copies = num_of_copies


    def run(self):
        for i in range(1, self.num_of_copies+1):
            print("## Printing document {} copy#{}".format(self.document_name, i))


class fetch_Data(threading.Thread):


    def run(self):
        url = "https://api.covid19india.org/v4/min/timeseries.min.json"
        response = requests.get(url)

        # covid_cases = json.loads(response.text)
        # print(json.dumps(covid_cases))

        print(response.text[:100])



    # def fetch_cases(self):

def main():

    print("App started")

    cases = fetch_Data()
    cases.start()

    printer = Printer(document_name="LearningPython.pdf", num_of_copies=10)
    printer.start()


    print("App finished")

if __name__ == '__main__':
    main()