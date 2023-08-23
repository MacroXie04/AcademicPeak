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
## Start nginx
>sudo nginx
## Stop nginx
>sudo nginx -s stop
## Start web server
>uwsgi --ini uwsgi.ini
## Stop web server
>uwsgi --stop uwsgi.pid

