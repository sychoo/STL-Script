
# Thu Dec 17 13:43:57 EST 2020
# Simon Chu
from stl.api.signal import Signal

# sample Python program to demonstrate the usage of Signal api
# note that signal1, 2, 3, and 4 are equivalent upon creation

# === create a signal from scratch ===

# adding signal content using JSON string
signal1 = Signal()
signal1.add(json_str='''{ "param" : 7 }''')
signal1.add(json_str='''{ "param" : 10 }''')

# adding signal content using Python dictionary
signal2 = Signal()
signal2.add(py_dict={"param" : 7})
signal2.add(py_dict={"param" : 10})


# create a signal from a existing JSON-formatted signal
json_str = """
    {
        "0" : {
            "content" : {
                    "param" : 7
            }
        },

        "1" : {
            "content" : {
                    "param" : 10
            }
        }
    }
"""
signal3 = Signal(json_str=json_str)

# create a signal from a python dictionary formatted signal
py_dict = {
    "0" : {
        "content" : {
                "param" : 7
        }
    },

    "1" : {
        "content" : {
                "param" : 10
        }
    }
}

signal4 = Signal(py_dict=py_dict)

assert signal1.get_json_str() == signal2.get_json_str()
assert signal1.get_json_str() == signal3.get_json_str()
assert signal1.get_json_str() == signal4.get_json_str()

# testing section
json_str_2 = """
    {
        "0" : {
            "content" : {
                    "param" : 7
            }
        },

        "1" : {
            "content" : {
                    "param" : 10,
                    "param_2" : 15
            }
        }
    }
"""

signal5 = Signal(json_str_2)

assert signal5.get_quantifiable_keys() == ["param"]

