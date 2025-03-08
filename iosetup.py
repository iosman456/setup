import os
import subprocess

def install_package(package_name):
    try:
        result = subprocess.run(["apk", "add", package_name], check=True, capture_output=True, text=True)
        print(f"{package_name} başarıyla yüklendi!\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"{package_name} yüklenirken hata oluştu:\n{e.stderr}")

def main():
    print("İOS'da Gereken Paketler Yükleniyor...")
    packages = ["update", "upgrade", "python2", "python3", "py-pip", "py3-pip"]
    for package in packages:
        install_package(package)
    print("Gereken Paketler Yüklendi!")

if __name__ == "__main__":
    main()