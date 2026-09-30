import unittest

from onlinejudge_api.main import main


class GetContestYukicoderTest(unittest.TestCase):
    def test_294(self):
        url = 'https://yukicoder.me/contests/294'
        expected = {
            "status": "ok",
            "messages": [],
            "result": {
                "url": "https://yukicoder.me/contests/294",
                "contestId": "294",
                "name": "yukicoder contest 277",
                "problems": [
                    {
                        "url": "https://yukicoder.me/problems/5033",
                        "problemId": "5033",
                        "contestId": "294",
                        "name": "Square Sqsq",
                        "context": {
                            "contest": {
                                "name": "yukicoder contest 277",
                                "url": "https://yukicoder.me/contests/294"
                            },
                            "alphabet": "A"
                        }
                    },
                    {
                        "url": "https://yukicoder.me/problems/5191",
                        "problemId": "5191",
                        "contestId": "294",
                        "name": "Multiply or Divide",
                        "context": {
                            "contest": {
                                "name": "yukicoder contest 277",
                                "url": "https://yukicoder.me/contests/294"
                            },
                            "alphabet": "B"
                        }
                    },
                    {
                        "url": "https://yukicoder.me/problems/5203",
                        "problemId": "5203",
                        "contestId": "294",
                        "name": "Moving Penguin",
                        "context": {
                            "contest": {
                                "name": "yukicoder contest 277",
                                "url": "https://yukicoder.me/contests/294"
                            },
                            "alphabet": "C"
                        }
                    },
                    {
                        "url": "https://yukicoder.me/problems/5229",
                        "problemId": "5229",
                        "contestId": "294",
                        "name": "Range Nearest Query",
                        "context": {
                            "contest": {
                                "name": "yukicoder contest 277",
                                "url": "https://yukicoder.me/contests/294"
                            },
                            "alphabet": "D"
                        }
                    },
                    {
                        "url": "https://yukicoder.me/problems/5436",
                        "problemId": "5436",
                        "contestId": "294",
                        "name": "Squared Sum",
                        "context": {
                            "contest": {
                                "name": "yukicoder contest 277",
                                "url": "https://yukicoder.me/contests/294"
                            },
                            "alphabet": "E"
                        }
                    },
                    {
                        "url": "https://yukicoder.me/problems/5459",
                        "problemId": "5459",
                        "contestId": "294",
                        "name": "Multiply or Add",
                        "context": {
                            "contest": {
                                "name": "yukicoder contest 277",
                                "url": "https://yukicoder.me/contests/294"
                            },
                            "alphabet": "F"
                        }
                    },
                ]
            },
        }
        actual = main(['get-contest', url], debug=True)
        self.assertEqual(expected, actual)
