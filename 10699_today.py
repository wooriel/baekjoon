# -*- coding: utf-8 =*=
from datetime import datetime

if __name__ == "__main__":
    # y = date.year
    # m = date.month
    # d = date.day
    current = datetime.utcnow()
    print("{}-{}-{}".format(current.year, str(current.month).zfill(2), str(current.day).zfill(2)))
    # date.isoformat