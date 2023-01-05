from json import JSONEncoder


class JsonManager(JSONEncoder):
    def default(self, obj):
        return obj.__dict__
