# Wagtail Accounts Application

This is the `accounts` application for managing user accounts in a Django project. It includes functionalities such as user registration, login, and logout.

## Features

- User registration
- User login
- User logout
- Signal to automatically create a `Member` profile when a user registers

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/accounts.git
cd accounts
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add the accounts application to your Django project's INSTALLED_APPS:

```python
# settings.py or in Wagtail : your_app/settings/base.py
INSTALLED_APPS = [
    ...
    'accounts',
    ...
]
```

4. Include the accounts URLs in your project's URL configuration:

```python
# urls.py
urlpatterns = [
    ...
    path('accounts/', include('accounts.urls')),
    ...
]
```

5. Apply migrations:

```bash
python manage.py makemigrations accounts
python manage.py migrate
```

## Usage

### Register a new user

Visit the /accounts/register/ URL to register a new user.

### Login

Visit the /accounts/login/ URL to log in.

### Logout

Visit the /accounts/logout/ URL to log out.

### License

This project is licensed under the MIT License - see the LICENSE file for details.