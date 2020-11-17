# 2020-11-15 17:22:09 Sun
# Designed by Simon Chu


class Type:
    """super class for all types"""
    pass
    def __init__(self, type_str):
        self.type_str = type_str

    def __eq__(self, other):
        # print("self: " + self.type_str)
        # print("other: " + other.type_str)
        if other != None:
            return self.type_str == other.type_str
        else:
            return False
    
    def __ne__(self, other):
        # print("self: " + self.type_str)
        # print("other: " + str(other))

        if other != None:
            return self.type_str != other.type_str
        else:
            # when other is None, self is of a type, return true
            return True

    def __str__(self):
        return self.type_str + "_Type"
class Primitive_Type(Type):
    pass
    
class Custom_Type(Type):
    """
    TODO: allow user to define type using struct like syntax (similar to ReasonML),
    and then look up in the type context to match the defined type
    """
    pass

# class Parametric_Type(Type):
    # pass
