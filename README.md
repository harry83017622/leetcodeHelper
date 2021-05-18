[![PyPI - Python](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8|%203.9-blue.svg)](https://pypi.org/project/KeyExtractor/)
[![PyPI - PyPi](https://img.shields.io/pypi/v/leetcodeHelper)](https://pypi.org/project/leetcodeHelper/)

**This project helps you to do leetcode with your preferred IDE or editor with command-line interface (CLI).**
<br></br>
## **Getting Start**
---  
#### **Prerequisites**

* Windows 10, MacOS, Linux
* chrome version >=90.0.4430


#### **Installation**

```
# Prepare your virtual environment
conda create --name [env_name] python=3.9
conda activate [env_name]

# Install this package
pip install leetcodeHelper
```

#### **Usage**

```
# This command helps to load Chrome driver for you 
leetcode --init

# This CLI supports querying problems by names
leetcode --name two-sum  
leetcode --name add-two-numbers
leetcode --name median-of-two-sorted-arrays
```
Then question description and starter code will be automatically generated into question-name.py file. Now, you can do leetcode whenever in your preferred IDE.
<br></br>
## **Acknowledgments**
---
The part of Chrome driver installation is modified from [**@peterhudec**](https://github.com/authomatic/chromedriver_installer) project.  
Also, this project is inspired by [**@allenyummy**](https://github.com/allenyummy/KeyExtractor)'s project.  
<br></br>

## **Next release version**
---  
* Fix the format error in the result file (change line missing).
* Crawl by the Number/Tag/Level/Category of the questions.
* Post your code back to leetcode platform and check all testcases. Retreive results.  
* Docker version