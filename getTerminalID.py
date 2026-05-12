import subprocess as sp
import platform as pf
import base64
import hashlib
from datetime import datetime 


def getArch():
    arch = pf.machine()
    encoded_bytes = base64.b64encode(arch.encode('utf-8'))
    return encoded_bytes.decode('utf-8'), arch
    
def buildTID():
    terminalID = None
    try:
      nonBaseArch, baseArch = getArch()
      sign0 = nonBaseArch + baseArch
      terminalID = hashlib.md5(sign0.encode()).hexdigest()
    except Exception as e:
      print(e)
    return terminalID
            