import json


class DirectoryViewModel:
    def __init__(self, directoryCode, directoryName):
        self.directoryCode = directoryCode,
        self.directoryName = directoryName


class DirectoryViewModelEncoder(json.JSONEncoder):
    def default(self, obj):
        return [obj.directoryCode, obj.directoryName]
