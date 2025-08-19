import subprocess
import sys
from files import read_file

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running: {cmd}\n{result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def get_current_branch():
    return run("git rev-parse --abbrev-ref HEAD")

def push_branch_to_github(branch):
    run(f"git push -u origin {branch}")

def get_commits_not_in_main_branch(main_branch="main"):
    return run(f"git log {main_branch}..HEAD --pretty=format:'%h %s' --reverse")

def create_pull_request(branch, tmp_path, main_branch="main"):
    pr_title = f"PR from {branch}"
    pr_url = run(f'gh pr create --base {main_branch} --head {branch} --title "{pr_title}" --body-file "{tmp_path}"')
    return pr_url 

def read_template():
    return read_file(".github/pull_request_template.md")