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
   venv\Scripts\activate
3. **Install Dependencies
  `pip install django djangorestframework requests`

4. **Apply Migrations
  `python manage.py makemigrations
   python manage.py migrate`

#Task 1: Backend Development
   1. Start the server
      `python manage.py runserver`
   2. Testing
      
      POST /add-app/:
      `curl -X POST http://localhost:8000/api/add-app/ -H "Content-Type: application/json" -d '{"name": "TestApp", "version": "1.0", "description": "Test app"}`

      GET /get-app/{id}/ (replace {id} with the returned ID):
      `curl http://localhost:8000/api/get-app/1/`

      DELETE /delete-app/{id}/:
      `curl -X DELETE http://localhost:8000/api/delete-app/1/`

#Task 2: Database Management
   1. Setup
      1. Ensure migrations are applied (see General Setup).
      2. Populate sample data:
         `python apps/sample_data.py`
         `python manage.py shell`
         `from apps.models import App
          App.objects.create(name="TestApp1", version="1.0", description="Test app 1")
          App.objects.create(name="TestApp2", version="2.1", description="Test app 2")
          exit()`
