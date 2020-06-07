class StringHandler(object):
    def init(self,string,language= "german"):
        self.string = string    
        self.language = language
    def remove_special_character(self):
        dict_sc = {}
        if self.language == "german":
            dict_sc['ü'.encode()] = b'ue'
            dict_sc['Ü'.encode()] = b'Ue'
            dict_sc['ä'.encode()] = b'ae'
            dict_sc['Ä'.encode()] = b'Ae'
            dict_sc['ö'.encode()] = b'oe'
            dict_sc['Ö'.encode()] = b'Oe'
            dict_sc['ß'.encode()] = b'ss'     
        string = self.string
        string = string.encode()
        keys = list(dict_sc.keys())
        values = list(dict_sc.values())
        for I in range(len(keys)):
            string = string.replace(keys[I],values[I])
        string = string.decode('utf-8')
        return string
    
# sh = StringHandler()
# sh.string = "ü"
# sh.remove_special_character()