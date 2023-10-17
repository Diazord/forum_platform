# Forum platform

Project can only be run on a local machine.
* First you need to clone project:

```bash
$ git clone https://github.com/Diazord/forum_platform
```

Secondary go in project folder:
```bash
$ cd forum_platform
```

* After that you should do migrations:
```bash
$ python manage.py makemigrations && python manage.py migrate
```

* Now you're ready to run project:
```bash
$ python manage.py runserver 127.0.0.1:8000
```
