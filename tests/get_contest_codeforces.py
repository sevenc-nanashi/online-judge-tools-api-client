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
                "contest_id": 999,
                "problems": [
                    {
                        "url": "https://codeforces.com/contest/999/problem/A",
                        "problem_id": "A",
                        "contest_id": 999,
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
                        "problem_id": "B",
                        "contest_id": 999,
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
                        "problem_id": "C",
                        "contest_id": 999,
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
                        "problem_id": "D",
                        "contest_id": 999,
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
                        "problem_id": "E",
                        "contest_id": 999,
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
                        "problem_id": "F",
                        "contest_id": 999,
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
