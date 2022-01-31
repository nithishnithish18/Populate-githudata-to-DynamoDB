from util import list_repo
from util import extract_fields
from util import get_repo_details

if __name__ == '__main__':
    since = '453896572'
    token = "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"
    repos_list = list_repo(since, token)
    final_list = []
    for repo in repos_list:
        owner = repo["owner"]["login"]
        name = repo["name"]
        repo_details = get_repo_details(owner, name, token)
        repo_fields = extract_fields(repo_details)
        final_list.append(repo_fields)

    print(len(final_list))
    print(final_list)

