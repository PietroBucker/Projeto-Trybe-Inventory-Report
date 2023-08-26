from inventory_report.inventory import Inventory
from inventory_report.product import Product
from inventory_report.reports.report import Report
from datetime import datetime, date


class SimpleReport(Report):
    stock: list[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.stock.append(inventory)
        return

    def generate(self) -> str:
        larges_inv: dict[str, int] = dict()
        for stock in self.stock:
            if stock.data:
                oldest_date = SimpleReport.old_manufacturing(stock.data)
                closest_date = SimpleReport.close_expiration(stock.data)
                for el in stock.data:
                    if el.company_name not in larges_inv:
                        larges_inv[el.company_name] = 1
                    else:
                        larges_inv[el.company_name] += 1
        return (
            f"Oldest manufacturing date: {oldest_date} "
            f"Closest expiration date: {closest_date} "
            "Company with the largest inventory: "
            f"{max(larges_inv, key=lambda chave: larges_inv[chave])}"
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


produto = Product(
    id="1",
    product_name="Nicotine Polacrilex",
    company_name="Target Corporation",
    manufacturing_date="2020-02-18",
    expiration_date="2023-09-26",
    serial_number="CR25 1551 4467 2549 4402 1",
    storage_instructions="instrucao 1",
)

produto2 = Product(
    id="1",
    product_name="Nicotine Polacrilex",
    company_name="Corporation",
    manufacturing_date="2022-01-18",
    expiration_date="2023-09-17",
    serial_number="CR25 1551 4467 2549 4402 1",
    storage_instructions="instrucao 1",
)

produto3 = Product(
    id="1",
    product_name="Nicotine Polacrilex",
    company_name="Target",
    manufacturing_date="2021-02-18",
    expiration_date="2023-08-27",
    serial_number="CR25 1551 4467 2549 4402 1",
    storage_instructions="instrucao 1",
)

produto4 = Product(
    id="1",
    product_name="Nicotine Polacrilex",
    company_name="Corporation",
    manufacturing_date="2019-02-18",
    expiration_date="2023-08-26",
    serial_number="CR25 1551 4467 2549 4402 1",
    storage_instructions="instrucao 1",
)
inventory4 = Inventory()
inventory = Inventory([produto])
inventory2 = Inventory([produto3])
inventory3 = Inventory([produto4])
inventory.add_data([produto2])
teste = SimpleReport()
teste.add_inventory(inventory)
teste.add_inventory(inventory2)
teste.add_inventory(inventory3)
teste.add_inventory(inventory4)
print(teste.generate())
