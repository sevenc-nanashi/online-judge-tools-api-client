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
                "contest_id": "COOK131B",
                "problems": [{
                    "url": "https://www.codechef.com/COOK131B/problems/SHOEFIT",
                    "problem_id": "SHOEFIT",
                    "contest_id": "COOK131B",
                    "name": "Shoe Fit",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/CHFGCD",
                    "problem_id": "CHFGCD",
                    "contest_id": "COOK131B",
                    "name": "Chef and GCD",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/XORORED",
                    "problem_id": "XORORED",
                    "contest_id": "COOK131B",
                    "name": "XOR-ORED",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/CHFPLN",
                    "problem_id": "CHFPLN",
                    "contest_id": "COOK131B",
                    "name": "Chef In Infinite Plane",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/MODEQUAL",
                    "problem_id": "MODEQUAL",
                    "contest_id": "COOK131B",
                    "name": "Mod Equality",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/BEAUSUB",
                    "problem_id": "BEAUSUB",
                    "contest_id": "COOK131B",
                    "name": "Beautiful Subsequence",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/COLRGRPH",
                    "problem_id": "COLRGRPH",
                    "contest_id": "COOK131B",
                    "name": "Hidden Colored Graph",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/MATBEAUT",
                    "problem_id": "MATBEAUT",
                    "contest_id": "COOK131B",
                    "name": "Make the Matrix Beautiful",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/SPTREE2",
                    "problem_id": "SPTREE2",
                    "contest_id": "COOK131B",
                    "name": "A Special Tree 2",
                    "context": {
                        "contest": {
                            "name": "July Cook-Off 2021 Division 2",
                            "url": "https://www.codechef.com/COOK131B"
                        }
                    }
                }, {
                    "url": "https://www.codechef.com/COOK131B/problems/GCDLEN",
                    "problem_id": "GCDLEN",
                    "contest_id": "COOK131B",
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
