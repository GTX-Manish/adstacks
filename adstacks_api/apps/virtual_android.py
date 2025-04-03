import subprocess
import os
import time

def check_emulator():
    """Check if an emulator is running."""
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    if 'emulator' not in result.stdout:
        print("No emulator detected. Start it with: emulator -avd TestEmulator")
        return False
    return True

def install_apk(apk_path):
    """Install an APK on the emulator."""
    if not os.path.exists(apk_path):
        print(f"APK not found at {apk_path}. Provide a valid APK file.")
        return False
    try:
        subprocess.run(['adb', 'install', apk_path], check=True)
        print(f"Successfully installed {apk_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install APK: {e}")
        return False

def get_system_info():
    """Retrieve and log system information from the emulator."""
    commands = {
        'OS Version': ['adb', 'shell', 'getprop', 'ro.build.version.release'],
        'Device Model': ['adb', 'shell', 'getprop', 'ro.product.model'],
        'Available Memory': ['adb', 'shell', 'cat', '/proc/meminfo']
    }
    
    system_info = {}
    for key, cmd in commands.items():
        result = subprocess.run(cmd, capture_output=True, text=True)
        if key == 'Available Memory':
            for line in result.stdout.splitlines():
                if 'MemAvailable' in line:
                    system_info[key] = line.strip()
                    break
        else:
            system_info[key] = result.stdout.strip()
    
    with open('system_info.log', 'w') as f:
        for key, value in system_info.items():
            f.write(f"{key}: {value}\n")
    
    print("System Info Logged:")
    for key, value in system_info.items():
        print(f"{key}: {value}")
    return system_info

if __name__ == "__main__":
    if not check_emulator():
        exit(1)
    
    print("Waiting for emulator to boot...")
    time.sleep(30)
    
    apk_path = "/Users/manishkumar/Downloads/sample_app.apk"
    install_apk(apk_path)
    
    get_system_info()