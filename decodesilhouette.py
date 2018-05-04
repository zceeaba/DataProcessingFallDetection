import base64
def decodesilhouette(silhouettestring):
    decode=base64.b64decode(silhouettestring)
    return decode