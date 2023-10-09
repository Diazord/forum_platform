﻿# Forum platform

Project can only be run on a local machine.
First you need to clone project:
```
git clone https://github.com/Diazord/forum_platform "your_folder"
```
Secondary make sure you're in project folder:
```
pwd

Path
----
C:\your\project\"your_folder"
```
If you're not here, just use:
```
cd "your_folder"
```
After that you should do migrations:
```
python manage.py makemigrations && python manage.py migrate
```
Now you're ready to run project:
```
python manage.py runserver 127.0.0.1:8000
```
