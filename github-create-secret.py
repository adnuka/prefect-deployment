
from prefect.blocks.system import Secret
from prefect_github import GitHubCredentials
import os

def create_github_token_secret():
    """Create a Secret block for GitHub token"""
    
    # Create the Secret block
    secret_block = Secret(value=os.getenv('GITHUB_TOKEN'))
    
    # Save the block with a name
    secret_block.save(name="github-token")
    # Load the GitHub token from secret block
    secret_block = Secret.load("github-token")
    github_token = secret_block.get()
    
    # Create and save GitHub credentials with the token
    github_credentials = GitHubCredentials(token=github_token)
    github_credentials.save("github-credentials", overwrite=True)
    print("✅ GitHub credentials block saved")
    
    
    print("✅ Secret block 'github-token' created successfully!")

if __name__ == "__main__":
    create_github_token_secret()
