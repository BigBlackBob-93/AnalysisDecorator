import pandas
import numpy as np
from config import excel


class Data:
    """Class for getting data from .xlsx.

    Methods: get_groups(column: str) -> list[str] | get_data() -> dict
    """

    @staticmethod
    def get_groups(column: str) -> list[str]:
        """Get one group of researches from .xlsx file

        Default file parameters contains in config.py.

        Arguments:
        column:str -- column number in the table used to retrieve the data
        """
        data = pandas.read_excel(excel.get('file'), sheet_name=excel.get(2))
        researches = []

        if list(data.columns.ravel()).count(column) != 0:
            for research in data[column].tolist():
                if research is np.nan:
                    pass
                else:
                    researches.append(research)
        return researches

    @staticmethod
    def get_data() -> dict:
        """Get all researches (with reference values) from .xlsx file

        Default file parameters contains in config.py.
        """
        data = {}
        data_p = pandas.read_excel(excel.get('file'), sheet_name=excel.get(1))
        for row in data_p.itertuples(index=False, name=None):
            data[row[0]] = [row[1], row[2]]
        return data
