from prefect import flow
from main import main
from prefect_github import GitHubCredentials
github_credentials_block = GitHubCredentials.load("test-github-block")

@flow(log_prints=True, persist_result=True)
def market_data_flow():
    main()

if __name__ == "__main__":
    market_data_flow.serve(name="market-data-deployment", tags=["market-data"], interval=1800) # 30 minutes in seconds
