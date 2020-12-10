# The show_barcode library
This is a library me and [Alon]() made for my computer science teacher who asked for a barcode library for our class as a 9th grade finish project.



# installation

### Windows and UNIX( Mac and Linux) installations

To start the installation you need to cd into the download directory where `setup.py` is stored.

For installing you can simply run the shell script `install.sh`.

If that doesnt work you should try calling it through the terminal,  

knowing the path to your python executable. 

`[python executables path] setup.py install`

### Windows specific download

You can also install using the py launcher (`py -0` to see all versions).

You can install using a certain version by entering `py -[version] setup.py install`

# use

* For importing use:
```python 
import show_barcode
```

* For showing image on screen:
```python
show_barcode.show_barcode("1234567891231")
```
