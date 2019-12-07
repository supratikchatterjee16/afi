# Automatic File Identifier

A simple program written to identify by hook(extensions) or by crook(signatures). Failing to either, implies that the file might be a text file with no signature or extension.

## Using

There is a signature downloader, which is tailored to download and store information found on [File Signatures](https://filesignatures.net/). This creates a python file named signatures.py, which needs to be in the same folder as the program.
The program imports this and makes use of it.

```python
import afi
list_mime_tuples = afi.identify(<filepath or folderpath>)
# The above gives you a list of tuples which contain the mimes for each identified file
# It identifies using both extension and signatures
```

## Author

Supratik Chatterjee

## Issues

There are some file popular extensions and signatures missing. 
Should one find it, kindly let me know.

## Downloading

```bash
mkdir afi
cd ./afi
git init
git remote add origin https://github.com/supratikchatterjee16/afi.git
git pull origin master
pip install .
```
