# Build Different Report Generator Classes

from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self):
        pass

class StudentReport(ReportGenerator):
    def generate_report(self):
        # Write your code here
        return "Generating Student Report"

class PlacementReport(ReportGenerator):
    def generate_report(self):
        # Write your code here
        return "Generating Placement Report"

class AttendanceReport(ReportGenerator):
    def generate_report(self):
        # Write your code here
        return "Generating Attendance Report"

def create_report(report_type):
    if report_type == 'STUDENT':
        return StudentReport()
    if report_type == 'PLACEMENT':
        return PlacementReport()
    return AttendanceReport()

n = int(input())
reports = []

for _ in range(n):
    report_type = input().strip()
    reports.append(create_report(report_type))

for report in reports:
    print(report.generate_report())