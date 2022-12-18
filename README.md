# Piccolo Admin
Admin panel for  https://github.com/RomanZorkin/fitnes_endpoint

This service start database & admin web service.
#
## Installation:

```bash
python -m venv venv
source venv/bin/activate
pip install poetry
poetry install
```
#
## You need create .env file with rules:
```
DATABASE_URL=://vasy:123@db:5432/piccolo_admin

# to create postgres in container
POSTGRES_PASSWORD=123
POSTGRES_USER=vasy
POSTGRES_DB=piccolo_admin
```
#
## You need create table scheme in DB, add admin user, just input commands:
```bash
piccolo migrations forwards session_auth
piccolo migrations forwards user
piccolo user create
piccolo migrations new home --auto
piccolo migrations forwards home
```
#
## Now we can start service:

```bash
make run
```
### 
vasy
@95147fg