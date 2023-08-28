from inventory_report.inventory import Inventory
from inventory_report.product import Product
from inventory_report.reports.report import Report
from datetime import datetime, date


class SimpleReport(Report):
    def __init__(self) -> None:
        self.stock: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.stock.append(inventory)
        return

    def generate(self) -> str:
        self.invent: dict[str, int] = dict()
        for stock in self.stock:
            if stock.data:
                oldest_date = SimpleReport.old_manufacturing(stock.data)
                closest_date = SimpleReport.close_expiration(stock.data)

                for el in stock.data:
                    if el.company_name not in self.invent:
                        self.invent[el.company_name] = 1
                        # self.invent[el.company_name].add(id(el.expiration_date))
                    else:
                        self.invent[el.company_name] += 1
                        # self.invent[el.company_name].add(id(el.expiration_date))
        return (
            f"Oldest manufacturing date: {oldest_date}\n"
            f"Closest expiration date: {closest_date}\n"
            "Company with the largest inventory: "
            f"{max(self.invent, key=lambda chave: self.invent[chave])}\n"
        )

    @staticmethod
    def old_manufacturing(data: list[Product]) -> date:
        return min(
            [
                datetime.strptime(
                    data_str.manufacturing_date, "%Y-%m-%d"
                ).date()
                for data_str in data
            ]
        )

    @staticmethod
    def close_expiration(data: list[Product]) -> date:
        now_date = datetime.now().date()
        return min(
            [
                datetime.strptime(data_str.expiration_date, "%Y-%m-%d").date()
                for data_str in data
                if datetime.strptime(
                    data_str.expiration_date, "%Y-%m-%d"
                ).date()
                > now_date
            ]
        )


# produto = Product(
#     id="1",
#     product_name="Nicotine Polacrilex",
#     company_name="a",
#     manufacturing_date="2020-02-18",
#     expiration_date="2023-10-28",
#     serial_number="CR25 1551 4467 2549 4402 1",
#     storage_instructions="instrucao 1",
# )

# produto2 = Product(
#     id="1",
#     product_name="Polacrilex",
#     company_name="b",
#     manufacturing_date="2020-02-18",
#     expiration_date="2023-10-27",
#     serial_number="CR25 1551 4467 2549 4402 1",
#     storage_instructions="instrucao 1",
# )

# produto3 = Product(
#     id="1",
#     product_name="Nicotine Polacrilex",
#     company_name="b",
#     manufacturing_date="2020-02-18",
#     expiration_date="2023-10-26",
#     serial_number="CR25 1551 4467 2549 4402 1",
#     storage_instructions="instrucao 1",
# )

# produto4 = Product(
#     id="1",
#     product_name="Nicotine Polacrilex",
#     company_name="d",
#     manufacturing_date="2020-02-18",
#     expiration_date="2023-10-29",
#     serial_number="CR25 1551 4467 2549 4402 1",
#     storage_instructions="instrucao 1",
# )
# # inventory4 = Inventory()
# inventory = Inventory([produto])
# inventory2 = Inventory([produto3])
# inventory3 = Inventory([produto4])
# inventory.add_data([produto2])
# teste = SimpleReport()
# teste.add_inventory(inventory)
# teste.add_inventory(inventory2)
# teste.add_inventory(inventory3)
# # teste.add_inventory(inventory4)
# print(teste.generate())
