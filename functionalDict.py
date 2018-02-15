# functional dictionary
class functionalDict():
    def __init__(self,_dict={}):
        self.Dict = _dict

    @classmethod
    def fromDict(_dict):
        ??
    def __setitem__(self,key,value):
        self.Dict[key] = value

    def __getitem__(self,key):
        return self.Dict[key]

    def toList(self):
        return self.Dict.items()
    
    def mapPairs(Fun, keyExclude=[]):
        newDict = functionalDict()
        newDict.Dict = dict([(k[0],Fun(k)) for k in self.Dict.items() if k[0] not in keyExclude])
        return 

    def mapValues(Fun, keyExclude=[]):
        return dict([(k[0],Fun(k[1])) for k in self.Dict.items() if k[0] not in keyExclude])

