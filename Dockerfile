FROM amancevice/superset

ENV SUPERSET_METADATA_CONNECTION=mysql://root:gt86589089@galera-lb.galera:3306/superset \
    CACHE_REDIS_URL=redis://redis-master.Redis-cluster:6379/1 \
    APPLICATION_PREFIX=superset \
    BROKER_URL=redis://redis-master.Redis-cluster:6379/1 \
    CELERY_RESULT_BACKEND=redis://redis-master.Redis-cluster:6379/1

COPY superset_config.py /etc/superset/