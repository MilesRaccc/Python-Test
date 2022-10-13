class TreeStore:
    def __init__(self, content):
        self.__content = content

    def getAll(self):
        return self.__content

    def getItem(self, id):
        for dic in self.__content:
            if dic["id"] == id:
                return dic
        return None

    def getChildren(self, parent):
        return list(filter(lambda x: x["parent"] == parent, list(self.__content)))

    def getAllParents(self, id):
        result = list()
        item = self.getItem(id)
        first_iteration = True
        while item is not None:
            if first_iteration:
                first_iteration = False
            else:
                result.append(item)
            item = self.getItem(item["parent"])
        return result


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)


print(ts.getAllParents(7))

# Примеры использования:
#  - ts.getAll() // [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#
#  - ts.getItem(7) // {"id":7,"parent":4,"type":None}
#
#  - ts.getChildren(4) // [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#  - ts.getChildren(5) // []
#
#  - ts.getAllParents(7) // [{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]