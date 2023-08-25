from dataclasses import dataclass


@dataclass
class Product:
    id: str
    product_name: str
    company_name: str
    manufacturing_date: str
    expiration_date: str
    serial_number: str
    storage_instructions: str

    def __str__(self) -> str:
        return (
            f"The product {self.id} - {self.product_name} "
            f"with serial number {self.serial_number} "
            f"manufactured on {self.manufacturing_date} "
            f"by the company {self.company_name} "
            f"valid until {self.expiration_date} "
            "must be stored according to the following instructions: "
            f"{self.storage_instructions}."
        )


# produto = {
#     "id": "1",
#     "product_name": "Nicotine Polacrilex",
#     "company_name": "Target Corporation",
#     "manufacturing_date": "2021-02-18",
#     "expiration_date": "2023-09-17",
#     "serial_number": "CR25 1551 4467 2549 4402 1",
#     "storage_instructions": "instrucao 1",
# }
# print(produto.values())
