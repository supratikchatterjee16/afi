# Automatic File Identifier

A simple program written to identify by hook(extensions) or by crook(signatures). Failing to either, implies that the file might be a text file with no signature or extension.

## Using

There is a signature downloader, which is tailored to download and store information found on [File Signatures](https://filesignatures.net/). This creates a python file named signatures.py, which needs to be in the same folder as the program.
The program imports this and makes use of it.

The main program lies in the identifier.py file.

