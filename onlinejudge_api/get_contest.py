import json
from typing import *

import onlinejudge.dispatch
from onlinejudge.service.atcoder import AtCoderContest
from onlinejudge.service.atcoder_problems import AtCoderProblemsContest
from onlinejudge.service.codechef import CodeChefContest
from onlinejudge.service.codeforces import CodeforcesContest
from onlinejudge.service.yukicoder import YukicoderContest
from onlinejudge.type import *
from onlinejudge_api.get_problem import get_problem_ids

schema_example = {
    "contest_id": "cf16-exhibition",
    "url": "https://atcoder.jp/contests/cf16-exhibition",
    "name": "CODE FESTIVAL 2016 Exhibition",
    "problems": [
        {
            "problem_id": "codefestival_2016_ex_a",
            "contest_id": "cf16-exhibition",
            "url": "https://atcoder.jp/contests/cf16-exhibition/tasks/codefestival_2016_ex_a",
            "name": "Distance Pairs",
            "context": {
                "contest": {
                    "url": "https://atcoder.jp/contests/cf16-exhibition",
                    "name": "CODE FESTIVAL 2016 Exhibition",
                },
                "alphabet": "A",
            }
        },
        {
            "problem_id": "codefestival_2016_ex_b",
            "contest_id": "cf16-exhibition",
            "url": "https://atcoder.jp/contests/cf16-exhibition/tasks/codefestival_2016_ex_b",
            "name": "Exact Payment",
            "context": {
                "contest": {
                    "url": "https://atcoder.jp/contests/cf16-exhibition",
                    "name": "CODE FESTIVAL 2016 Exhibition",
                },
                "alphabet": "B",
            }
        },
    ],
}  # type: Dict[str, Any]

schema = {
    "$schema": "http://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "contest_id": {
            "type": "string",
        },
        "url": {
            "type": "string",
            "format": "uri",
        },
        "problems": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "problem_id": {
                        "type": "string",
                    },
                    "contest_id": {
                        "type": "string",
                    },
                    "url": {
                        "type": "string",
                        "format": "uri",
                    },
                    "name": {
                        "type": "string",
                    },
                    "context": {
                        "type": "object",
                        "properties": {
                            "contest": {
                                "type": "object",
                                "properties": {
                                    "url": {
                                        "type": "string",
                                        "format": "uri",
                                    },
                                    "name": {
                                        "type": "string",
                                    },
                                },
                            },
                            "alphabet": {
                                "type": "string",
                            },
                        },
                    },
                },
                "required": ["url", "name", "context"],
            },
        },
    },
    "required": ["url", "problems"],
}  # type: Dict[str, Any]


def main(contest: Contest, *, is_full: bool, session: requests.Session) -> Dict[str, Any]:
    """
    :raises Exception:
    """

    result = {
        "url": contest.get_url(),
        "problems": [],
    }  # type: Dict[str, Any]

    data = None  # type: Optional[ContestData]
    problem_data = None  # type: Optional[ProblemData]
    if isinstance(contest, AtCoderContest):
        data = contest.download_data(session=session)
        result["name"] = data.name
        for problem_data in contest.list_problem_data(session=session):
            problem = problem_data.problem  # type: Problem
            data_ = {
                "url": problem.get_url(),
                "name": problem_data.name,
                "context": {
                    "contest": {
                        "name": data.name,
                        "url": contest.get_url(),
                    },
                    "alphabet": problem_data.alphabet,
                },
            }  # type: Dict[str, Any]
            result["problems"].append(data_)
        if is_full:
            result["raw"] = {
                "html": data.html.decode(),
            }

    elif isinstance(contest, CodeforcesContest):
        data = contest.download_data(session=session)
        result["name"] = data.name
        for problem_data in contest.list_problem_data(session=session):
            problem = problem_data.problem
            data_ = {
                "url": problem.get_url(),
                "name": problem_data.name,
                "context": {
                    "contest": {
                        "name": data.name,
                        "url": contest.get_url(),
                    },
                    "alphabet": problem.index,
                },
            }
            result["problems"].append(data_)
        if is_full:
            result["raw"] = {
                "json": data.json.decode(),
            }

    elif isinstance(contest, YukicoderContest):
        result = contest._download_data(session=session)
        if not is_full:
            assert 'raw' in result
            del result["raw"]

    elif isinstance(contest, AtCoderProblemsContest):
        result = contest._download_data(session=session)
        if not is_full:
            assert 'raw' in result
            del result["raw"]

    elif isinstance(contest, CodeChefContest):
        data = contest.download_data(session=session)
        result["url"] = data.url
        result["name"] = data.name
        for problem_data in data.get_problem_data():
            data_ = {
                "url": problem_data.url,
                "name": problem_data.name,
                "context": {
                    "contest": {
                        "name": data.name,
                        "url": contest.get_url(),
                    },
                },
            }
            result["problems"].append(data_)
        if is_full:
            result["raw"] = json.loads(data.json)

    else:
        assert False

    result['contest_id'] = str(vars(contest)['contest_id'])
    for problem_result in result['problems']:
        parsed_problem = onlinejudge.dispatch.problem_from_url(problem_result['url'])
        assert parsed_problem is not None
        problem_result.update(get_problem_ids(parsed_problem))
        problem_result['contest_id'] = result['contest_id']
    return result
