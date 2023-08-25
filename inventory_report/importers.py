import json
import csv
from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        product_list = []
        with open(self.path, "r") as file:
            content = file.read()
            for product in json.loads(content):
                product_list.append(
                    Product(
                        id=product["id"],
                        product_name=product["product_name"],
                        company_name=product["company_name"],
                        manufacturing_date=product["manufacturing_date"],
                        expiration_date=product["expiration_date"],
                        serial_number=product["serial_number"],
                        storage_instructions=product["storage_instructions"],
                    )
                )
        return product_list


# teste = JsonImporter("inventory_report/data/inventory.json")
# print(teste.import_data())


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        new_dict = dict()
        product_list = []
        with open(self.path, "r") as file:
            content = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = content
            for produto in data:
                new_dict = {header[i]: produto[i] for i in range(len(header))}

                product_list.append(
                    Product(
                        id=new_dict["id"],
                        product_name=new_dict["product_name"],
                        company_name=new_dict["company_name"],
                        manufacturing_date=new_dict["manufacturing_date"],
                        expiration_date=new_dict["expiration_date"],
                        serial_number=new_dict["serial_number"],
                        storage_instructions=new_dict["storage_instructions"],
                    )
                )
        return product_list


teste = CsvImporter("inventory_report/data/inventory.csv")
print(teste.import_data())


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
