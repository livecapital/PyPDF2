#!/usr/bin/env python

from distutils.core import setup
import PyPDF2

long_description = """
A Pure-Python library built as a PDF toolkit.  It is capable of:

- extracting document information (title, author, ...),
- splitting documents page by page,
- merging documents page by page,
- cropping pages,
- merging multiple pages into a single page,
- encrypting and decrypting PDF files.

By being Pure-Python, it should run on any Python platform without any
dependencies on external libraries.  It can also work entirely on StringIO
objects rather than file streams, allowing for PDF manipulation in memory.
It is therefore a useful tool for websites that manage or manipulate PDFs.
"""

setup(
        name="PyPDF2",
        version=PyPDF2.__version__,
        description="PDF toolkit",
        long_description=long_description,
        author="Phaseit, Inc.",
        author_email="PyPDF2@phaseit.net",
        url="http://github.com/mstamy2/PyPDF2/tarball/master",
        download_url="http://github.com/mstamy2/PyPDF2/tarball/master",
        classifiers = [
                "Development Status :: 5 - Production/Stable",
                "Intended Audience :: Developers",
                "License :: OSI Approved :: BSD License",
                "Programming Language :: Python :: 2",
                "Programming Language :: Python :: 3",
                "Operating System :: OS Independent",
                "Topic :: Software Development :: Libraries :: Python Modules",
            ],
        packages=["PyPDF2"],
    )
