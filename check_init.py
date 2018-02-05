from sqlalchemy import text, create_engine
import time
import os

def check_init(database_url, retry_times):
    has_inited = False
    connection = None
    db = create_engine(database_url, echo=True)
    while has_inited == False and retry_times >= 0:
        try:
            connection = db.connect()
            result = connection.execute(text("select * from tb_init"))
            has_inited = len(result._saved_cursor._rows) >= 1
            
            if has_inited == False:
                print("init has not finished, retry after 1 second.")
                time.sleep(1)
                retry_times = retry_times - 1
        except Exception:
            print("connect failed, retry after 1 second.")
            time.sleep(1)
            retry_times = retry_times - 1
        finally:
            if connection is not None:
                connection.close()

if __name__ == "__main__":
    database_url = os.getenv('SUPERSET_METADATA_CONNECTION') #"mysql://root:gt86589089@galera-lb.galera:3306/superset_test"
    check_init(database_url, 180)
