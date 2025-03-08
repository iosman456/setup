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

    print("Hoş geldiniz! Bu script, İOS'da gereken paketleri yükleyecek.\n")

    default_packages = [
        "update", "upgrade", "python2", "python3", "py-pip", "py3-pip", 
        "git", "curl", "wget", "vim", "nano", "htop", "tmux", "openssl", 
        "nodejs", "npm", "zip", "unzip", "jq", "bash", "make", 
        "gcc", "g++", "nodejs-npm", "python3-dev", "libffi-dev", "musl-dev",
        "docker", "docker-compose", "postgresql", "redis", "mongodb",
        "sqlite", "nginx", "apache2", "php", "php-fpm", "ruby", "perl",
        "java", "openjdk8", "openjdk11", "maven", "gradle", "pipenv",
        "virtualenv", "ruby-dev", "perl-dev", "go", "rust"
    ]

    user_input = input("Varsayılan paketleri yüklemek ister misiniz? (E/h): ").strip().lower()
    if user_input == 'e':
        packages = default_packages
    else:
        packages = input("Yüklemek istediğiniz paketleri virgülle ayırarak girin: ").strip().split(',')

    print("\nGereken paketler yükleniyor...")
    for package in packages:
        package = package.strip()
        install_package(package)
    print("Gereken paketler yüklendi!")

if __name__ == "__main__":
    main()