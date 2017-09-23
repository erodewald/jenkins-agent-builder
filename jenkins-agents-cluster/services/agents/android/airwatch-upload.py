import json
import ntpath
import requests
from pprint import pprint

class AirWatchClient():
    def __init__(self):
       
        # AirWatch API settings
        self.url = "https://cn888.awmdm.com"
        self.headers = {
            'aw-tenant-code': "2Uc3HIkYpQoLiNIex03gvTMRdwhjgyHHGRFjOy4L+BQ=",
 #           'content-type': "application/json",
            'accept': "application/json",
            'authorization': "Basic Zm9kbWRtYWRtaW5AZml0bmVzc29uZGVtYW5kMjQ3LmNvbTpGaXRuZXNzT25EZW1hbmQyNDch",
            'cache-control': "no-cache",
            'postman-token': "7038ad62-5984-d186-5061-66eb19203740"
        }

    def uploadNewApplicationVersion(self, filePath, organizationGroupID):
        blobID = self.uploadBlob(filePath, organizationGroupID)
        print blobID

    def uploadBlob(self, filePath, organizationGroupID):
        filename = ntpath.basename(filePath)
        url = "{baseUrl}/api/mam/blobs/uploadblob?filename={filename}&organizationgroupid={organizationGroupID}&moduleType=Application".format(
            baseUrl = self.url,
            filename = filename,
            organizationGroupID = organizationGroupID
        )

        data = open(filePath, 'rb').read()

        response = requests.post(headers = self.headers, url = url, data = data)

        content = json.loads(response.content)
        return content["Value"]

airWatchClient = AirWatchClient()

airWatchClient.uploadNewApplicationVersion("app-production-release.apk", 799)