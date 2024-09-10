class BadReportGenerator:
    def generate_pdf(self):
        pass

    def generate_csv(self):
        pass

#---

from abc import ABC, abstractmethod

class PDFReportGenerator(ABC):
    @abstractmethod
    def generate_pdf(self):
        pass

class CSVReportGenerator(ABC):
    @abstractmethod
    def generate_csv(self):
        pass

class TransactionCSVReport(CSVReportGenerator):
    def generate_csv(self):
        print("Generating CSV report for transactions")

csv_report = TransactionCSVReport()
csv_report.generate_csv()
