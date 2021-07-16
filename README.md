# Django w/h docker-compose project
-----------------------------------

# Run project
-------------
```
docker-compose up
```

Docker settings
---------------

Moved to [settings](https://docs.docker.com/compose/install/)

Create superuser
-----------------
```
docker-compose run django bash
./manage.py createsuperuser
```
