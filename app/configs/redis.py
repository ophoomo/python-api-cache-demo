import json
import redis
from app.configs.setting import get_settings
from sqlalchemy.ext.declarative import DeclarativeMeta

setting = get_settings()

# connecting redis
r = redis.Redis(host=setting.REDIS_ENDPOINT, username=setting.REDIS_USERNAME, password=setting.REDIS_PASSWORD,
                 port=setting.REDIS_PORT, db=0, decode_responses=True)

# function ส่งตัวแปร r ออกไป
def get_redis():
    return r

# object to json
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)