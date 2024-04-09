from flask import Flask
import json
import requests


app = Flask(__name__)

@app.route('/<repo_owner>/<repo_name>')

def get_latest_release_tag_version(repo_owner, repo_name):
    latest_release=""
    try:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases"
        headers = {"Accept": "application/vnd.github+json","X-GitHub-Api-Version": "2022-11-28"}
        r=requests.get(url, headers=headers)
        latest_release = json.loads(r.text)[0]["tag_name"]

    except Exception as e:
        # By this way we can know about the type of error occurring
            print("failed to get release tag version: ",e)

    if not latest_release:
         latest_release="failed to fetch github release tag version"

    return f"{latest_release}"

if __name__ == '__main__':
    app.run(debug=False, port=8080, host="0.0.0.0")