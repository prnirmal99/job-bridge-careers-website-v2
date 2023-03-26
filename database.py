import os
from sqlalchemy import create_engine,text
 
db_connection_string= os.environ['DB_CONNECTION_STRING']



engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(type(result))
    result_as_dict = result.mappings().all()
    print(type(result_as_dict))
    jobs=[]
    for row in result_as_dict:
      jobs.append(row)
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"), {'val': id})
    rows = result.mappings().all()
    print(rows)
    print(type(rows))
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])