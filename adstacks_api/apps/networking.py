import requests
import subprocess
import json

def get_mock_data():
    """Retrieve mock data from the emulator."""
    try:
        device_id = subprocess.run(['adb', 'shell', 'getprop', 'ro.serialno'], 
                                 capture_output=True, text=True, check=True).stdout.strip()
        os_version = subprocess.run(['adb', 'shell', 'getprop', 'ro.build.version.release'], 
                                   capture_output=True, text=True, check=True).stdout.strip()
        memory = subprocess.run(['adb', 'shell', 'cat', '/proc/meminfo'], 
                               capture_output=True, text=True, check=True).stdout
        for line in memory.splitlines():
            if 'MemAvailable' in line:
                available_memory = line.strip()
                break
        else:
            available_memory = "Unknown"
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving emulator data: {e}")
        return None
    
    return {
        'device_id': device_id,
        'os_version': os_version,
        'available_memory': available_memory
    }

def send_to_backend():
    """Send mock data to the Django API and log the response."""
    url = 'http://localhost:8000/api/add-app/'
    mock_data = get_mock_data()
    
    if not mock_data:
        print("Failed to get mock data. Aborting.")
        return
    
    payload = {
        'name': f"Emulator_{mock_data['device_id']}",
        'version': mock_data['os_version'],
        'description': f"Virtual Android device with {mock_data['available_memory']}"
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        with open('server_response.log', 'w') as f:
            f.write(f"Status: {response.status_code}\n")
            f.write(f"Response: {json.dumps(response.json(), indent=2)}\n")
        
        print(f"Server Response: {response.status_code} - {response.json()}")
    except requests.RequestException as e:
        error_msg = f"Failed to connect to server: {e}"
        print(error_msg)
        with open('server_response.log', 'w') as f:
            f.write(error_msg + "\n")

if __name__ == "__main__":
    print("Ensure emulator is running and Django server is at http://localhost:8000/")
    send_to_backend()