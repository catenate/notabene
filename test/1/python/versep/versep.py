import sys

ver = sys.argv[1].replace("_", ".")
ver = ver.split(".")
if len(ver) == 2:
	ver += '0'
print ver
