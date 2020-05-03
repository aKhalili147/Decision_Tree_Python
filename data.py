import csv
import numpy as np 

class Data:

    in_data = [[] for x in range(2)]

    def __init__(self,path):
        self.path = path

    def read_data(self):
        
        # reading csv file to a list
        with open(self.path,'r') as file:
            reader = csv.reader(file)
            self.in_data = list(reader)

        # parsing data 
        for instance in self.in_data:
            for i in range(len(instance)):
                if i != 4:
                    instance[i] = float(instance[i])

        # self.print_data()

        return self.in_data

    def sort_data(self, index):
        return sorted(self.in_data, key=lambda x: x[index])

    def print_data(self,arr):
        for instance in arr:
            print(instance)

    def get_nrows(self,arr):
        cnt = 0
        for row in arr: cnt+=1
        return cnt

    def get_ncols(self,arr):
        cnt = 0
        for row in arr[0]: cnt+=1
        return cnt