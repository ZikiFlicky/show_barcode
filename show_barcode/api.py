import barcode
from barcode import BarcodeNotFoundError


DEFAULT_BAR: str = "ean13"
barcode_digits: dict = {
    "ean13": 13
}


def create_barimg(bar: str, bar_type: str = None):
    """
    create a PIL object with the given barcode
    given parameters:
    bar[str] = the barcode you want to be displayed (the number).
    bar_type[str] = the barcode type you want to be displayed, like ean13
    """
    bar_type = bar_type or DEFAULT_BAR
    bar_type = bar_type.lower()
    # check if the barcode type is in available barcodes, raise error if not
    if bar_type not in barcode_digits:
        raise BarcodeNotFoundError(
            "unsupported barcode type '{}'".format(bar_type)
        )
    # store length of barcode
    barcode_length: int = barcode_digits[bar_type]
    assert len(bar) == barcode_length
    # creates a barcode
    ean = barcode.get(bar_type, bar, barcode.writer.ImageWriter())
    assert ean.get_fullcode() == bar
    # renders the image as a PIL object
    img = ean.render()
    # shows the PIL object on screen
    return img
