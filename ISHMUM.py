
#
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
