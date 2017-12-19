import os

#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
#ROW_LIMIT = 5000
#SUPERSET_WORKERS = 4

#SUPERSET_WEBSERVER_PORT = 8088
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
#SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = os.getenv('SUPERSET_METADATA_CONNECTION')

# Flask-WTF flag for CSRF
#WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
#WTF_CSRF_EXEMPT_LIST = []

# Set this API key to enable Mapbox visualizations
#MAPBOX_API_KEY = ''

# Allow users of Public role accessing anonymous
PUBLIC_ROLE_LIKE_GAMMA=True

applicationPrefix = os.getenv('APPLICATION_PREFIX')

# Cache config
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis', # 使用 Redis
    'CACHE_KEY_PREFIX': applicationPrefix + '_cache:', # 缓存项前缀
    'CACHE_REDIS_URL': os.getenv('CACHE_REDIS_URL') # 配置 URL
}

resultBackend = os.getenv('CELERY_RESULT_BACKEND')
# Celery work config, supporting async query
class CeleryConfig(object):
    BROKER_URL = os.getenv('BROKER_URL')
    CELERY_IMPORTS = 'superset.sql_lab'
    CELERY_RESULT_BACKEND = resultBackend
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}
CELERY_CONFIG = CeleryConfig

# config results backend
import re
m = re.match(r'redis://([^:/]+):([0-9]+)/([0-9]+)', resultBackend)
backendHost = m.group(1)
backendPort = int(m.group(2))
backDb = int(m.group(3))
from werkzeug.contrib.cache import RedisCache
RESULTS_BACKEND = RedisCache(
    host=backendHost, port=backendPort, db=backDb,
    key_prefix= applicationPrefix + "_results:")

# log environment variables for check
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("supersetConfig")
logger.info("metadata storage: " + SQLALCHEMY_DATABASE_URI)
logger.info("cache reidsUrl: " + CACHE_CONFIG['CACHE_REDIS_URL'])
logger.info("broker url: " + CeleryConfig.BROKER_URL)
logger.info("Result backend url:" + CeleryConfig.CELERY_RESULT_BACKEND)
logger.info("RedisCache: { host: %s, port: %s, db: %s, key_prefix: %s }" % tuple([backendHost, backendPort, backDb, RESULTS_BACKEND.key_prefix]))