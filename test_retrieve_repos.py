import unittest
from unittest.mock import patch, Mock, call
from retrieve_repos import display_user_repos_commits


class TestGitHubAPI(unittest.TestCase):

    @patch('requests.get')
    def test_display_user_repos_commits_success(self, mock_get):
        # Mock response for user repos
        mock_user_repos_response = Mock()
        mock_user_repos_response.status_code = 200
        mock_user_repos_response.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]
        mock_get.side_effect = [mock_user_repos_response]

        # Mock response for commits in repo1
        mock_repo1_commits_response = Mock()
        mock_repo1_commits_response.status_code = 200
        mock_repo1_commits_response.json.return_value = [{"commit": {"message": "commit message"}}]

        # Mock response for commits in repo2
        mock_repo2_commits_response = Mock()
        mock_repo2_commits_response.status_code = 200
        mock_repo2_commits_response.json.return_value = [{"commit": {"message": "commit message"}},
                                                         {"commit": {"message": "commit message"}}]
        mock_get.side_effect = [mock_user_repos_response, mock_repo1_commits_response, mock_repo2_commits_response]

        # Expected output
        expected_output = [
            "Repo: repo1 Number of commits: 1",
            "Repo: repo2 Number of commits: 2"
        ]

        # Call the function and capture the output
        with patch('builtins.print') as mock_print:
            display_user_repos_commits("test_user")

        # Verify the output
        mock_print.assert_has_calls([call(msg) for msg in expected_output])

    @patch('requests.get')
    def test_display_user_repos_commits_failed_user_repos(self, mock_get):
        # Mock response for failed user repositories request
        mock_user_repos_response = Mock()
        mock_user_repos_response.status_code = 404
        mock_get.return_value = mock_user_repos_response

        # Expected output
        expected_output = "Failed to fetch repositories for the user"

        # Call the function and capture the output
        with patch('builtins.print') as mock_print:
            display_user_repos_commits("test_user")

        # Verify the output
        mock_print.assert_called_once_with(expected_output)


if __name__ == '__main__':
    unittest.main()
