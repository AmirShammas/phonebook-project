# Phonebook-Project

This app creates a phonebook using Django Templates and sqlite database.

## Installation

This app is developed using python 3.11.

After making venv, install the necessary packages using the command below:

```
pip install -r requirements.txt
```

## Usage

Copy `sample_settings.py` file and rename it to `local_settings.py`.

To generate the secret key, run the command below:

```
py -c "import secrets; print(secrets.token_urlsafe())"
```

Copy and paste this new value into the `local_settings.py` under the variable `SECRET_KEY`.

Run the server:

```
py manage.py runserver
```

## Endpoints and Permissions

You have not access to any endpoint without authentication.

After authentication as a regular-user, you have limited access to endpoints.

Only the super-user has access to all endpoints.

## Accounts Endpoints

`http://localhost:8000/accounts/signup/` => Sign up the new user.

`http://localhost:8000/accounts/login/` => Login the user.

`http://localhost:8000/accounts/logout/` => Logout the user.

## Phones Endpoints

`http://localhost:8000/`  => Home page.

`http://localhost:8000/phone/`  => Display all phones.

`http://localhost:8000/phone/new/`  => Create a new phone.

`http://localhost:8000/phone/1/`  => Display the phone which `id=1`.

`http://localhost:8000/phone/1/edit/`  => Edit the phone which `id=1`.

`http://localhost:8000/phone/1/delete/`  => Delete the phone which `id=1`.

### Task List

- [x] phones
- [ ] admin panel
- [ ] cities
- [ ] users
- [ ] filter
- [ ] search
- [ ] pagination
- [ ] image upload
- [ ] rss feed
- [ ] user profile
