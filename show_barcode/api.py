import barcode


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
        assert bar_type in barcode_digits
        # store length of barcode
        barcode_length: int = barcode_digits[bar_type]
        len_err: str = f"the length of the barcode is supposed to be {barcode_length}"
        assert len(bar) == barcode_length, len_err
        # creates a barcode
        ean = barcode.get(bar_type, bar, barcode.writer.ImageWriter())
        assert ean.get_fullcode() == bar
        # renders the image as a PIL object
        img = ean.render()
        # shows the PIL object on screen
        return img
