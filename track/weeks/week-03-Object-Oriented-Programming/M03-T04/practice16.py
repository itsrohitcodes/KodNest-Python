# Run a Compatible Reporter That does not inherit ReportGenerator

from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self):
        pass


class StudentReport(ReportGenerator):
    def generate_report(self):
        return "Generating Student Report"


class PlacementReport(ReportGenerator):
    def generate_report(self):
        return "Generating Placement Report"


class SimpleTextReporter:
    # Add constructor and generate_report()
    def __init__(self, title):
        self.title = title

    def generate_report(self):
        return f"Generating Text Report: {self.title}"


def run_reports(reports):
    # Call generate_report() for every object
    for report in reports:
        print(report.generate_report())


title = input()

# Create all three reporter objects and run them
reports = [
    StudentReport(),
    PlacementReport(),
    SimpleTextReporter(title)
]

run_reports(reports)