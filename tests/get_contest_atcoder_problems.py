import unittest

from onlinejudge_api.main import main


class GetContestAtCoderProblemsTest(unittest.TestCase):
    def test_21fb8ee5(self):
        url = 'https://kenkoooo.com/atcoder/#/contest/show/21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf'
        expected = {
            "status": "ok",
            "messages": [],
            "result": {
                "url": "https://kenkoooo.com/atcoder/#/contest/show/21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                "contest_id": "21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                "name": "\u3042\u3055\u304b\u306411/19",
                "problems": [
                    {
                        "url": "https://atcoder.jp/contests/abc164/tasks/abc164_c",
                        "problem_id": "abc164_c",
                        "contest_id": "21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                        "name": "C. gacha",
                        "context": {
                            "contest": {
                                "url": "https://kenkoooo.com/atcoder/#/contest/show/21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                                "name": "\u3042\u3055\u304b\u306411/19"
                            },
                            "alphabet": "0"
                        }
                    },
                    {
                        "url": "https://atcoder.jp/contests/tenka1-2014-quala/tasks/tenka1_2014_qualA_a",
                        "problem_id": "tenka1_2014_qualA_a",
                        "contest_id": "21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                        "name": "A. \u5929\u4e0b\u4e00\u5e8f\u6570",
                        "context": {
                            "contest": {
                                "url": "https://kenkoooo.com/atcoder/#/contest/show/21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                                "name": "\u3042\u3055\u304b\u306411/19"
                            },
                            "alphabet": "1"
                        }
                    },
                    {
                        "url": "https://atcoder.jp/contests/abc060/tasks/arc073_a",
                        "problem_id": "arc073_a",
                        "contest_id": "21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                        "name": "C. Sentou",
                        "context": {
                            "contest": {
                                "url": "https://kenkoooo.com/atcoder/#/contest/show/21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                                "name": "\u3042\u3055\u304b\u306411/19"
                            },
                            "alphabet": "2"
                        }
                    },
                    {
                        "url": "https://atcoder.jp/contests/abc140/tasks/abc140_d",
                        "problem_id": "abc140_d",
                        "contest_id": "21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                        "name": "D. Face Produces Unhappiness",
                        "context": {
                            "contest": {
                                "url": "https://kenkoooo.com/atcoder/#/contest/show/21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                                "name": "\u3042\u3055\u304b\u306411/19"
                            },
                            "alphabet": "3"
                        }
                    },
                    {
                        "url": "https://atcoder.jp/contests/abc062/tasks/arc074_a",
                        "problem_id": "arc074_a",
                        "contest_id": "21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                        "name": "C. Chocolate Bar",
                        "context": {
                            "contest": {
                                "url": "https://kenkoooo.com/atcoder/#/contest/show/21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                                "name": "\u3042\u3055\u304b\u306411/19"
                            },
                            "alphabet": "4"
                        }
                    },
                    {
                        "url": "https://atcoder.jp/contests/agc026/tasks/agc026_c",
                        "problem_id": "agc026_c",
                        "contest_id": "21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                        "name": "C. String Coloring",
                        "context": {
                            "contest": {
                                "url": "https://kenkoooo.com/atcoder/#/contest/show/21fb8ee5-c293-4c5b-8d3d-9169afdf6fcf",
                                "name": "\u3042\u3055\u304b\u306411/19"
                            },
                            "alphabet": "5"
                        }
                    },
                ]
            },
        }
        actual = main(['get-contest', url], debug=True)
        self.assertEqual(expected, actual)
