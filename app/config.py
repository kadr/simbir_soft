class Config(object):
    """Конфигурация для Флака"""

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://simbirsk_soft:156489@db/simbirsk_soft'
    SECRET_KEY = 'sdkljslajfps098sdf09jflk43lrjfslkdnl'
    REDIS_URL = "redis://:156489@redis"
