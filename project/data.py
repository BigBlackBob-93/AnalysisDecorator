import pandas
import numpy as np
from config import excel


class Data:
    def __init__(self):
        self.data = {}
        data = pandas.read_excel(excel.get('file'), sheet_name=excel.get(1))
        for row in data.itertuples(index=False, name=None):
            self.data[row[0]] = [row[1], row[2]]

    @staticmethod
    def get_groups(column: str) -> list[str]:
        data = pandas.read_excel(excel.get('file'), sheet_name=excel.get(2))
        researches = []

        if list(data.columns.ravel()).count(column) != 0:
            for research in data[column].tolist():
                if research is np.nan:
                    pass
                else:
                    researches.append(research)

        return researches
