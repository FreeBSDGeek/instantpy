import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="instantpy",
    version="0.0.1",
    author="Kirk Davis",
    author_email="kirk.github@bohica.net",
    description="A Python wrapper for Aruba Instant REST API",
    long_description="Aruba Instant API by Michael Wood (mww012@gmail.com) backported to Python2 by Kirk Davis (kirk.github@bohica.net)",
    long_description_content_type="text/markdown",
    url="https://github.com/FreeBSDGeek/instantpy.git",
    packages=setuptools.find_packages(exclude=['.vscode/']),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7'
)
