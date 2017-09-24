import json
import ntpath
import requests
import copy
from pprint import pprint

class AirWatchClient():
    def __init__(self):
       
        # AirWatch API settings
        self.url = "https://cn888.awmdm.com"
        self.headers = {
            'aw-tenant-code': "2Uc3HIkYpQoLiNIex03gvTMRdwhjgyHHGRFjOy4L+BQ=",
            'accept': "application/json",
            'authorization': "Basic Zm9kbWRtYWRtaW5AZml0bmVzc29uZGVtYW5kMjQ3LmNvbTpGaXRuZXNzT25EZW1hbmQyNDch",
            'cache-control': "no-cache",
            'postman-token': "7038ad62-5984-d186-5061-66eb19203740"
        }

        self.jsonHeaders = copy.copy(self.headers)
        self.jsonHeaders['content-type'] = 'application/json'

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

    def internalApplicationSave(self, applicationName, deviceModelID, blobID):
        url = "{baseUrl}/api/mam/apps/internal/begininstall".format(
            baseUrl = self.url,
        )        

        data = {
            'ApplicationName': applicationName,
            'BlobId': blobID,
            'AutoUpdateVersion': False,
            'DeviceType': deviceModelID,
            'PushMode': 'OnDemand',
            "SupportedModels": {
                "Model": [
                    {
                        "ModelId": deviceModelID,
                    }
                ]
            }
        }

        jsonData = json.dumps(data)

        response = requests.post(headers = self.jsonHeaders, url = url, data = jsonData)

        print response.status_code
        print response.content

    def updateInternalApplication(self, applicationID, blobID):
        url = "{baseUrl}/api/mam/apps/internal/{applicationID}".format(
            baseUrl = self.url,
            applicationID = applicationID
        )        

        data = {
        }

        jsonData = json.dumps(data)

        response = requests.put(headers = self.jsonHeaders, url = url, data = jsonData)

        print response.status_code
        print response.content

    def getInternalApplication(self, applicationID):
        url = "{baseUrl}/api/mam/apps/internal/{applicationID}".format(
            baseUrl = self.url,
            applicationID = applicationID
        )

        data = {}

        jsonData = json.dumps(data)        

        response = requests.get(headers = self.jsonHeaders, url = url, data = jsonData)

        print response.status_code
        print response.content



airWatchClient = AirWatchClient()

# airWatchClient.uploadNewApplicationVersion("app-production-release15.apk", 799)
appicationID = 2634
applicationName = 'FOD Gen5 KSH'
androidModelID = 5
blobID = 837977
airWatchClient.internalApplicationSave(applicationName, androidModelID, blobID)

# airWatchClient.updateInternalApplication(appicationID, blobID)

# airWatchClient.getInternalApplication(appicationID)