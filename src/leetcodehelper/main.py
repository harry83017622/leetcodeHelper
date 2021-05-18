from leetcodehelper.utils.tools import driverHandler, writeResutlsToFile
from leetcodehelper.driver import installer
import sys

import argparse

def entry():
    parser = argparse.ArgumentParser()
    parser.add_argument("--init",action='store_true', help="initial the current folder as the work folder and install the webdriver from the crawler")
    parser.add_argument("--name", help="add the name of the question. ex. python3 main.py --name two-sum, or python3 main.py --name add-two-numbers")
    args = parser.parse_args()

    if args.init:
        installer.run()
    else:
        crawler = driverHandler(args.name) # args.name = two sum, crawler.problemName=two-sum
        question_description = crawler.descriptionParser()
        starter_code = crawler.starterCodeParser()
        crawler.quitDriver()
        writeResutlsToFile(args.name,question_description,starter_code)

        sys.exit("Finish crawling!")