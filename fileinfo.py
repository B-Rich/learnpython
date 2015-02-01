from  import 


class Fileinfo(UserDict):
    "store file metadata"
    def __inti__(self, filename=None):
        UserDict.__inti__(self)
        self["name"]=filename
    
