import requests

def display_user_repos_commits(user_id):
    """
    Retrieve repos and the number of commits for a given GitHub user ID
    """
    try:
        # get all repos using restful API
        response = requests.get(f"https://api.github.com/users/{user_id}/repos")

        if response.status_code == 200:
            repos = response.json()
            # iterate every repos
            for repo in repos:
                repo_name = repo['name']
                # get all commits using restful API
                commits_response = requests.get(f"https://api.github.com/repos/{user_id}/{repo_name}/commits")
                if commits_response.status_code == 200:
                    commits = commits_response.json()

                    commits_count = len(commits)

                    # print result
                    print(f"Repo: {repo_name} Number of commits: {commits_count}")
                else:
                    print(f"Failed to fetch commits for repository {repo_name}")
        else:
            print("Failed to fetch repositories for the user")

    except Exception as e:
        print("An error occurred:", e)


if __name__ == '__main__':
    # Example usage
    user_id = "HarveyQin"
    display_user_repos_commits(user_id)