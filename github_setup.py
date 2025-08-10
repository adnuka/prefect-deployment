#!/usr/bin/env python3
"""
Improved script to create GitHub block connection for Prefect
"""
import os
import time
from prefect.blocks.system import Secret

def main():
    print("🚀 Setting up GitHub block...")
    
    # Wait a bit for Prefect server to be fully ready
    print("⏳ Waiting for Prefect server to be ready...")
    time.sleep(30)
    
    # Get GitHub token from environment variable
    github_token = os.getenv('GITHUB_TOKEN')
    
    if not github_token:
        print("❌ ERROR: GITHUB_TOKEN not found!")
        return False
    
    try:
        # First, register the GitHub blocks
        print("📦 Registering GitHub block types...")
        import subprocess
        result = subprocess.run(["prefect", "block", "register", "-m", "prefect_github"], 
                            capture_output=True, text=True)
        print(f"Register result: {result.stdout}")
        if result.stderr:
            print(f"Register stderr: {result.stderr}")
        
        # Import after registration
        from prefect_github import GitHubRepository
        
        # Create secret block for the token
        print("🔑 Creating token secret...")
        token_secret = Secret(value=github_token)
        token_secret.save("github-token", overwrite=True)
        print("✅ Token secret 'github-token' created")
        
        # Your repository URL
        repo_url = "https://github.com/adnuka/market-prices-app"
        
        # Create GitHub repository block
        print("📁 Creating GitHub repository block...")
        github_block = GitHubRepository(
            repository_url=repo_url,
            reference="main"
        )
        
        github_block.save("my-github-repo", overwrite=True)
        print("✅ GitHub block 'my-github-repo' created!")
        
        # Verify the block was created
        print("🔍 Verifying block creation...")
        test_block = GitHubRepository.load("my-github-repo")
        print(f"✅ Verification successful: {test_block.repository_url}")
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("🎉 GitHub block setup completed successfully!")
    else:
        print("💥 GitHub block setup failed!")