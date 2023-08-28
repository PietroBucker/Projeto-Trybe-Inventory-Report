from typing import List

from inventory_report.importers import CsvImporter, JsonImporter
from inventory_report.inventory import Inventory
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


def process_report_request(file_paths: List[str], report_type: str) -> str:
    if report_type == "simple" or report_type == "complete":
        inventory = Inventory()
        report = (
            SimpleReport() if report_type == "simple" else CompleteReport()
        )
        for path in file_paths:
            if path.endswith(".csv"):
                data = CsvImporter(path).import_data()
                inventory.add_data(data)
                report.add_inventory(inventory)
                # return report.generate()
                break

            elif path.endswith(".json"):
                data = JsonImporter(path).import_data()
                inventory.add_data(data)
                report.add_inventory(inventory)
                # return report.generate()
                break

        return report.generate()
    else:
        raise ValueError("Report type is invalid.")
