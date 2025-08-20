#!/usr/bin/env python3
"""
Upload script for Tokenometry package to PyPI.
This script helps upload your built package to PyPI.
"""

import os
import sys
import subprocess
from pathlib import Path


def check_dist_exists():
    """Check if the dist directory exists with built packages."""
    dist_path = Path("dist")
    if not dist_path.exists():
        print("❌ Error: 'dist/' directory not found!")
        print("   Please run 'python build_package.py' first to build the package")
        sys.exit(1)
    
    packages = list(dist_path.glob("*.whl")) + list(dist_path.glob("*.tar.gz"))
    if not packages:
        print("❌ Error: No package files found in 'dist/' directory!")
        print("   Please run 'python build_package.py' first to build the package")
        sys.exit(1)
    
    print(f"✅ Found {len(packages)} package(s) in dist/ directory:")
    for pkg in packages:
        print(f"   📦 {pkg.name}")
    return packages


def check_twine_installed():
    """Check if twine is installed."""
    try:
        subprocess.run(["twine", "--version"], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_pypi_credentials():
    """Get PyPI credentials from user."""
    print("\n🔑 PyPI Credentials Required")
    print("=" * 30)
    print("You need to provide your PyPI username and API token.")
    print("If you don't have an API token, create one at: https://pypi.org/manage/account/token/")
    print()
    
    username = input("Enter your PyPI username: ").strip()
    if not username:
        print("❌ Username cannot be empty")
        return None, None
    
    password = input("Enter your PyPI API token: ").strip()
    if not password:
        print("❌ API token cannot be empty")
        return None, None
    
    return username, password


def get_test_pypi_credentials():
    """Get Test PyPI credentials from user."""
    print("\n🧪 Test PyPI Credentials Required")
    print("=" * 35)
    print("⚠️  IMPORTANT: Test PyPI requires a SEPARATE account!")
    print("   Test PyPI is completely separate from production PyPI.")
    print("   You need to create a new account at: https://test.pypi.org/account/register/")
    print()
    
    username = input("Enter your Test PyPI username: ").strip()
    if not username:
        print("❌ Username cannot be empty")
        return None, None
    
    password = input("Enter your Test PyPI password (not API token): ").strip()
    if not password:
        print("❌ Password cannot be empty")
        return None, None
    
    return username, password


def upload_to_test_pypi():
    """Upload to Test PyPI first (recommended)."""
    print("🧪 Uploading to Test PyPI...")
    print("   This is recommended before uploading to production PyPI")
    print("   ⚠️  Note: Test PyPI uses regular username/password, not API tokens!")
    
    # Get Test PyPI credentials (different from production)
    username, password = get_test_pypi_credentials()
    if not username or not password:
        print("❌ Credentials not provided. Upload cancelled.")
        return False
    
    try:
        # Use environment variables for credentials
        env = os.environ.copy()
        env['TWINE_USERNAME'] = username
        env['TWINE_PASSWORD'] = password
        
        print("   Uploading with provided credentials...")
        result = subprocess.run(
            ["twine", "upload", "--repository", "testpypi", "dist/*"],
            env=env, check=True
        )
        print("✅ Successfully uploaded to Test PyPI!")
        print("   You can test the package with: pip install --index-url https://test.pypi.org/simple/ tokenometry")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to upload to Test PyPI: {e}")
        print("\n🔍 Troubleshooting Test PyPI 403 Error:")
        print("   1. Make sure you have a Test PyPI account at https://test.pypi.org/account/register/")
        print("   2. Test PyPI uses username/password, NOT API tokens")
        print("   3. Your Test PyPI account is separate from production PyPI")
        print("   4. Try logging in at https://test.pypi.org/account/login/ first")
        return False


def upload_to_pypi():
    """Upload to production PyPI."""
    print("🚀 Uploading to production PyPI...")
    print("   ⚠️  This will make your package publicly available!")
    
    # Ask for confirmation
    response = input("   Are you sure you want to continue? (yes/no): ").lower().strip()
    if response not in ['yes', 'y']:
        print("   Upload cancelled by user")
        return False
    
    # Get production PyPI credentials (uses API tokens)
    username, password = get_pypi_credentials()
    if not username or not password:
        print("❌ Credentials not provided. Upload cancelled.")
        return False
    
    try:
        # Use environment variables for credentials
        env = os.environ.copy()
        env['TWINE_USERNAME'] = username
        env['TWINE_PASSWORD'] = password
        
        print("   Uploading with provided credentials...")
        result = subprocess.run(
            ["twine", "upload", "dist/*"],
            env=env, check=True
        )
        print("✅ Successfully uploaded to PyPI!")
        print("   Your package is now available at: https://pypi.org/project/tokenometry/")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to upload to PyPI: {e}")
        print("\n🔍 Troubleshooting Production PyPI Error:")
        print("   1. Make sure your API token has 'Entire account (all projects)' scope")
        print("   2. Verify your username and API token are correct")
        print("   3. Check if your account has 2FA enabled (API tokens required)")
        return False


def create_pypirc_file():
    """Create a .pypirc file for storing PyPI credentials."""
    print("\n📝 Creating .pypirc configuration file...")
    print("   This will store your credentials securely for future uploads.")
    print("   ⚠️  Note: Test PyPI and Production PyPI use different credential types!")
    
    print("\n🔑 Production PyPI (uses API tokens):")
    prod_username, prod_password = get_pypi_credentials()
    if not prod_username or not prod_password:
        print("❌ Production PyPI credentials not provided. Configuration cancelled.")
        return False
    
    print("\n🧪 Test PyPI (uses username/password):")
    test_username, test_password = get_test_pypi_credentials()
    if not test_username or not test_password:
        print("❌ Test PyPI credentials not provided. Configuration cancelled.")
        return False
    
    pypirc_content = f"""[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = {prod_username}
password = {prod_password}

[testpypi]
repository = https://test.pypi.org/legacy/
username = {test_username}
password = {test_password}
"""
    
    try:
        with open('.pypirc', 'w') as f:
            f.write(pypirc_content)
        
        # Set secure permissions (readable only by owner)
        os.chmod('.pypirc', 0o600)
        
        print("✅ .pypirc file created successfully!")
        print("   Your credentials are now stored securely.")
        print("   Future uploads will use these credentials automatically.")
        return True
    except Exception as e:
        print(f"❌ Failed to create .pypirc file: {e}")
        return False


def show_troubleshooting_info():
    """Show troubleshooting information for common PyPI issues."""
    print("\n🔍 PyPI Upload Troubleshooting Guide")
    print("=" * 40)
    
    print("\n📚 Test PyPI vs Production PyPI:")
    print("   • Test PyPI: https://test.pypi.org/")
    print("     - Separate account required")
    print("     - Uses username/password (NOT API tokens)")
    print("     - For testing packages before production")
    print("     - Register at: https://test.pypi.org/account/register/")
    
    print("\n   • Production PyPI: https://pypi.org/")
    print("     - Your main PyPI account")
    print("     - Uses username + API token")
    print("     - For final package releases")
    print("     - API tokens at: https://pypi.org/manage/account/token/")
    
    print("\n🚨 Common Issues:")
    print("   1. 403 Forbidden on Test PyPI:")
    print("      → Create a Test PyPI account first")
    print("      → Use username/password, not API tokens")
    
    print("\n   2. 403 Forbidden on Production PyPI:")
    print("      → Check API token scope (needs 'Entire account')")
    print("      → Verify username and token are correct")
    print("      → Ensure 2FA is enabled if required")
    
    print("\n   3. Package name conflicts:")
    print("      → Check if 'tokenometry' is already taken")
    print("      → Consider using a different package name")
    
    print("\n💡 Pro Tips:")
    print("   • Always test on Test PyPI first")
    print("   • Use .pypirc file for automatic authentication")
    print("   • Keep your API tokens secure and never commit them to git")


def main():
    """Main upload process."""
    print("🚀 Tokenometry PyPI Upload Script")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not Path("tokenometry").exists():
        print("❌ Error: Please run this script from the Tokenometry project root directory")
        sys.exit(1)
    
    # Check if twine is installed
    if not check_twine_installed():
        print("❌ Error: twine is not installed!")
        print("   Install it with: pip install twine")
        sys.exit(1)
    
    # Check if packages are built
    packages = check_dist_exists()
    
    # Check if .pypirc exists
    pypirc_exists = Path('.pypirc').exists()
    if pypirc_exists:
        print("✅ Found .pypirc configuration file")
        print("   Your credentials are already configured.")
    else:
        print("ℹ️  No .pypirc file found")
        print("   You can create one to store your credentials securely.")
    
    print("\n📤 Choose an option:")
    print("1. Upload to Test PyPI (recommended for testing)")
    print("2. Upload to Production PyPI (final release)")
    print("3. Both (Test first, then Production)")
    print("4. Create/Update .pypirc configuration file")
    print("5. Show troubleshooting information")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            upload_to_test_pypi()
            break
        elif choice == "2":
            upload_to_pypi()
            break
        elif choice == "3":
            if upload_to_test_pypi():
                print("\n" + "="*40)
                upload_to_pypi()
            break
        elif choice == "4":
            create_pypirc_file()
            break
        elif choice == "5":
            show_troubleshooting_info()
            break
        elif choice == "6":
            print("👋 Upload cancelled. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
    
    print("\n🎉 Process completed!")


if __name__ == "__main__":
    main()
