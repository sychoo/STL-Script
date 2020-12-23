# Wed 2020-12-16 17:11:04 EDT
# Created by Simon Chu
# define the standard format for the signal

import json
import stl.exceptions as exceptions
# from typing import Optional

# json.loads(JSON str) -> dict (decode)
# json.dumps(dict) -> JSON str (encode)
class Signal:
    
    def __init__(self, json_str=None, py_dict=None) -> None:
        """initialize the Signal object
            self.data: the python dictionary object that holds the signal
            self.next_index: the index of the next signal to be inserted
        """

        # case when both parameters are not given
        if json_str == None and py_dict == None:
            

            # initialize empty data
            self.data = dict()

            # set the next index to be inserted (initialize to 0)
            self.next_index = 0

        
        # user supplied both JSON and Python dictionary data
        elif json_str != None and py_dict != None:
           
            raise exceptions.Signal_Creation_Error("Ambiguity in creating Signal object. Supplied both JSON and Python dictionary data.")


        # one of the data is given
        else:
            
            # case when only JSON string is given or only Python dictionary is given
            # convert the json_str to py_dict
            if json_str != None and py_dict == None:
                py_dict = json.loads(json_str)
            
            # add py_dict to signal
            # verify the dictionary
            if Signal.static_verify_signal(py_dict):
                self.data = py_dict
            else:
                raise exceptions.Invalid_Signal_Error("Signal specified is Invalid! Could not verify Signal.")

            self.next_index = len(self.data)

    def __str__(self) -> str:
        return self.get_json_str()

    def get_json_str(self) -> str:
        """return the sorted keys/indented string representation of the JSON"""
        return json.dumps(self.data, sort_keys=True, indent=4)
        
    def print_json(self) -> None:
        """print the json string"""
        print(self.get_json_str())
    
    def add(self, json_str=None, py_dict=None) -> None:
        """add signal items to the data, append"""

        # case when both parameters are not given
        if json_str == None and py_dict == None:
            raise exceptions.Signal_Not_Added("No signal content data is supplied!")

        # case when both parameters are supplied
        elif json_str != None and py_dict != None:
            raise exceptions.Signal_Not_Added("Ambiguity when adding to Signal. Both json_str and py_dict are supplied.")

        # case when one of the data is given
        else:
            # if json_str is supplied, convert it to Python dictionary
            if json_str != None and py_dict == None:
                py_dict = json.loads(json_str)

            # add the newly added signal content to the "content" field of the signal data
            # initialize dictionary in the specific index
            self.data[str(self.next_index)] = dict()
            self.data[str(self.next_index)]["content"] = py_dict

            # increment the next index to be inserted
            self.next_index += 1

    # def set_index_content(self, )
       

    def verify_signal(self) -> bool:
        return Signal.static_verify_signal(self.data)


    @staticmethod
    def static_verify_signal(signal_data: dict) -> bool:
        # TODO: verify weather all indices exists in the bound use signal_val.py #verify self.data
        return True

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def get_quantifiable_keys(self) -> list[str]:
        # wrapper for get_quantifiable_keys for current object
        return Signal.static_get_quantifiable_keys(self.data)


    @staticmethod
    def static_get_quantifiable_keys(signal_data: dict) -> list[str]:
        """return all the common keys throughout all signal contents that can be quantifiable"""
        if len(signal_data) == 0:
            # return empty list if self.data is empty
            return list()
        
        elif len(signal_data) > 1:
            # assume signal index start with 0
            # note that set() extract a set of dictionary keys
            signal_content_common_key_set = set(signal_data["0"]["content"])

            for signal_index in signal_data.keys():
                signal_content_common_key_set = signal_content_common_key_set.intersection(set(signal_data[signal_index]["content"]))

            return list(signal_content_common_key_set)

        else:
            # when there is only 1 element in the signal_data, return its keys
            return signal_data["0"]["content"].keys()
