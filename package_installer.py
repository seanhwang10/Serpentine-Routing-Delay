import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = ["numpy", "matplotlib"]

for pkg in required_packages:
    try:
        __import__(pkg)
    except ImportError:
        print(f"Package {pkg} not found. Installing...")
        install(pkg)

print("All required packages are installed. You can now run your code.")
