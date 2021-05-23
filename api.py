import requests
import json
from collections import OrderedDict
# get question name, number, and details from api
# content = requests.get('https://leetcode.com/api/problems/algorithms/')


def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


def get_detail_api():
    content = requests.get(
        'https://leetcode.com/api/problems/algorithms/').content
    print(type(content))
    questions = json.loads(content)['stat_status_pairs']
    print(questions[0])

def get_question():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
        'Host': 'leetcode.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36',
        'Referer': 'https://leetcode.com/accounts/login/',
    }
    extra_headers = {
        # 'Origin': BASE_URL,
        # 'Referer': BASE_URL,
        # 'X-CSRFToken': self.auth.cookies["csrftoken"],
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json',
    }
    new_headers = merge_two_dicts(extra_headers, headers)

    query = """{
        user {
            username
            email
            isCurrentUserVerified
            isCurrentUserPremium
            __typename
        }
    }"""

    query = """query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            title
            titleSlug
            questionId
            content
            difficulty
            stats
            companyTagStats
            topicTags {
                name
                slug
                __typename
            }
            similarQuestions
            codeSnippets {
                lang
                langSlug
                code
                __typename
            }
            solution {
                id
                canSeeDetail
                __typename
            }
            sampleTestCase
            enableTestMode
            metaData
            enableRunCode
            judgerAvailable
            __typename
        }
    }"""
    body = {
        'query': query,
        'operationName': "questionData",
        'variables': {'titleSlug': 'two-sum'}
    }

    url = 'https://leetcode.com/graphql'
    r = requests.post(url, headers=new_headers, data=json.dumps(body))
    content = json.loads(r.text)
    question = content["data"]["question"]["content"]
    return question

def get_codeSnippets():
    sample_code = content["data"]["question"]["codeSnippets"]
    code = ""
    for i in sample_code:
        if i["lang"] == 'Python':
            code = i["code"]

    print(code)

def submit(self, id):
    code = self.get_code_from_quiz_id(id)
    success, text_or_id = quiz.submit(code)
    if success:
        code = 1
        while code > 0:
            r = quiz.check_submission_result(text_or_id)
            code = r[0]

        if code < -1:
            return (False, r[1])
        else:
            return (True, _submit_result_prettify(r[1]))
    else:
        return (False, 'send data failed!')

def _submit_result_prettify(result):
    prettified = OrderedDict()
    if 'status_code' not in result:
        prettified['status'] = 'Unknow result format: %s' % json.dumps(result)
    if result['status_code'] == 20:
        prettified['status'] = 'Compile error'
        prettified['Your input'] = ''
        prettified['Your answer'] = result['compile_error']
        prettified['Expected answer'] = 'Unknown error'
    elif result['status_code'] == 10:
        prettified['status'] = 'Accepted'
        prettified['Run time'] = result['status_runtime']
    elif result['status_code'] == 11:
        prettified['status'] = 'Wrong answer'
        s = result['compare_result']
        prettified['Passed test cases'] = '%d/%d' % (s.count('1'), len(s))
        prettified['Your input'] = result['input']
        prettified['Your answer'] = result['code_output']
        prettified['Expected answer'] = result['expected_output']
    elif result['status_code'] == 12:  # memeory limit exceeded
        prettified['status'] = 'Memory Limit Exceeded'
    elif result['status_code'] == 13:  # output limit exceeded
        prettified['status'] = 'Output Limit Exceeded'
    elif result['status_code'] == 14:  # timeout
        prettified['status'] = 'Time Limit Exceeded'
    elif result['status_code'] == 15:
        prettified['status'] = 'Runtime error'
        prettified['Runtime error message'] = result['runtime_error']
        prettified['Last input'] = result['last_testcase']
    else:
        prettified['status'] = 'Unknown status'
    return prettified

class quiz():
    def __init__(self) -> None:
        pass
    def submit(self, code):
        if not self.auth.is_login:
            return (False, "")
        body = {'question_id': self.id,
                'test_mode': False,
                'lang': LANG_MAPPING.get(config.language, 'cpp'),
                'judge_type': 'large',
                'typed_code': code}

        csrftoken = self.auth.cookies['csrftoken']
        extra_headers = {'Origin': BASE_URL,
                         'Referer': self.url + '/?tab=Description',
                         'DNT': '1',
                         'Content-Type': 'application/json;charset=UTF-8',
                         'Accept': 'application/json',
                         'X-CSRFToken': csrftoken,
                         'X-Requested-With': 'XMLHttpRequest'}

        newheaders = merge_two_dicts(headers, extra_headers)

        r = self.auth.retrieve(self.url + '/submit/', method='POST', data=json.dumps(body), headers=newheaders)
        if r.status_code != 200:
            return (False, 'Request failed!')
        text = r.text.encode('utf-8')
        try:
            data = json.loads(text)
        except Exception:
            return (False, text)

        if 'error' in data:
            return (False, data['error'])
        return (True, data['submission_id'])
        
    def check_submission_result(self, submission_id):
        url = SUBMISSION_URL.format(id=submission_id)
        r = self.auth.retrieve(url)
        if r.status_code != 200:
            return (-100, 'Request failed!')
        text = r.text.encode('utf-8')
        data = json.loads(text)
        try:
            if data['state'] == 'PENDING':
                return (1,)
            elif data['state'] == 'STARTED':
                return (2,)
            elif data['state'] == 'SUCCESS':
                if 'run_success' in data:
                    if data['run_success']:
                        return (0, data)  # data['total_correct'], data['total_testcases'], data['status_runtime'])
                    else:
                        return (-1, data)  # data['compile_error'])
                else:
                    raise KeyError
        except KeyError:
            return (-2, 'Unknow error')
# print(sample_code)


# 設定 cookie
# my_cookies = dict(my_cookie_name='G. T. Wang')

# # 將 cookie 加入 GET 請求
# r = requests.get("http://httpbin.org/cookies", cookies = my_cookies)
# print(r.content)
