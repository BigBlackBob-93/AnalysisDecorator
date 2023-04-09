from PyQt6.QtWidgets import QApplication
import sys
from analysis import (
    ClinicalBloodTest,
    RedBloodIndicators,
    WhiteBloodIndicators,
    Leukocytes,
    ESR,
    PathologicalBloodCells
)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # vendor_code_2 = ClinicalBloodTest(name='Eric Aidan Diaz')
    # ESR(WhiteBloodIndicators(Leukocytes(RedBloodIndicators(vendor_code_2)))).create_form().show()
    #
    # vendor_code_3 = ClinicalBloodTest(name='Aidan William Garcia')
    # ESR(PathologicalBloodCells(WhiteBloodIndicators(Leukocytes(RedBloodIndicators(vendor_code_3))))).create_form().show()
    #
    # vendor_code_5 = ClinicalBloodTest(name='Joseph Sebastian Phillips')
    # WhiteBloodIndicators(Leukocytes(vendor_code_5)).create_form().show()
    #
    # vendor_code_6 = ClinicalBloodTest(name='Daniel Kevin Rogers')
    # PathologicalBloodCells(WhiteBloodIndicators(Leukocytes(vendor_code_6))).create_form().show()

    sys.exit(app.exec())
