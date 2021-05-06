from utils.tools import driverHandler, writeResutlsToFile
import os
import sys

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--name", help="add the name of the question. ex. python3 main.py --name two-sum, or python3 main.py --name add-two-numbers")
args = parser.parse_args()



if __name__=='__main__':

    crawler = driverHandler(args.name) # args.name = two sum, crawler.problemName=two-sum
    question_description = crawler.descriptionParser()
    starter_code = crawler.starterCodeParser()
    crawler.quitDriver()
    writeResutlsToFile(args.name,question_description,starter_code)

    sys.exit("Finish crawling!")