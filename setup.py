# made by Yuval Tasher and Alon Segal 2020
from setuptools import setup


# dependencies to download
dependencies: list = ["Pillow", "python-barcode"]

# minimum version
min_ver: str = "3.7"

def main() -> None:
    setup(
        name="show_barcode",
        version="1.0",
        packages=["show_barcode"],
        license="GPL3",
        author="Yuval Tasher, Alon Segal",
        description="a library to show generate barcodes that show up on screen",
        install_requires=dependencies,
        python_requires=f">={min_ver}",
        classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9"
        ]
    )


if __name__ == "__main__":
    main()

