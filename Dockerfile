FROM python:3.13.0b1-apline

RUN pip install -r requirements.txt

CMD python manage.py migrate && python manage.py runserver
