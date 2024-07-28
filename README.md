# Django Posts and Users App

## Overview

This is a Django application for managing posts and users.

## Setup

To get started with the project, follow these steps:

1. **Clone the Repository and and navigate to the project directory (myproject).**:

2. **Install Dependencies**: Installs required Python packages from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**: Applies database migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

4. **Create a Superuser**: Sets up an admin user for accessing the Django admin interface.

```bash
 python3 manage.py createsuperuser
```

5. **Run the Development** Server: Run the server. The server will start on port 8000

```bash
 python3 manage.py runserver
```
