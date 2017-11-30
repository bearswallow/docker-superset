# docker-superset
Dockerfile and configuration files for superset web server, using following settings.
- mysql as metadata storage
- redis as result cache
- redis as asyc query message broker
- redis as asyc query result storage

# docker specification
The docker image should be used together with [docker-superset-init](https://hub.docker.com/r/malebear311/docker-superset-init/) and [superset-worker](https://hub.docker.com/r/malebear311/superset-worker/). Use *docker-superset-init* as setup that is only execute once.

```
docker run -d --name=superset -p 8088:8088 malebear311/superset
```

You can specify following ENVs when execute docker run command. So the container will create with your config.
- SUPERSET_METADATA_CONNECTION: mysql url of superset metadata storage, must like *mysql://root:gt86589089@galera-lb.galera:3306/superset*.
- APPLICATION_PREFIX: key prefix of data cache and async query result.
- CACHE_REDIS_URL: redis url of data cache, must like *redis://redis-master.Redis-cluster:6379/1*.
- BROKER_URL: redis url of async message broker, must like *redis://redis-master.Redis-cluster:6379/1*.
- CELERY_RESULT_BACKEND: redis url of async query result storage, must like *redis://redis-master.Redis-cluster:6379/1*.

These ENV's values must be identical to [docker-superset-init](https://hub.docker.com/r/malebear311/docker-superset-init/) and [superset-worker](https://hub.docker.com/r/malebear311/superset-worker/).