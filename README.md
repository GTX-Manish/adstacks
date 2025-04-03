# Python Intern Assignment - Adstacks Media

This project implements a Django-based API, database integration, Android emulator simulation, and networking functionality as per the Adstacks Media Python Intern Assignment requirements. Below are the setup instructions and deliverables for each task.


## General Setup
1. **Clone the Repository**:
   - Ensure you have this project directory (`adstacks_api/`).

2. **Create and Activate Virtual Environment**:
   ```bash
   python3 -m venv venv
   # On MacOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate```
3. **Install Dependencies
  `pip install django djangorestframework requests`

4. **Apply Migrations
  `python manage.py makemigrations
   python manage.py migrate`

**Task 1: Backend Development
   ## 1. Start the server
      `python manage.py runserver`
   ## 2. Testing
      
      2.1 POST /add-app/:
         `curl -X POST http://localhost:8000/api/add-app/ -H "Content-Type: application/json" -d '{"name": "TestApp", "version": "1.0", "description": "Test app"}`

      2.2 GET /get-app/{id}/ (replace {id} with the returned ID):
         `curl http://localhost:8000/api/get-app/1/`

      2.3 DELETE /delete-app/{id}/:
         `curl -X DELETE http://localhost:8000/api/delete-app/1/`

# Task 2: Database Management
   ## 1. Setup
      1.1 Ensure migrations are applied (see General Setup).
      1.2 Populate sample data:
      
         python apps/sample_data.py`
         python manage.py shell`
         
         from apps.models import App
         App.objects.create(name="TestApp1", version="1.0", description="Test app 1")
         App.objects.create(name="TestApp2", version="2.1", description="Test app 2")
         exit()
   ## 2. Verification
      ```bash
      python manage.py shell
      
      from apps.models import App
      print(App.objects.all())

# Task 3: Virtual Android System Simulation
   ## Setup
         1. Install Android SDK:
            Download command-line tools from developer.android.com.
            Extract to ~/android-sdk.
            
         2. Set environment variables:
               export ANDROID_HOME=~/android-sdk
               export PATH=$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$ANDROID_HOME/cmdline-tools/latest/bin:$PATH
               source ~/.zshrc 

               !!! For MacOS
               sdkmanager "platform-tools" "emulator" "system-images;android-30;google_apis;arm64-v8a"

         3. Create AVD
            avdmanager create avd -n TestEmulator -k "system-images;android-30;google_apis;arm64-v8a" --device "pixel_4"
      
         4. Start Emulator
            emulator -avd TestEmulator -no-snapshot &
      
         5. Place Sample APK
            Copy a compatible APK (e.g., sample.apk) to the project root (adstacks_api/).
      
         6. Run
            python apps/virtual_android.py

# Task 4: Basic Networking
   ## Setup
      1. Start the Django server
         python manage.py runserver
      2. Ensure the emulator is running
         emulator -avd TestEmulator &
      3. Run
         python apps/networking.py
