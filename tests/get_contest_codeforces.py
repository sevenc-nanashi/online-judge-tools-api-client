import unittest

from onlinejudge_api.main import main


class GetContestAtCoderProblemsTest(unittest.TestCase):
    def test_21fb8ee5(self):
        url = 'https://codeforces.com/contest/999'
        expected = {
            "status": "ok",
            "messages": [],
            "result": {
                "url": "https://codeforces.com/contest/999",
                "contestId": "999",
                "problems": [
                    {
                        "url": "https://codeforces.com/contest/999/problem/A",
                        "problemId": "A",
                        "contestId": "999",
                        "name": "Mishka and Contest",
                        "context": {
                            "contest": {
                                "name": "Codeforces Round 490 (Div. 3)",
                                "url": "https://codeforces.com/contest/999"
                            },
                            "alphabet": "A"
                        }
                    },
                    {
                        "url": "https://codeforces.com/contest/999/problem/B",
                        "problemId": "B",
                        "contestId": "999",
                        "name": "Reversing Encryption",
                        "context": {
                            "contest": {
                                "name": "Codeforces Round 490 (Div. 3)",
                                "url": "https://codeforces.com/contest/999"
                            },
                            "alphabet": "B"
                        }
                    },
                    {
                        "url": "https://codeforces.com/contest/999/problem/C",
                        "problemId": "C",
                        "contestId": "999",
                        "name": "Alphabetic Removals",
                        "context": {
                            "contest": {
                                "name": "Codeforces Round 490 (Div. 3)",
                                "url": "https://codeforces.com/contest/999"
                            },
                            "alphabet": "C"
                        }
                    },
                    {
                        "url": "https://codeforces.com/contest/999/problem/D",
                        "problemId": "D",
                        "contestId": "999",
                        "name": "Equalize the Remainders",
                        "context": {
                            "contest": {
                                "name": "Codeforces Round 490 (Div. 3)",
                                "url": "https://codeforces.com/contest/999"
                            },
                            "alphabet": "D"
                        }
                    },
                    {
                        "url": "https://codeforces.com/contest/999/problem/E",
                        "problemId": "E",
                        "contestId": "999",
                        "name": "Reachability from the Capital",
                        "context": {
                            "contest": {
                                "name": "Codeforces Round 490 (Div. 3)",
                                "url": "https://codeforces.com/contest/999"
                            },
                            "alphabet": "E"
                        }
                    },
                    {
                        "url": "https://codeforces.com/contest/999/problem/F",
                        "problemId": "F",
                        "contestId": "999",
                        "name": "Cards and Joy",
                        "context": {
                            "contest": {
                                "name": "Codeforces Round 490 (Div. 3)",
                                "url": "https://codeforces.com/contest/999"
                            },
                            "alphabet": "F"
                        }
                    },
                ],
                "name": "Codeforces Round 490 (Div. 3)"
            },
        }
        actual = main(['get-contest', url], debug=True)
        self.assertEqual(expected, actual)
