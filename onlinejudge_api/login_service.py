from typing import *

from onlinejudge.type import *

schema_example = {
    "loggedIn": True,
    "userName": "chokudai",
    "profileUrl": "https://atcoder.jp/users/chokudai",
}  # type: Dict[str, Any]

schema = {
    "type": "object",
    "properties": {
        "loggedIn": {
            "type": "boolean",
        },
        "userName": {
            "type": "string",
        },
        "profileUrl": {
            "type": ["string", "null"],
            "format": "uri",
        },
    },
    "required": ["loggedIn"],
}  # type: Dict[str, Any]


def main(service: Service, *, username: Optional[str], password: Optional[str], check_only: bool, session: requests.Session) -> Dict[str, Any]:
    """
    :raises Exception:
    :raises LoginError:
    """

    result = {}  # type: Dict[str, Any]
    if check_only:
        # We cannot check `assert username is None` because some environments defines $USERNAME and it is set here. See https://github.com/online-judge-tools/api-client/issues/53
        assert password is None
    else:
        assert username is not None
        assert password is not None

        def get_credentials() -> Tuple[str, str]:
            assert username is not None  # for mypy
            assert password is not None  # for mypy
            return (username, password)

        service.login(get_credentials=get_credentials, session=session)
    user = service.is_logged_in(session=session)
    if not check_only and user is None:
        raise LoginError
    result["loggedIn"] = user is not None
    if user is not None:
        result["userName"] = user.username
        result["profileUrl"] = user.profile_url
    return result
