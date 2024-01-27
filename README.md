# Token authentication system using Django REST Framework

## This project provides a simple **Token** authentication, using Django REST Frameword.
## In this system provided 2 API-Endpoints:
- To user login
- To register a new user 

# Installation
```bash
git clone https://github.com/snomfake/drf-token-auth-system.git
cd drf-token-auth-system
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
### Don't forget to change the database settings!!!

# Usage

## Create a new user
```bash
curl -sS -X POST \
-H "Content-Type: application/json" \
-d '{"username": "admin", "password":"ultra_secret_password"}' \
http://localhost:8000/token/signup/ | jq

{
  "token": "0cb22116303bde62e5194241826413fb5d29bfc7"
}
```

## Login user
```bash
curl -sS -X POST \
-H "Content-Type: application/json" \
-d '{"username": "admin", "password":"ultra_secret_password"}' \
http://localhost:8000/token/login/ | jq

{
  "token": "0cb22116303bde62e5194241826413fb5d29bfc7"
}
```

## If data not correct
```bash

curl -sS -X POST \
-H "Content-Type: application/json" \
-d '{"username": "admin", "password":"no_secret_password"}' \
http://localhost:8000/token/login/ | jq

{
  "detail": "Not found"
}
```
