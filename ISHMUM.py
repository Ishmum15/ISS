# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
