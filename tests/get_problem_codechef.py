import unittest

from onlinejudge_api.main import main


class GetProblemCodeChefTest(unittest.TestCase):
    def test_xorored(self):
        url = 'https://www.codechef.com/COOK131B/problems/XORORED'
        expected = {
            "status": "ok",
            "messages": [],
            "result": {
                "name": "XOR-ORED",
                "url": "https://www.codechef.com/COOK131B/problems/XORORED",
                "problemId": "XORORED",
                "contestId": "COOK131B",
                "tests": [{
                    "input": "1\n2\n4 6\n",
                    "output": "6 2\n"
                }],
                "context": {}
            },
        }
        actual = main(['get-problem', url], debug=True)
        self.assertEqual(expected, actual)
