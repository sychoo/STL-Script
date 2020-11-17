from core_types import Primitive_Type

class Int_Type(Primitive_Type):
    def __init__(self):
        super(Int_Type, self).__init__("INT")

class Boolean_Type(Primitive_Type):
    def __init__(self):
        super(Boolean_Type, self).__init__("BOOLEAN")

class Float_Type(Primitive_Type):
    def __init__(self):
        super(Float_Type, self).__init__("FLOAT")

class String_Type(Primitive_Type):
    def __init__(self):
        super(String_Type, self).__init__("STRING")

class STL_Type(Primitive_Type):
    def __init__(self):
        super(STL_Type, self).__init__("STL")