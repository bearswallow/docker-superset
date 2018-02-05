FROM amancevice/superset

ENV SUPERSET_METADATA_CONNECTION=mysql://root:gt86589089@galera-lb.galera:3306/superset \
    CACHE_REDIS_URL=redis://redis-master.Redis-cluster:6379/1 \
    APPLICATION_PREFIX=superset \
    BROKER_URL=redis://redis-master.Redis-cluster:6379/1 \
    CELERY_RESULT_BACKEND=redis://redis-master.Redis-cluster:6379/1

USER root
COPY superset_config.py /etc/superset/
ADD --chown=superset:superset check_init.py /superset/
COPY --chown=superset:superset superset-start.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/superset-start.sh /superset/check_init.py
USER superset

ENTRYPOINT [ "sh" ]
CMD [ "/usr/local/bin/superset-start.sh" ]
