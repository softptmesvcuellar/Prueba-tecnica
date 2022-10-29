import os
import time
import gzip


def dump_db(host, port, user, passwd, db):
    date = time.strftime('%Y-%m-%d-%I')
    os.popen(
        f"mysqldump -h {host} -P {port} -u {user} -p{passwd} {db} > {db}_{date}.sql").read()
    with open(f"{db}_{date}.sql", 'rb') as fin, gzip.open(f"{db}_{date}.sql.gz", 'wb') as fout:
        fout.writelines(fin)
    os.remove(f"{db}_{date}.sql")
    return f"{db}_{date}.sql.gz"
