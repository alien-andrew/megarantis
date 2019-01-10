import redis
import os

db_host = os.environ['MEGARANTIS_DB_SERVICE_SERVICE_HOST']
print( db_host )

r = redis.Redis(host=db_host, port=6379, db=0)

def setValRedis( key, val ):
  r.set( key, val )
  return;

def getValRedis( key ):
  val = r.get( key )
  return val; 
