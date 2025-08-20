#!/usr/bin/env python3
"""
Build script for Tokenometry package.
This script helps build, test, and prepare the package for PyPI.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        sys.exit(1)


def clean_build():
    """Clean previous build artifacts."""
    print("🧹 Cleaning previous build artifacts...")
    dirs_to_clean = ["build", "dist", "*.egg-info"]
    for dir_pattern in dirs_to_clean:
        for path in Path(".").glob(dir_pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"   Removed: {path}")
            else:
                path.unlink()
                print(f"   Removed: {path}")
    print("✅ Cleanup completed")


def install_dev_dependencies():
    """Install development dependencies."""
    print("📦 Installing development dependencies...")
    run_command("pip install -e .[dev]", "Installing package in development mode")


def run_tests():
    """Run the test suite."""
    print("🧪 Running tests...")
    run_command("python -m pytest tests/ -v", "Running test suite")


def build_package():
    """Build the package distribution."""
    print("🔨 Building package distribution...")
    run_command("python -m build", "Building package")


def check_package():
    """Check the built package for issues."""
    print("🔍 Checking package for issues...")
    run_command("twine check dist/*", "Checking package")


def main():
    """Main build process."""
    print("🚀 Starting Tokenometry package build process...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("tokenometry").exists() or not Path("setup.py").exists():
        print("❌ Error: Please run this script from the Tokenometry project root directory")
        sys.exit(1)
    
    try:
        # Clean previous builds
        clean_build()
        
        # Install dev dependencies
        install_dev_dependencies()
        
        # Run tests
        run_tests()
        
        # Build package
        build_package()
        
        # Check package
        check_package()
        
        print("=" * 50)
        print("🎉 Package build completed successfully!")
        print("\n📦 Your package is ready in the 'dist/' directory")
        print("📤 To upload to PyPI, run: twine upload dist/*")
        print("🧪 To test locally, run: pip install dist/*.whl")
        
    except KeyboardInterrupt:
        print("\n⚠️ Build process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
