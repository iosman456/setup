import os
import subprocess
import sys

def install_package(package_name):
    try:
        result = subprocess.run(["apk", "add", package_name], check=True, capture_output=True, text=True)
        print(f"{package_name} başarıyla yüklendi!\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        if "is already installed" in e.stderr:
            print(f"{package_name} zaten yüklü.")
        else:
            print(f"{package_name} yüklenirken hata oluştu:\n{e.stderr}")

def main():
    if os.geteuid() != 0:
        print("Bu scripti çalıştırmak için root yetkisine sahip olmalısınız.")
        sys.exit(1)

    print("İOS'da Gereken Paketler Yükleniyor...")
    packages = ["update", "upgrade", "python2", "python3", "py-pip", "py3-pip"]
    for package in packages:
        install_package(package)
    print("Gereken Paketler Yüklendi!")

if __name__ == "__main__":
    main()