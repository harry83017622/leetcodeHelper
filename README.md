# **LeetcodeHelper**

## **Description**
---  
This project is a leetcode helper toolkit. This toolkit help you to leetcode without actually


## **Getting Start**
---  
#### **Prerequisites**

* Windows 10, python3.9 (maybe >=3.6 is fine).
* Linux and Docker will be supported ASAP.
* pip or conda
* chrome version 90.0.4430


#### **Installation**

    git clone https://github.com/harry83017622/leetcodeHelper.git

    Install pip packages

    pip install -r requirements.txt

#### **Usage**

For now, you can only crawl leetcode website by entering correct question names. For example:  
```
python3 main.py --name two-sum  
python3 main.py --name add-two-numbers
python3 main.py --name median-of-two-sorted-arrays
```
Then question description and starter code will be automatically generated into question-name.py file. Now, you can leetcode whenever in your preferred IDE.
## **To Do**
---  
* Crawl by the Number/Tag/Level/Category of the questions.
* Post your code back to leetcode platform and check all testcases. Retreive results.  
* Docker and Linux compatibility