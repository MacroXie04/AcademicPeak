# deploy
## Django project path
> cd /var/www/hongzhe
## Enter virtualenv
>source bin/activate
## Recollect static files
>python manage.py collectstatic
## Restart uwsgi
>uwsgi --reload uwsgi.pid
## Reload nginx
>nginx -s reload
## Start web server
>nginx
>uwsgi --ini uwsgi.ini
## Stop web server
>uwsgi --stop uwsgi.pid

