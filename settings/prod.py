import os


REDIS_URI = os.environ["REDISCLOUD_URL"]
MONGO_URI = os.environ["MONGOHQ_URL"]
AMQP_URI = os.environ["CLOUDAMQP_URL"]
EXT_AMQP_URI = os.environ["X_RABBITMQ_BIGWIG_URL"]
PUSHW_AUTH_TOKEN = os.environ["PUSHW_AUTH_TOKEN"]
PUSHW_AUTH_KEY = os.environ["PUSHW_AUTH_KEY"]
