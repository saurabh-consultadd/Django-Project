# Blog Application

# Overview

The **Blog Application** is a Django-based web application which uses the concept of Model, View and Serializer. It has user authentication as well that allow restricted permissions for certain operation.

<br/>

# Table of Contents
1. [Features](#features)
2. [Project Setup](#setup)
3. [Project Structure](#structure)
4. [API Endpoints](#endpoints)
5. [Testing](#testing)

<br/>

# Features <a name = "features"></a>
#### 1. Two models namely Posts and Comments which have some fields.
#### 2. It uses in built user authentication that allows special permission to admin.
#### 3. Author of the post can update and delete it. They also have permission to turn off comment.
#### 4. Any authenticated user can do a comment on other's post.
#### 5. Any user can reply to other's comment.
#### 6. Admin has power to update and delete any post or comment.
#### 7. We can see all posts and comments but cannot perform any operations.
#### 8. A special feature that post with same content cannot be posted again.
#### There are many more to explore...

<br/>

# Project Setup <a name = "setup"></a>

## Prerequisites

- Python 
- Django 
- Django REST Framework 
- PostgreSQL
- pytest 

## Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<yourusername>/Django-Project.git
   cd inventory-management-system
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     . env/bin/activate
     ```

4. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure the Database:**
   Ensure that PostgreSQL is running and create a database named `blogdb`.

   Update the `DATABASES` setting in `inventory_management/settings.py`:
   ```python
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogdb',                      
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }

6. **Apply Migrations:**
   ```bash
    python manage.py migrate
   ```

7. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

<br/>

# Project Structure <a name = "structure"></a>

- `BlogApplication/`: Project settings and configuration.
  - `settings.py`: Configuration settings.
  - `urls.py`: Project-wide URL routing.
- `blog/`: Contains the Django app for Blog Application.
  - `models.py`: Defines the `Posts` and `Comments` models.
  - `views.py`: Contains API views for posts and comments.
  - `serializers.py`: Serializers for the models.
  - `urls.py`: URL routing for the app.

<br/>

# API Endpoints <a name = "endpoints"></a>

## Create User
- Method: POST
- Endpoint: user/
- Screenshot:
<img width="1018" alt="Screenshot 2024-07-23 at 12 44 39 PM" src="https://github.com/user-attachments/assets/1493e4d1-39da-4e27-8fe6-d4fbbbd85828">

## Posts Endpoints
### 1. Add Post
 - Method: POST
- Endpoint: posts/
- Screenshot:
<img width="1022" alt="Screenshot 2024-07-23 at 12 45 38 PM" src="https://github.com/user-attachments/assets/793b9f20-86ba-442e-b348-dc25daa319b7">

### 2. Get Post
 - Method: POST
- Endpoint: posts/
- Screenshot:
<img width="1013" alt="Screenshot 2024-07-23 at 12 45 27 PM" src="https://github.com/user-attachments/assets/c379c191-ac6b-453d-911f-ae38a90b9446">


### 3. Update Post
 - Method: POST
- Endpoint: posts/
- Screenshot:
<img width="1015" alt="Screenshot 2024-07-23 at 12 45 56 PM" src="https://github.com/user-attachments/assets/9008946e-a17f-493e-8d94-a6d49dee82aa">

### 4. Delete Post
 - Method: POST
- Endpoint: posts/
- Screenshot:
<img width="1014" alt="Screenshot 2024-07-24 at 12 26 39 PM" src="https://github.com/user-attachments/assets/ab66fdb9-0248-42f0-8903-8ea7be5db343">

## Comments Endpoints
### 1. Add Comment
 - Method: POST
- Endpoint: comments/
- Screenshot:
<img width="1018" alt="Screenshot 2024-07-24 at 12 56 19 PM" src="https://github.com/user-attachments/assets/26afd889-6e11-49e3-9ade-d7f8a922b144">

### 2. Get comment
 - Method: POST
- Endpoint: comments/
- Screenshot:
<img width="1019" alt="Screenshot 2024-07-24 at 12 55 50 PM" src="https://github.com/user-attachments/assets/e0bc9a0e-c777-44e0-a555-dfd7a903c7d8">

### 3. Update comment
 - Method: POST
- Endpoint: comments/
- Screenshot:
<img width="1023" alt="Screenshot 2024-07-23 at 12 47 57 PM" src="https://github.com/user-attachments/assets/f237c74b-1107-4589-a489-ac640c331f7a">

### 4. Delete comment
 - Method: POST
- Endpoint: comments/
- Screenshot:
<img width="1017" alt="Screenshot 2024-07-24 at 12 56 11 PM" src="https://github.com/user-attachments/assets/70b2c649-005f-4d1f-ad74-3e9dfff89cea">


# Testing <a name = "testing"></a>

To run tests and check coverage:

1. **Install Testing Dependencies:**
   ```bash
   pip install pytest pytest-django
   ```

2. **Configure the settings.py:**
   Add the code in `BlogApplication/settings.py`:
   ```python
   TEST_RUNNER = 'pytest_runner.DjangoTestSuiteRunner'
   ```

3. **Run Tests:**
   ```bash
   pytest
   ```

4. **Check Test Coverage:**
   ```bash
   coverage run -m pytest
   ```

5. **Get Coverage Report:**
   ```bash
   coverage report
   ```

## Test Result:
<img width="1118" alt="Screenshot 2024-07-25 at 11 51 39 AM" src="https://github.com/user-attachments/assets/f3656cd0-d614-4de8-a19a-67cb90a94739">

