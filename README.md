# Forum platform

Project can only be run on a local machine.
* First you need to clone project:

```bash
$ git clone https://github.com/Diazord/forum_platform "your_folder"
```

* Secondary make sure you're in project folder:
```bash
$ pwd

Path
----
C:\your\project\"your_folder"
```

If you're not here, just use:
```bash
$ cd "your_folder"
```

* After that you should do migrations:
```bash
$ python manage.py makemigrations && python manage.py migrate
```

* Now you're ready to run project:
```bash
$ python manage.py runserver 127.0.0.1:8000
```
