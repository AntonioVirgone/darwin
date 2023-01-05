class DataDocument:
    def __init__(self,
                 projectName,
                 directoryName,
                 fileName,
                 serviceName,
                 serviceVersion,
                 gkeServiceName,
                 commandList):
        self.projectName = projectName
        self.directoryName = directoryName
        self.fileName = fileName
        self.serviceName = serviceName
        self.serviceVersion = serviceVersion
        self.gkeServiceName = gkeServiceName
        self.commandList = commandList

    @staticmethod
    def fromJson(json):
        print("json is %s" % json)
        return DataDocument(json['projectName'],
                            json['directoryName'],
                            json['fileName'],
                            json['serviceName'],
                            json['serviceVersion'],
                            json['gkeServiceName'],
                            json['commandList'])
