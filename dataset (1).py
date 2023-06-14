
import numpy as np
import matplotlib as pyplt

def load_data():
    #load data from csv file, we use 'genfromtxt' because numpy is designed to work with numbers and not strings
    data = np.genfromtxt('./Training Data/tic-tac-toe copy.csv', delimiter = ',', dtype = 'str')

    #so we convert the data to numbers
    #lets assign 'x' = 4, 'b' = 5, 'o' = 6, 'positive' = '1' and 'negative' = '0'
    data[data == 'x'] = int(4)
    data[data == 'b'] = 5
    data[data == 'o'] = 6
    data[data == 'positive'] = 1
    data[data == 'negative'] = 0
    
    #converting all data in array to datatype float
    data = data.astype(int)

    #splitting the features and outputs into seperate arrays
    x = data[:, 0:9]
    y = data[:, 9:]

    #print(data[1])
    #print(x[:10])
    #print(y[:10])

    #converting 1-D array to 2-D array
    #x = np.expand_dims(x, axis = 1)
    #y = np.expand_dims(y, axis = 1)

    return(x, y)

