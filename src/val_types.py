from sys import path

# path.append("Type")

from src.Type.core_types import\
    Type,\
    Primitive_Type,\
    Custom_Type

from src.Type.primitive_types import\
    Int_Type,\
    Boolean_Type,\
    Float_Type,\
    String_Type,\
    STL_Type,\
    List_Type,\
    Tuple_Type

class Type_Selector:
    @staticmethod
    def select(type_str):
        """select the primitive types, otherwise, wrap the string around a type object"""
        # handle primitive types
        if type_str == "INT":
            return Int_Type()
        
        elif type_str == "BOOLEAN":
            return Boolean_Type()
        
        elif type_str == "FLOAT":
            return Float_Type()
        
        elif type_str == "STRING":
            return String_Type()

        elif type_str == "STL":
            return STL_Type()
        
        # elif type_str == "LIST":
        #     return List_Type()
        
        elif type_str == "TUPLE":
            return Tuple_Type()

        # case when the type string passed in is not a pre-defined primitive type
        else:
            return Custom_Type(type_str)