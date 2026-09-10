# Process Unrelated File Exporter Objects using Duck Typing

class CSVExporter:
    def __init__(self, file_name):
        self.file_name = file_name

    def export(self):
        # Write your code here
        return f"CSV Export: {self.file_name}.csv"


class JSONExporter:
    def __init__(self, file_name):
        self.file_name = file_name

    def export(self):
        # Write your code here
        return f"JSON Export: {self.file_name}.json"


class PDFExporter:
    def __init__(self, file_name):
        self.file_name = file_name

    def export(self):
        # Write your code here
        return f"PDF Export: {self.file_name}.pdf"


def run_exporters(exporters):
    # Process every exporter using one loop
    for exporter in exporters:
        print(exporter.export())


file_name = input()

# Create exporter objects, store them in one list and run them
exporter = [
    CSVExporter(file_name),
    JSONExporter(file_name),
    PDFExporter(file_name)
]

run_exporters(exporter)