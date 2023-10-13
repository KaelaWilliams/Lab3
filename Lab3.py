"""
 Name: Kaela Williams & Jevan Wilskey
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: Fall 2023
 Instructor: Dr. Cao
 Date: 10/12/23
 Sources consulted: any books, individuals, etc consulted

 Known Bugs: description of known bugs and other program imperfections

 Creativity: anything extra that you added to the lab

 Instructions: instructions to user on how to execute your program

"""
import sys
import argparse
import math
import random

def splitData(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store the first 7000 of them in trainData, and the rest 3000 in testData
    Instruction:
            There is no grading script for this function, because different group may select different dataset depending on their course project, but generally you should make sure that you code can divide the dataset correctly, since you may use it for the course project
    """
    # your code here
    data_file = open(data, "r")
    data_label = data_file.readline()
    data_lines = []
    for line in data_file:
        data_lines.append(line)
    data_file.close()

    train_length = int(len(data_lines) * float(ratio))
    test_length = int(len(data_lines) * (1 - float(ratio)))

    train_file = open(trainData, "w")
    train_file.write(str(data_label))
    for i in range(train_length):
        train_file.write(str(data_lines.pop()))
    train_file.close()

    test_file = open(testData, 'w')
    test_file.write(str(data_label))
    for i in range(test_length):
        test_file.write(str(data_lines.pop()))
    test_file.close()    


def splitDataRandom(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store 7000 of them in trainData, and 3000 in testData.
    Instruction:
            Almost same as splitData, the only difference is this function will randomly shuffle the input data, so you will randomly select data and store it in the trainData
    """
    # your code here
    data_file = open(data, "r")
    data_label = data_file.readline()
    data_lines = []
    for line in data_file:
        data_lines.append(line)
    data_file.close()

    train_length = int(len(data_lines) * float(ratio))
    test_length = int(len(data_lines) * (1 - float(ratio)))
    train_current = 0
    test_current = 0

    train_file = open(trainData, "w")
    train_file.write(str(data_label))
    test_file = open(testData, 'w')
    test_file.write(str(data_label))
    for i in data_lines:
        file = random.randint(1,2)
        if file == 1:
            if train_current != train_length:
                train_file.write(str(data_lines.pop()))
                train_current = train_current+1
            else:
                test_file.write(str(data_lines.pop()))
        else:
            if test_current != test_length:
                test_file.write(str(data_lines.pop()))
                test_current = test_current+1
            else:
                train_file.write(str(data_lines.pop()))
    train_file.close()
    test_file.close() 



def main():
    options = parser.parse_args()
    mode = options.mode       # first get the mode
    print("mode is " + mode)
    """
    similar to Lab 2, please add your testing code here
    """
    # your code here
    data = options.data
    trainData = options.trainData
    testData = options.testData
    ratio = options.ratio
    if data == '' or trainData == '' or testData == '' or ratio == '':
        showHelper()
    if mode == 'N':
        splitData(data, trainData, testData, ratio)
    elif mode == 'R':
        splitDataRandom(data, trainData, testData, ratio)
    pass


def showHelper():
    """
    Similar to Lab 2, please update the showHelper function to show users how to use your code
    """
    parser.print_help(sys.stderr)
    print("Please provide input augument. Here are examples:")
    print("python "+sys.argv[0]+" --mode R --data Hopsital_Dataset.csv --testData test.csv --trainData train.csv --ratio 0.5")
    print("python "+sys.argv[0]+" --mode N --data Hopsital_Dataset.csv --testData test.csv --trainData train.csv --ratio 0.2")

    sys.exit(0)


if __name__ == "__main__":
    #------------------------arguments------------------------------#
    #Shows help to the users                                        #
    #---------------------------------------------------------------#
    parser = argparse.ArgumentParser()
    parser._optionals.title = "Arguments"
    parser.add_argument('--mode', dest='mode',
    default = '',    # default empty!
    help = 'Mode: R for random splitting, and N for the normal splitting')

    """
    Similar to Lab 2, please update the argument, and add as you need
    """
    # your code here
    parser.add_argument('--data', dest='data',
    default = '',    # default empty!
    help = 'The original data file')
    parser.add_argument('--testData', dest='testData',
    default = '',    # default empty!
    help = 'The file for testing data used to test the model')
    parser.add_argument('--trainData', dest='trainData',
    default = '',    # default empty!
    help = 'The file for the training data used to build the model')
    parser.add_argument('--ratio', dest='ratio',
    default = '',    # default empty!
    help = 'The ratio of how much of the data should be used for training. A number between 0.0 and 1.0')
    
    if len(sys.argv)<3:
        showHelper()
    main()
