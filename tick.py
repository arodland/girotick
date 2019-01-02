import subprocess
import time
import os
import sys
import logging
import psycopg2

cwd = os.getcwd()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        #logging.FileHandler("{0}/{1}.log".format(logPath, fileName)),
        logging.StreamHandler(sys.stdout)
    ])

logger = logging.getLogger()

con = None

try:
    dsn = "dbname='%s' user='%s' host='%s' password='%s'" % (os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_HOST"), os.getenv("DB_PASSWORD"))
    con = psycopg2.connect(dsn)
except:
    logger.error("Unable to connect to the database")

cursor = con.cursor()

try:
    cursor.execute(open("dbsetup.sql", "r").read())
except:
    logger.error("Unable to execute database cursor")

cursor.close()
con.close()

starttime=time.time()
while True:
  logger.info("start tick")
  subprocess.call(['python', cwd + '/tread.py', '1', '4'])
  time.sleep(300.0 - ((time.time() - starttime) % 300.0))
