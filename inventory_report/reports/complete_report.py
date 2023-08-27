from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        final_string = super().generate()
        print(self.invent)
        final_string += "Stocked products by company:\n "
        final_string += "".join(
            [f"- {a}: {len(b)}\n" for a, b in self.invent.items()]
        )
        return final_string


# teste2 = CompleteReport()

# print(teste2.generate())

# produto = Product(
#     id="1",
#     product_name="Nicotine Polacrilex",
#     company_name="Target Corporation",
#     manufacturing_date="2020-02-18",
#     expiration_date="2023-09-26",
#     serial_number="CR25 1551 4467 2549 4402 1",
#     storage_instructions="instrucao 1",
# )

# produto2 = Product(
#     id="1",
#     product_name="Nicotine Polacrilex",
#     company_name="Corporation",
#     manufacturing_date="2022-01-18",
#     expiration_date="2023-09-17",
#     serial_number="CR25 1551 4467 2549 4402 1",
#     storage_instructions="instrucao 1",
# )

# produto3 = Product(
#     id="1",
#     product_name="Nicotine Polacrilex",
#     company_name="Target",
#     manufacturing_date="2021-02-18",
#     expiration_date="2023-08-27",
#     serial_number="CR25 1551 4467 2549 4402 1",
#     storage_instructions="instrucao 1",
# )

# produto4 = Product(
#     id="1",
#     product_name="Nicotine Polacrilex",
#     company_name="Corporation",
#     manufacturing_date="2019-02-18",
#     expiration_date="2023-08-26",
#     serial_number="CR25 1551 4467 2549 4402 1",
#     storage_instructions="instrucao 1",
# )
# inventory4 = Inventory()
# inventory = Inventory([produto])
# inventory2 = Inventory([produto3])
# inventory3 = Inventory([produto4])
# inventory.add_data([produto2])
# teste = SimpleReport()
# teste.add_inventory(inventory)
# teste.add_inventory(inventory2)
# teste.add_inventory(inventory3)
# teste.add_inventory(inventory4)
# teste2 = CompleteReport()
# teste2.add_inventory(inventory2)

# print(teste2.generate())
