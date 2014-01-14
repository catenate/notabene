import sys
import hashlib

def usage() :
    print 'usage: %s $file' % sys.argv[0]
    sys.exit(1)

if len(sys.argv) == 0:
    usage()

try :
    exe_path = sys.argv[1]
except :
    usage()

def sha1sum(f_path):
    h = hashlib.sha1()
    f = file(f_path, 'rb')
    while True :
        dat = f.read(2048)
        if len(dat) == 0 : break
        h.update(dat)
    return h.hexdigest()

print sha1sum(exe_path) + '	' + exe_path
