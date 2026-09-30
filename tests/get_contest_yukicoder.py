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
                "contest_id": 294,
                "name": "yukicoder contest 277",
                "problems": [
                    {
                        "url": "https://yukicoder.me/problems/5033",
                        "problem_id": 5033,
                        "contest_id": 294,
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
                        "problem_id": 5191,
                        "contest_id": 294,
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
                        "problem_id": 5203,
                        "contest_id": 294,
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
                        "problem_id": 5229,
                        "contest_id": 294,
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
                        "problem_id": 5436,
                        "contest_id": 294,
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
                        "problem_id": 5459,
                        "contest_id": 294,
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
