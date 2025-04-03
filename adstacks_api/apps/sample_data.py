import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adstacks_api.settings')

import django
django.setup()

try:
    from apps.models import App
except ModuleNotFoundError as e:
    print(f"Error importing apps.models: {e}")
    sys.exit(1)

def populate_sample_data():
    sample_apps = [
        {'name': 'TestApp1', 'version': '1.0', 'description': 'Test app 1'},
        {'name': 'TestApp2', 'version': '2.1', 'description': 'Test app 2'},
    ]
    
    for app_data in sample_apps:
        App.objects.create(**app_data)
    print("Sample data added successfully!")

if __name__ == '__main__':
    populate_sample_data()