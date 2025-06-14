from files import write_to_tempfile, cleanup_tempfile
from github import get_current_branch, push_branch_to_github, get_commits_not_in_main_branch, create_pull_request, read_template
from client import Client
import sys

def main():
    main_branch = sys.argv[1] if len(sys.argv) > 1 else "main"
    user_context = input("¿Hay algún contexto adicional que quieras añadir a la descripción del PR? (Pulsa Enter para omitir): ")

    branch = get_current_branch()
    push_branch_to_github(branch)
    commits = get_commits_not_in_main_branch(main_branch)
    template = read_template()
    pr_body = Client().build_pr_body(template, commits, user_context)
    tmp_path = write_to_tempfile(pr_body)	
    create_pull_request(branch, tmp_path, main_branch)
    cleanup_tempfile(tmp_path)
    print("Pull request created!")

if __name__ == "__main__":
    main()
