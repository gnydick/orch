#!/usr/bin/env python3

from github import Github
import re

token = "22024c38409908bb5e80e93616cd7de87c115075"


def gather_clone_urls(organization, no_forks=True):
    gh = Github(login_or_token=token)
    org = gh.get_organization(login=organization)

    repos = org.get_repos()

    for repo in repos:

        # Don't print the urls for repos that are forks.
        if no_forks and repo.fork:
            continue

        yield repo

def lower(string):
    return string.group(1) + '-' + str.lower(string.group(2))

if __name__ == '__main__':
    remove_foo_pattern = re.compile(r'^foo-')
    replace_caps_pattern = re.compile(r'([a-z])([A-Z])([a-z])')
    repos = gather_clone_urls("Foo")
    for repo in repos:
        clean_repo = remove_foo_pattern.sub(r'', repo.name)

        clean_clean_repo = re.sub(r'([a-z])([A-Z])([a-z])', lower, clean_repo)
        print("%s\t%s" % (clean_clean_repo, repo.clone_url))
