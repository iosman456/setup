import os
import subprocess
import sys

def is_root():
    return os.geteuid() == 0

def check_package_installed(package_name):
    try:
        result = subprocess.run(["apk", "info", package_name], check=True, capture_output=True, text=True)
        if package_name in result.stdout:
            return True
        return False
    except subprocess.CalledProcessError:
        return False

def install_package(package_name):
    if check_package_installed(package_name):
        print(f"{package_name} zaten yüklü.")
        return
    try:
        result = subprocess.run(["apk", "add", package_name], check=True, capture_output=True, text=True)
        print(f"{package_name} başarıyla yüklendi!\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"{package_name} yüklenirken hata oluştu:\n{e.stderr}")

def main():
    if not is_root():
        print("Bu scripti çalıştırmak için root yetkisine sahip olmalısınız.")
        sys.exit(1)

    print("İOS'da Gereken Paketler Yükleniyor...")
    packages = ["update", "upgrade", "python2", "python3", "py-pip", "py3-pip"]
    for package in packages:
        install_package(package)
    print("Gereken Paketler Yüklendi!")

if __name__ == "__main__":
    main()