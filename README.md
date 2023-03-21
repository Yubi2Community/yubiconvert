# YubiConvert

YubiConvert - a Python module that can convert numeric words to their numerical form effortlessly. What's more, it supports both Western and Indian currency standards, making it the ultimate solution for all your numerical conversion needs.

## Installation

To install the YubiConvert module, it is recommended to first ensure that you have updated the pip to the latest version. Then, you can use pip to install the module from the Python Package Index with the following command:

```python
pip install yubiconvert

```

## Usage

Once the module is installed, you can import it into your Python code using the following line:

```python
from yubiconvert import yubiconvert as w2n
```

Then you can use the **word_to_num** method to convert a number-word to numeric digits, as shown below.
```python
print(w2n.word_to_num("twenty lakh three thousand nineteen Rupees"))
2003019
```
```python
print(w2n.word_to_num('two point three')) 
2.3
```
```python
print(w2n.word_to_num('112')) 
112
```
```python
print(w2n.word_to_num('point one')) 
0.1
```
```python
print(w2n.word_to_num('one hundred thirty-five')) 
135
```
```python
print(w2n.word_to_num("there was a group of ten friends who went to the restaurant for a party, ordered thirty two dishes including ten drinks and bill came out as ten thousand five hundred and thirty paisa")) 
there was a group of 10 friends who went to the restaurant for a party, ordered 32 dishes including 10 drinks and bill came out as 10500.3
```
## Credits
This repo is a forked of [w2n](https://github.com/akshaynagpal/w2n) library and the same has been used as a base to extend it further to support indian currency standards.