import requests
import json


def list_repo(since,token):
    res = requests.get(
        f"https://api.github.com/repositories?since={since}",
        headers={'Authorization': f'token {token}'}
    )
    content = res.content.decode("utf-8")
    repo_list = json.loads(content)
    return repo_list

def extract_fields(repo_content):
    try:
        repo_dict = {
            'id': repo_content['id'],
            'node_id': repo_content["node_id"],
            'name': repo_content["name"],
            "full_name": repo_content["full_name"],
            "owner": {
                'login': repo_content['owner']['login'],
                'id': repo_content['owner']["id"],
                'node_id': repo_content['owner']['node_id'],
                'type': repo_content['owner']["type"],
                'site_admin': repo_content['owner']['site_admin']
            },
            'html_url': repo_content['html_url'],
            'description': repo_content['description'],
            'fork': repo_content['fork'],
            'created_at': repo_content['created_at']}

        return repo_dict

    except:
        pass


def get_repo_details(owner, name, token):
    res = requests.get(
        f"https://api.github.com/repos/{owner}/{name}",
        headers={'Authorization': f'token {token}'}
    )

    repo_details = json.loads(res.content)
    return  repo_details

