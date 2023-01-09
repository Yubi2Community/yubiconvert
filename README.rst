==============
Word to Number
==============
This is a Python module to convert number words (eg. twenty one) to numeric digits (21) modified to support indian currency standards as well as Western stadards.
It can also replace numbers written in between the sentence while keeping rest of the stuff as it is.

++++++++++++
Installation
++++++++++++
Please ensure that you have **updated pip** to the latest version before installing indian_word2number.

You can install the module using Python Package Index using the below command.

.. code-block:: python

  pip install indian-word2number

+++++
Usage
+++++
First you have to import the module using the below code.

.. code-block:: python

    from indian_word2number import indian_w2n as w2n

Then you can use the **word_to_num** method to convert a number-word to numeric digits, as shown below.

.. code-block:: python

    >>> print(w2n.word_to_num("twenty lakh three thousand nineteen Rupees and zero paisa only"))
    2003019

    >>> print(w2n.word_to_num('two point three')) 
    2.3

    >>> print(w2n.word_to_num('112')) 
    112

    >>> print(w2n.word_to_num('point one')) 
    0.1

    >>> print(w2n.word_to_num('one hundred thirty-five')) 
    135

    >>> print(w2n.word_to_num("there was a group of ten friends who went to the restaurant for a party, ordered thirty two dishes including ten drinks and bill came out as ten thousand five hundred and thirty paisa")) 
    there was a group of 10 friends who went to the restaurant for a party, ordered 32 dishes including 10 drinks and bill came out as 10500.3

+++++++++++
Bugs/Errors
+++++++++++

Please ensure that you have updated pip to the latest version before installing word2number.

++++++++++++
Contributors
++++++++++++
- Darshan Patel (`DarshanPatel-Yubi <https://github.com/DarshanPatel-Yubi>`__)

++++++++++++
Credits
++++++++++++
This repo is a forked of `w2n <https://github.com/akshaynagpal/w2n>` library and the same has been used as a base to extend it further to support indian currency standards.