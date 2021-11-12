def readFromGit(gitpath):
    r = requests.get(
        "https://api.github.com/repos/{owner}/{repo}/contents/{path}".format(
            owner=owner, repo=repo, path=gitpath
        ),
        headers={
            "accept": "application/vnd.github.v3.raw",
            "authorization": "token {}".format(token),
        },
    )
    return r
