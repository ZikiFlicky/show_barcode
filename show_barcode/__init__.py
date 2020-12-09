from .api import create_barimg


def show_barcode(
        bar: str, 
        bar_type: str = None) -> None:
    """
    create barcode and show it on screen
    given parameters:
    bar[str] = the barcode you want to be displayed (the number).
    bar_type[str] = the barcode type you want to be displayed, like ean13
    """
    img = create_barimg(bar, bar_type)
    img.show()

