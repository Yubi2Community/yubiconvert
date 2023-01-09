import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))


setup(
    name="indian_word2number",
    packages=["indian_word2number"],  # this must be the same as the name above
    version="1.2",
    license="MIT",
    description="Convert number words eg. three hundred and forty two to numbers (342) for indian currency standards.",
    author="Darshan Patel",
    author_email="darshan.patel@go-yubi.com",
    url="https://github.com/credavenue/ca-ds-nlp-Indian-word2number",  # use the URL to the github repo
    keywords=[
        "numbers",
        "convert",
        "words",
        "indian",
        "currency",
    ],  # arbitrary keywords
    classifiers=["Intended Audience :: Developers", "Programming Language :: Python"],
    long_description=open_file("README.rst").read(),
    install_requires=[
        "nltk",
    ],
)
