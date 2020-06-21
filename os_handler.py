from datetime import datetime
import pathlib

# https://stackoverflow.com/questions/39359245/from-stat-st-mtime-to-datetime


def get_last_mod(filename):
    """returns last modification date of filename
    Returns:
        dateime: last modification date of filename
    """
    p = pathlib.Path(filename)
    
    mod_time = p.stat().st_mtime
    mod_timestamp = datetime.fromtimestamp(mod_time)
    return mod_timestamp


if __name__ == "__main__":
    filename = r"C:\DEV\git\EED85\scrapping-pollination\src\data\51427.html"
    print(get_last_mod(filename))
    