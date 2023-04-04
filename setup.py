import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    "function to open file"
    return open(os.path.join(os.path.dirname(__file__), fname))


setup(
    name="yubiconvert",
    packages=["yubiconvert"],  # this must be the same as the name above
    version="1.0",
    license="MIT",
    description="Python module that can convert numeric words to their numerical form effortlessly",
    author="Yubi Data Science Team",
    author_email="data@go-yubi.com",
    url="https://github.com/Yubi2Community/yubiconvert",
    keywords=[
        "numbers",
        "convert",
        "words",
        "indian",
        "currency",
    ],  # arbitrary keywords
    classifiers=["Intended Audience :: Developers", "Programming Language :: Python"],
    long_description=open_file("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "nltk",
    ],
)
