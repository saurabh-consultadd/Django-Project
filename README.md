# Blog Application

# Overview

The **Blog Application** is a Django-based web application which have models i.e., Posts and Comments. It has user authentication which allow only the author of the Post to Update and Delete the posts, but everyone has access to see the posts. Now similar for comments, only authenticated user can do a comment on any post and they have access to Update and Delete it. The application uses Django REST Framework to provide a set of RESTful API endpoints for interacting with the database.



# Project Setup

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

# API Endpoints

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
<img width="1019" alt="Screenshot 2024-07-23 at 12 46 20 PM" src="https://github.com/user-attachments/assets/c462f054-a1b4-4bb3-ba6a-4529dc73ae53">

## Comments Endpoints
### 1. Add Comment
 - Method: POST
- Endpoint: comments/
- Screenshot:
<img width="1010" alt="Screenshot 2024-07-23 at 12 47 08 PM" src="https://github.com/user-attachments/assets/d2fde1c6-ad16-408b-b9e6-76f878269b32">

### 2. Get comment
 - Method: POST
- Endpoint: comments/
- Screenshot:
<img width="1012" alt="Screenshot 2024-07-23 at 12 47 21 PM" src="https://github.com/user-attachments/assets/dea72363-f275-4012-8851-038a00ea99f2">

### 3. Update comment
 - Method: POST
- Endpoint: comments/
- Screenshot:
<img width="1023" alt="Screenshot 2024-07-23 at 12 47 57 PM" src="https://github.com/user-attachments/assets/f237c74b-1107-4589-a489-ac640c331f7a">

### 4. Delete comment
 - Method: POST
- Endpoint: comments/
- Screenshot:
<img width="1020" alt="Screenshot 2024-07-23 at 12 48 29 PM" src="https://github.com/user-attachments/assets/e08ba4a7-b1cd-42bd-945a-ba5fdfa9d630">


# Testing

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

## Project Structure

- `BlogApplication/`: Project settings and configuration.
  - `settings.py`: Configuration settings.
  - `urls.py`: Project-wide URL routing.
- `blog/`: Contains the Django app for Blog Application.
  - `models.py`: Defines the `Posts` and `Comments` models.
  - `views.py`: Contains API views for posts and comments.
  - `serializers.py`: Serializers for the models.
  - `urls.py`: URL routing for the app.


<!-- ## Notes -->
<!-- 
- Ensure that MySQL server is running and accessible with the credentials provided.
- Adjust database configurations in `settings.py` as necessary.

For any issues or further questions, please refer to the [Django documentation](https://docs.djangoproject.com/en/stable/) or the [Django REST Framework documentation](https://www.django-rest-framework.org/).
``` -->

<!-- You can copy and paste this markdown into a `README.md` file in your project repository. It includes an overview of the project, setup instructions, details about the API endpoints, and testing guidelines. -->

