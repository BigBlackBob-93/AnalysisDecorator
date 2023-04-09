from datetime import datetime
from abc import ABC, abstractmethod
from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QDoubleSpinBox,
    QPushButton
)
from config import LEFT
from object import Object
from data import Data
from report import Report

NOW = datetime.now().strftime("%d-%m-%Y")


class Form(ABC):
    """Base abstract form class, defines behavior.

    Methods: create_form() -> QMainWindow | get_obj() -> Object
    """

    @abstractmethod
    def create_form(self) -> QMainWindow:
        pass

    @abstractmethod
    def get_obj(self) -> Object:
        pass


class Analysis(Form):
    """Abstract class for any analysis form, inherited from class Form(ABC).

    Fields: form: QMainWindow | obj: Object | report: Report.
    Overridden methods: create_form() -> QMainWindow | get_obj() -> Object
    New methods: __init__()
    """

    def __init__(self):
        """Initialize all fields.

         Fields:
         form: QMainWindow -- main analysis form |
         obj: Object -- setting all objects on the analysis form and keeping some for this instance |
         report: Report -- report for this instance.
         """
        self.form: QMainWindow = QMainWindow()
        self.obj: Object = Object()
        self.report: Report = Report(self.obj)

    @abstractmethod
    def create_form(self) -> QMainWindow:
        pass

    @abstractmethod
    def get_obj(self) -> Object:
        return self.obj


class ClinicalBloodTest(Analysis):
    """Concrete class for clinical blood test form, inherited from class Analysis(Form).

    Inherited fields: form: QMainWindow | obj: Object | report: Report.
    New fields: name: str | date: str.
    Overridden methods: create_form() -> QMainWindow | get_obj() -> Object | __init__(self, name: str, date: str = NOW).
    """

    def __init__(self, name: str, date: str = NOW):
        """Overridden function. Initialize all fields and send them to the class Object to save.

        Fields:
        name: str -- patient's name |
        date: str  -- date of blood collection.
        """
        super().__init__()
        self.name: str = name
        self.date: str = date
        self.obj.add_obj(name, key='info')
        self.obj.add_obj(date, key='info')

    def create_form(self) -> QMainWindow:
        """Overridden function. Generate base form objects and return the form."""

        self.obj.set_obj(
            object=self.form,
            title=ClinicalBloodTest.__name__
        )
        self.obj.set_obj(
            object=QLabel(self.form),
            title="Name: " + self.name,
            above=self.obj.indent
        )
        self.obj.set_obj(
            object=QPushButton(self.form),
            title='Create report',
            above=self.obj.indent,
            left=LEFT * 16
        ).clicked.connect(self.report.create_report)

        self.obj.increase_indent()
        self.obj.set_obj(
            object=QLabel(self.form),
            title="Date: " + self.date,
            above=self.obj.indent
        )
        self.obj.increase_indent(2)
        self.obj.set_obj(
            object=QLabel(self.form),
            title="Research",
            above=self.obj.indent,
            left=LEFT * 4
        )
        self.obj.set_obj(
            object=QLabel(self.form),
            title="Result",
            above=self.obj.indent,
            left=LEFT * 16
        )

        return self.form

    def get_obj(self) -> Object:
        return super().get_obj()


class AnalysisDecorator(Form):
    """Abstract class for any analysis decorators, inherited from class Form(ABC).

    Fields: analysis: Form.
    Overridden methods: create_form() -> QMainWindow | get_obj() -> Object.
    New methods: __init__(analysis: Form) | create_researches(column: str, form: QMainWindow) -> None
    """

    def __init__(self, analysis: Form):
        """Initialize all fields.

        Fields:
        analysis: Form -- concrete object in hierarchy (type - base class), for methods redirection.
        """
        self.analysis: Form = analysis

    @abstractmethod
    def create_form(self) -> QMainWindow:
        """Overridden function. Forward this method to the Form."""
        return self.analysis.create_form()

    @abstractmethod
    def get_obj(self) -> Object:
        """Overridden function. Forward this method to the Form."""
        return self.analysis.get_obj()

    def create_researches(self, column: str, form: QMainWindow) -> None:
        """Generate objects (unique researches) and send them to the class Object to save.

        Extra function to avoid duplication, used only by descendants.
        Arguments:
        column: str  -- name of the table column in .xlsx |
        form: QMainWindow -- objects will be created on it.
        """
        form = form
        data = Data()
        # getting the requested group of researches (one concrete decorator - one group of researches)
        researches = data.get_groups(column)

        self.analysis.get_obj().increase_indent()
        for research in researches:
            self.get_obj().increase_indent()
            self.get_obj().add_obj(
                self.get_obj().set_obj(
                    object=QLabel(form),
                    title=research,
                    above=self.get_obj().indent,
                    left=LEFT * 4,
                    case=0
                ),
                key='researches')
            self.get_obj().add_obj(
                self.get_obj().set_obj(
                    object=QDoubleSpinBox(form),
                    above=self.get_obj().indent,
                    left=LEFT * 16
                ),
                key='results')


class RedBloodIndicators(AnalysisDecorator):
    """Concrete decorator class, inherited from class AnalysisDecorator(Form).

    Inherited fields: analysis: Form.
    Overridden methods: __init__(analysis: Form) | create_form() -> QMainWindow | get_obj() -> Object.
    Override all methods with forwarding them to ancestor.
    """

    def __init__(self, analysis: Form):
        super().__init__(analysis)

    def create_form(self) -> QMainWindow:
        form = super().create_form()  # forwarding
        super().create_researches(column=RedBloodIndicators.__name__, form=form)  # adding unique behaviour
        return form

    def get_obj(self) -> Object:
        return super().get_obj()


class WhiteBloodIndicators(AnalysisDecorator):
    """Concrete decorator class, inherited from class AnalysisDecorator(Form).

    Inherited fields: analysis: Form.
    Overridden methods: __init__(analysis: Form) | create_form() -> QMainWindow | get_obj() -> Object.
    Override all methods with forwarding them to ancestor.
    """
    def __init__(self, analysis: Form):
        super().__init__(analysis)

    def create_form(self) -> QMainWindow:
        form = super().create_form()
        super().create_researches(column=WhiteBloodIndicators.__name__, form=form)
        return form

    def get_obj(self) -> Object:
        return super().get_obj()


class Leukocytes(AnalysisDecorator):
    """Concrete decorator class, inherited from class AnalysisDecorator(Form).

    Inherited fields: analysis: Form.
    Overridden methods: __init__(analysis: Form) | create_form() -> QMainWindow | get_obj() -> Object.
    Override all methods with forwarding them to ancestor.
    """
    def __init__(self, analysis: Form):
        super().__init__(analysis)

    def create_form(self) -> QMainWindow:
        form = super().create_form()
        super().create_researches(column=Leukocytes.__name__, form=form)
        return form

    def get_obj(self) -> Object:
        return super().get_obj()


class ESR(AnalysisDecorator):
    """Concrete decorator class, inherited from class AnalysisDecorator(Form).

    Inherited fields: analysis: Form.
    Overridden methods: __init__(analysis: Form) | create_form() -> QMainWindow | get_obj() -> Object.
    Override all methods with forwarding them to ancestor.
    """
    def __init__(self, analysis: Form):
        super().__init__(analysis)

    def create_form(self) -> QMainWindow:
        form = super().create_form()
        super().create_researches(column=ESR.__name__, form=form)
        return form

    def get_obj(self) -> Object:
        return super().get_obj()


class PathologicalBloodCells(AnalysisDecorator):
    """Concrete decorator class, inherited from class AnalysisDecorator(Form).

    Inherited fields: analysis: Form.
    Overridden methods: __init__(analysis: Form) | create_form() -> QMainWindow | get_obj() -> Object.
    Override all methods with forwarding them to ancestor.
    """
    def __init__(self, analysis: Form):
        super().__init__(analysis)

    def create_form(self) -> QMainWindow:
        form = super().create_form()
        super().create_researches(column=PathologicalBloodCells.__name__, form=form)
        return form

    def get_obj(self) -> Object:
        return super().get_obj()
