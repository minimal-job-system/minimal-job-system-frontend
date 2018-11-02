# Minimal Job System - Frontend
Minimal Job System Frontend is a minimalistic Django app for submitting technology-independent jobs via a web interface.

Detailed documentation is in the "docs" directory.

## Quick start
1. Activate the Django virtual environment and install app via PIP::

    pip install .

2. Setup Minimal Job System API (see corresponding docs)

4. Add the Minimal Job System Frontend into a Django project site::

    <django_site>/settings.py
    INSTALLED_APPS [ ..., 'job_system_frontend' ]
    <django_site>/urls.py
    urlpatterns = [ ..., url(r'^frontend/', include('job_system_frontend.urls')) ]

5. (Optionally)
   Define a title and icon for the frontend application in settings.py within your Django project::

    CONSTANCE_CONFIG = {
      'JOB_SYSTEM_TITLE': (
        'Minimal Job System', 'Title of the Job System application'
      ),
      'JOB_SYSTEM_ICON': (
        'job_system_app/img/default.ico', 'Icon of the Job System application'
      )
    }

5. Run `python manage.py migrate database` to create the Django Constance models required by the Minimal Job System Frontend

