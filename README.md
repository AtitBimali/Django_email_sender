# Django_email_sender
Django app to automate emails.
Add your gmail and password in settings.py located inside email_sender folder (at line number 126 & 127)
Also turn on less secure apps : https://myaccount.google.com/u/2/lesssecureapps 
This features enables us to use our gmail account to send mails.

First Thing To Do:
```
python manage.py magemigrations
```

```
python manage.py migrate
```


Running the app:
``` 
Python manage.py runserver
```
Server starts at: http://127.0.0.1:8000/ From there you can type any valid gmail account you want to send an email and click on submit.
You can change the subject and title of the mail on views.py located inside core folder (at line 21 & 22).
