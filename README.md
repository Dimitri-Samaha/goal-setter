# Goal Setter

A Django web app for setting personal goals with deadlines and tracking whether they've been completed. Goals are stored in a MySQL table via a small hand-written DB wrapper rather than Django's ORM.

## Tech stack
- Python, Django
- MySQL (accessed through `mysql-connector-python`, queried by `SQL/sql_connector.py`)
- `mysqlclient` (`MySQLdb`) is also imported by `home/forms.py`

## Requirements
```
pip install django mysql-connector-python mysqlclient
```
A local MySQL server is required, reachable with the credentials hardcoded in `SQL/sql_connector.py` (`root` / `root` on `localhost`), with a database matching what `home/views.py` connects to.

## Running it
```
python manage.py migrate
python manage.py runserver
```
Then open http://127.0.0.1:8000/.

## Structure
- `Goal_Setter/` — Django project settings, URLs, WSGI/ASGI entry points.
- `home/` — the single Django app: views, forms, templates, and `modules.py` (the `Goal` data class).
- `SQL/sql_connector.py` — a generic `Connector` class wrapping `mysql.connector` for raw SQL queries (`get_data`, `add_data`, `delete_data`, `sort_data`).
