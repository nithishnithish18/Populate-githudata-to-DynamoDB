from util import list_repo
from util import extract_fields
from util import get_repo_details
from util import load_repos
from  util import delete_repos
import boto3
import os

if __name__ == '__main__':
    since = '453896572'
    token = "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"
    repos_list = list_repo(since, token)
    final_list = []
    for repos in repos_list:
        try:
            owner = repos["owner"]["login"]
            name = repos["name"]
            repo_details = get_repo_details(owner, name, token)
            repo_fields = extract_fields(repo_details)
            final_list.append(repo_fields)

        except:
            pass

    os.environ.setdefault("AWS_PROFILE", "itvgithub")
    os.environ.setdefault("AWS_DEFAULT_REGION","us-east-1")
    dynamodb = boto3.resource("dynamodb")
    ghrepos_table = dynamodb.Table("ghrepos")
    batch_writer = ghrepos_table.batch_writer()
    load_repos(final_list,ghrepos_table,batch_size=50)
    delete_repo = delete_repos(final_list,ghrepos_table,batch_size=50)
    item_list = ghrepos_table.scan()
    print(len(item_list['Items']))
