# piccolo_project

## Setup

piccolo asgi new

### Install requirements

```bash
pip install -r requirements.txt
```

### Getting started guide

```bash
python main.py
```

### Running tests

```bash
piccolo tester run
```


python -m venv venv
source venv/bin/activate
pip install poetry
poetry install

make .env file


docker-compose up -d
uvicorn app:app --port 1400 --host 0.0.0.0

piccolo migrations forwards session_auth
piccolo migrations forwards user
piccolo user create
piccolo migrations new home --auto
piccolo migrations forwards home

vasy
@95147fg