from inventory_report.product import Product


expect = """The product 1 - EA with serial number 123456 manufactured on
01/01/2020 by the company FIFA valid until 01/01/2021 must be stored according
to the following instructions: jogo para familia."""


def test_create_product() -> None:
    produto = Product(
        "1",
        "FIFA",
        "EA",
        "01/01/2020",
        "01/01/2021",
        "123456",
        "jogo para familia",
    )
    assert produto.id == "1"
    assert produto.company_name == "EA"
    assert produto.product_name == "FIFA"
    assert produto.manufacturing_date == "01/01/2020"
    assert produto.expiration_date == "01/01/2021"
    assert produto.serial_number == "123456"
    assert produto.storage_instructions == "jogo para familia"
