
from prefect.blocks.system import Secret
import os

def create_github_token_secret():
    """Create a Secret block for GitHub token"""
    
    # Create the Secret block
    secret_block = Secret(value=os.getenv('GITHUB_TOKEN'))
    
    # Save the block with a name
    secret_block.save(name="github-token")
    
    print("✅ Secret block 'github-token' created successfully!")

if __name__ == "__main__":
    create_github_token_secret()
