import platform
import sys
import subprocess

def setup_ios():
    print("iOS cihazı için setup işlemleri yapılıyor...")
    try:
        # İOS için gerekli paketleri yüklemek
        subprocess.check_call(["apk", "add", "update", "upgrade", "python2", "python3"])
    except subprocess.CalledProcessError as e:
        print(f"Paket yükleme hatası: {e}")
    except FileNotFoundError:
        print("apk komutu bulunamadı, lütfen apk'nın kurulu olduğundan emin olun.")

def setup_android():
    print("Android cihazı için setup işlemleri yapılıyor...")
    try:
        # Android için gerekli paketleri yüklemek
        subprocess.check_call(["pkg", "install", "update", "upgrade", "python2", "python3"])
    except subprocess.CalledProcessError as e:
        print(f"Paket yükleme hatası: {e}")
    except FileNotFoundError:
        print("pkg komutu bulunamadı, lütfen Termux'un kurulu olduğundan emin olun.")

def main():
    system = platform.system()
    if system == "Darwin":
        # macOS veya iOS olabilir, daha fazla kontrol gerekebilir
        if sys.platform == "darwin":
            setup_ios()
        else:
            print("Bilinmeyen iOS platformu")
    elif system == "Linux":
        setup_android()
    else:
        print(f"Desteklenmeyen platform: {system}")

if __name__ == "__main__":
    main()