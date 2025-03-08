import subprocess
import sys

def install_packages():
    with open('requests.txt', 'r') as file:
        packages = file.readlines()

    for package in packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package.strip()])

def save_installed_packages():
    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    with open('requests.txt', 'w') as file:
        file.write(installed_packages.decode())

def show_license():
    with open('requests.txt', 'r') as file:
        print(file.read())

if __name__ == "__main__":
    install_packages()
    save_installed_packages()
    show_license()