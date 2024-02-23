# WeatheNow Application Using Django

## Overview
This document outlines the structure and functionality of a Django-based web application designed to display weather information for specified cities. The application utilizes Django, a high-level Python web framework, for server-side logic, form handling, and rendering dynamic content. It incorporates HTML/CSS for the user interface and leverages external libraries such as Bulma for styling and Particle.js for animated backgrounds.

## Repository Structure
- `manage.py`: Django's command-line utility for managing administrative tasks.
- `weatherInfo/`: Django project directory containing settings, URL configurations, and WSGI configuration.
  - `settings.py`: Configuration settings for the Django project.
  - `urls.py`: URL configuration for the project.
  - `wsgi.py`: WSGI application object for the project.
- `mainApp/`: Django app directory containing models, views, forms, and templates for the main application functionality.

## Installation Guide
1. Clone the repository to your local machine.
2. Create a virtual environment:
   ```python -m venv env```
3. Activate the virtual environment:
   - On Windows:
     ```env\Scripts\activate```
   - On macOS/Linux:
     ```source env/bin/activate```
4. Install dependencies:
   ```pip install -r requirements.txt```
5. Apply migrations:
   ```python manage.py migrate```
6. Run the development server:
    ```python manage.py runserver```

## Usage
1. Access the application in your web browser at `http://localhost:8000`.
2. Enter a city name in the provided form and click "Check" to retrieve weather information.
3. View weather details including temperature, humidity, pressure, wind speed, and description.

## Deployment Considerations
- Set `DEBUG` to `False` in production settings.
- Configure a production database (e.g., PostgreSQL) in `settings.py`.
- Serve static files using a web server or CDN.
- Secure sensitive information such as `SECRET_KEY` and database credentials.

## Contact
For questions or support, please contact the project maintainer:

[Bernard George Charles](https://github.com/MeGaTroNOO7)
