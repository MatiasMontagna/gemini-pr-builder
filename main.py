from files import write_to_tempfile, cleanup_tempfile
from github import get_current_branch, push_branch_to_github, get_commits_not_in_master, create_pull_request, read_template
from client import Client

def main():
    branch = get_current_branch()
    push_branch_to_github(branch)
    commits = get_commits_not_in_master()
    template = read_template()
    pr_body = Client().build_pr_body(template, commits)
    tmp_path = write_to_tempfile(pr_body)	
    create_pull_request(branch, tmp_path)
    cleanup_tempfile(tmp_path)
    print("Pull request created!")

if __name__ == "__main__":
    main()
