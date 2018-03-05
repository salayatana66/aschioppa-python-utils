# functional dictionary

class functionalDict():
    def __init__(self):
        self.Dict = {}

    @staticmethod
    def fromDict(_dict,copy=False):
        out = functionalDict()
        if copy:
            out.Dict = _dict.copy()
        else:
            out.Dict = _dict
        return out

    def __setitem__(self,key,value):
        self.Dict[key] = value

    def __getitem__(self,key):
        return self.Dict[key]

    def toList(self):
        return self.Dict.items()

    def mapPairs(self,Fun):
        return functionalDict.fromDict(
            dict([Fun(k) for k in self.Dict.items()])
            )

    def mapKeys(self, Fun):
        return functionalDict.fromDict(
            dict([(Fun(k[0]),k[1]) for k in self.Dict.items()])
            )

    def mapValues(self, Fun):
        return functionalDict.fromDict(
            dict([(k[0],Fun(k[1])) for k in self.Dict.items()])
            )

    def filterPairs(self,Fun):
        return functionalDict.fromDict(
            dict([(k[0],k[1]) for k in self.Dict.items() if Fun(k)])
            )

    def filterKeys(self,Fun):
        return functionalDict.fromDict(
            dict([(k[0],k[1]) for k in self.Dict.items() if Fun(k[0])])
            )

    def filterValues(self,Fun):
        return functionalDict.fromDict(
            dict([(k[0],k[1]) for k in self.Dict.items() if Fun(k[1])])
            )

    def update(self, fDict2):
        self.Dict.update(fDict2.Dict)

    def __str__(self):
        return str(self.Dict)

# Tests
if __name__ == "__main__":
    fD = functionalDict.fromDict({"a" : 1, "b" : 2})
    fD["c"] = 3
    try:
        fD["d"]
    except KeyError:
        print("Ooops")
    print(fD)
    print(fD.filterValues(lambda x : x % 2 == 0))
    print( (fD.filterValues(lambda x : x % 2 == 0)
           .mapKeys(lambda x : x + "5")
           .mapValues(lambda x : x + 20)
           ))
