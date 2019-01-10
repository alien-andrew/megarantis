from flask import Flask
import db  

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, world'

@app.route('/dbtest')
def db_test(): 
  db.setValRedis( 'testkey', 'testval')
  val = db.getValRedis( 'testkey' ) 
  return 'val = '+val

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
