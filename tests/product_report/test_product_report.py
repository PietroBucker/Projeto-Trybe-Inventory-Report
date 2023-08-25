from inventory_report.product import Product


expect = (
    "The product 1 - FIFA with serial number 123456 manufactured on "
    "01/01/2020 by the company EA valid until 01/01/2021 must be "
    "stored according to the following instructions: jogo para familia."
)


def test_product_report() -> None:
    produto = Product(
        "1",
        "FIFA",
        "EA",
        "01/01/2020",
        "01/01/2021",
        "123456",
        "jogo para familia",
    )
    assert produto.__str__() == expect
