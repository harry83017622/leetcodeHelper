from utils.tools import driverHandler
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

    if os.path.exists(crawler.problemName+'.py'):
        print('{}.py exists'.format(crawler.problemName))
    else:
        try:
            print ("create {} file".format(crawler.problemName))
            with open(crawler.problemName+'.py', "w", encoding="utf-8") as file:
                file.write("''' \n" + question_description + "\n'''" + starter_code)
        except NameError:
            print('content is None. Try again or use different keywords!')
    sys.exit("Finish crawling!")