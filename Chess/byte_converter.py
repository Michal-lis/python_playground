import math
import pprint

units = ("B", "KB", "MB", "GB")


# initial value in bytes - display in KB, MB, and GB
def converter(b):
    to_kb = math.pow(2, 10)
    kb = round(b / to_kb, 2)
    to_mb = math.pow(2, 20)
    mb = round(b / to_mb, 2)
    to_gb = math.pow(2, 30)
    gb = round(b / to_gb, 2)
    return b, kb, mb, gb


pprint.pprint(converter(537395200))
