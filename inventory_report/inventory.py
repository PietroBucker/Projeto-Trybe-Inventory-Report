from inventory_report.product import Product


class Inventory:
    def __init__(self, data: list[Product] | None = None) -> None:
        self._data = data or []

    def add_data(self, data: list[Product]) -> None:
        self._data += data

    @property
    def data(self) -> list[Product]:
        return self._data.copy()
