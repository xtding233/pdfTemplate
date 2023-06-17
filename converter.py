import pandas as pd
from configparser import ConfigParser
from typing import List, Dict
from header import Header, TEMPLATE_HEADER

ESSENTIAL_FIELDS = {Header.priority :  999, Header.text : None}

_NUMERIC_TYPE_ = [Header.x1, Header.y1, Header.x2, Header.y2, Header.size,
                  Header.bold, Header.italic, Header.foreground, Header.priority, Header.multiline, Header.rotation]

class Converter:
    @staticmethod
    def from_csv(path_csv: str, delimiter = ",", first_line_as_header = False):
        # load dataframe
        if not first_line_as_header:
            df = pd.read_csv(path_csv, delimiter=delimiter, header=None)
            df.columns = TEMPLATE_HEADER
        else:
            df = pd.read_csv(path_csv, delimiter=delimiter)
        elements = []
        for i in range(0, len(df.index)):
            # loop on each row
            elements += [{}]
            for j in range(0, len(df.columns)):
                if not pd.isna(df.iloc[i, j]):
                    elements[i].update({df.columns[j] : df.iloc[i, j]})
        return Converter.validate_elements(elements)

    @staticmethod
    def from_ini(path_ini : str):
        config = ConfigParser()
        config.read(path_ini)
        elements = []
        for name in config.sections():
            e = {}
            e.update({Header.name : name})
            for k in list(config[Header.name].keys()):
                e.update({k : config[Header.name][k]})
            elements += [e]
        return Converter.validate_elements(elements)

    @staticmethod
    def validate_elements(elements : List[Dict[object, object]]):
        elements_ = elements.copy()
        for i in range(0, len(elements_)):
            for key in ESSENTIAL_FIELDS.keys(): # update with essential values
                if key not in elements_[i].keys():
                    elements_[i].update({key : ESSENTIAL_FIELDS[key]})
            for e in _NUMERIC_TYPE_: # elements
                if e in elements_[i].keys():
                    elements_[i].update({e : float(elements_[i][e])})
        return elements_

