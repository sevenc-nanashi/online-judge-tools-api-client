import unittest

from onlinejudge_api.main import main


class GetContestCodeChefTest(unittest.TestCase):
    def test_cook131b(self):
        url = "https://www.codechef.com/COOK131B"
        expected = {
            "status": "ok",
            "messages": [],
            "result": {
                "url": "https://www.codechef.com/COOK131B",
                "contestId": "COOK131B",
                "problems": [{
                    "url": "https://www.codechef.com/COOK131B/problems/SHOEFIT",
                    "problemId": "SHOEFIT",
                    "contestId": "COOK131B",
                    "name": "Shoe Fit",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/CHFGCD",
                    "problemId": "CHFGCD",
                    "contestId": "COOK131B",
                    "name": "Chef and GCD",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/XORORED",
                    "problemId": "XORORED",
                    "contestId": "COOK131B",
                    "name": "XOR-ORED",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/CHFPLN",
                    "problemId": "CHFPLN",
                    "contestId": "COOK131B",
                    "name": "Chef In Infinite Plane",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/MODEQUAL",
                    "problemId": "MODEQUAL",
                    "contestId": "COOK131B",
                    "name": "Mod Equality",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/BEAUSUB",
                    "problemId": "BEAUSUB",
                    "contestId": "COOK131B",
                    "name": "Beautiful Subsequence",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/COLRGRPH",
                    "problemId": "COLRGRPH",
                    "contestId": "COOK131B",
                    "name": "Hidden Colored Graph",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/MATBEAUT",
                    "problemId": "MATBEAUT",
                    "contestId": "COOK131B",
                    "name": "Make the Matrix Beautiful",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/SPTREE2",
                    "problemId": "SPTREE2",
                    "contestId": "COOK131B",
                    "name": "A Special Tree 2",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/GCDLEN",
                    "problemId": "GCDLEN",
                    "contestId": "COOK131B",
                    "name": "Maximal GCD",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }],
                "name": "July Cook-Off 2021 Division 2"
            },
        }
        actual = main(['get-contest', url], debug=True)
        self.assertEqual(expected, actual)
