import pandas as pd
from configparser import ConfigParser
from typing import List, Dict
from header import Header, TEMPLATE_HEADER
import codecs

ESSENTIAL_FIELDS = {Header.priority: 999, Header.text: None}

_NUMERIC_TYPE_ = [Header.x1, Header.y1, Header.x2, Header.y2, Header.size,
                  Header.bold, Header.italic, Header.foreground, Header.priority, Header.multiline, Header.rotation]


class Converter:
    @staticmethod
    def from_csv(path_csv: str, delimiter=",", first_line_as_header=False):
        # load dataframe
        if not first_line_as_header:
            df = pd.read_csv(path_csv, delimiter=delimiter, header=None)
            df.columns = TEMPLATE_HEADER
        else:
            df = pd.read_csv(path_csv, delimiter=delimiter)
        elements = Converter._generate_elements_from_csv_df(df)
        return Converter.validate_elements(elements)

    @staticmethod
    def _generate_elements_from_csv_df(df: pd.DataFrame):
        elements = []
        for i in range(0, len(df.index)):
            # loop on each row
            elements += [{}]
            for j in range(0, len(df.columns)):
                if not pd.isna(df.iloc[i, j]):
                    elements[i].update({df.columns[j]: df.iloc[i, j]})
        return elements

    @staticmethod
    def from_ini(path_ini: str):
        config = ConfigParser()
        config.read(path_ini)
        elements = Converter._generate_elements_from_ini_config(config)
        return Converter.validate_elements(elements)

    @staticmethod
    def _generate_elements_from_ini_config(config: ConfigParser):
        elements = []
        for name in config.sections():
            e = {}
            e.update({Header.name: name})
            for k in list(config[name].keys()):
                e.update({k: config[name][k]})
            elements += [e]
        return elements

    @staticmethod
    def read_html(path_html: str):
        f = codecs.open(path_html, 'r')
        return f.read()

    @staticmethod
    def validate_elements(elements: List[Dict[object, object]]):
        elements_ = elements.copy()
        for i in range(0, len(elements_)):
            for e in _NUMERIC_TYPE_:  # elements
                if e in elements_[i].keys():
                    elements_[i].update({e: float(str(elements_[i][e]))})
            for key in ESSENTIAL_FIELDS.keys():  # update with essential values
                if key not in elements_[i].keys():
                    elements_[i].update({key: ESSENTIAL_FIELDS[key]})
        return elements_