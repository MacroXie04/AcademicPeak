# Academic Peak
This is a Django and Python based website, build for academic need. 

## Website structure
### Django installed Application
| Url       | function                                |
|-----------|-----------------------------------------|
| /         | Academic Peak main site                 |
| /markdown | display and edit note in markdown format |
| /admin    | Django database management              |


## Deploy
### Download this project
> Need Python enviorment, and Django version = 5.0.
#### download via git
``` shell
git clone https://github.com/MacroXie/AcademicPeak.git
```

#### install Python requirements.txt
``` shell
pip install -r requirements.txt
```

#### create database
``` shell
python manage.py migrate
```

#### collect static files
``` shell
python manage.py collectstatic
```  

```shell
python manage.py createsuperuser
```  

#### Deploy via Django test server (not recommended)
``` python
python manage.py runserver
```

#### Deploy to public server (recommended)
[Django Documents](https://docs.djangoproject.com/zh-hans/5.0/howto/deployment/)





