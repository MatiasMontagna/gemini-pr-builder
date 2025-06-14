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

def get_commits_not_in_master():
    return run("git log master..HEAD --pretty=format:'%h %s'")

def create_pull_request(branch, tmp_path):
    pr_title = f"PR from {branch}"
    run(f'gh pr create --base master --head {branch} --title "{pr_title}" --body-file "{tmp_path}"') 
    
def read_template():
    return read_file(".github/pull_request_template.md")