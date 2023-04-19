Run: 

pip install django

C:\Users\Josh\startup\kickdwebsite\kickdURLHandling\kickdwebsite python manage.py runserver - Runs webserver from laptop

python manage.py startapp main - Creates our "main" application

https://docs.djangoproject.com/en/4.1/topics/http/urls/#how-django-processes-a-request

python manage.py makemigrations - like git commit for database changes

python manage.py migrate - like git push for database changes

views.py does all the backend processing

views.py populates dictionary and sends to to html/css frontend.

Example URL 
http://127.0.0.1:8000/?data=E00208014321B7E0xJOSHTESTx911

https://kickd.io/E0020801431E72E3xPOOPEATRx111

Youtube series I have been following along:
https://www.youtube.com/watch?v=Z4D3M-NSN58&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9&index=1&t=1063s