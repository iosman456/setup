import platform
import sys
import subprocess

def run_command(command):
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(f"Komut çalıştırma hatası: {e}")
    except FileNotFoundError:
        print(f"{command[0]} komutu bulunamadı, lütfen {command[0]}'nın kurulu olduğundan emin olun.")

def update_and_upgrade(package_manager):
    print(f"{package_manager} ile sistem güncelleniyor ve yükseltiliyor...")
    run_command([package_manager, "update"])
    run_command([package_manager, "upgrade"])

def install_packages(package_manager, packages):
    print(f"{package_manager} ile paketler yükleniyor: {', '.join(packages)}")
    run_command([package_manager, "install"] + packages)

def setup_ios():
    print("iOS cihazı için setup işlemleri yapılıyor...")
    package_manager = "apk"
    update_and_upgrade(package_manager)
    install_packages(package_manager, ["python2", "python3"])

def setup_android():
    print("Android cihazı için setup işlemleri yapılıyor...")
    package_manager = "pkg"
    update_and_upgrade(package_manager)
    install_packages(package_manager, ["python2", "python3"])

def main():
    system = platform.system()
    if system == "Darwin":
        # iOS olabilir, macOS olabilir. Daha fazla kontrol gerekebilir.
        if sys.platform.startswith('darwin'):
            setup_ios()
        else:
            print("Bilinmeyen iOS platformu")
    elif system == "Linux":
        # Android olabilir.
        if 'ANDROID_ARGUMENT' in sys.argv or 'com.termux' in sys.prefix:
            setup_android()
        else:
            print("Bilinen bir Android platformu değil")
    else:
        print(f"Desteklenmeyen platform: {system}")

if __name__ == "__main__":
    main()