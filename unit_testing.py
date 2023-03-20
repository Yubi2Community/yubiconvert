"""Module to define test cases
"""
import unittest

from indian_word2number import indian_w2n as w2n


class TestW2N(unittest.TestCase):
    """Class defination to test positive and negative cases"""

    def test_positives(self):
        """Function to test positive cases"""
        self.assertEqual(
            w2n.word_to_num("one lakh thirty two thousand five hundred forty two"),
            str(132542),
        )
        self.assertEqual(w2n.word_to_num("one lakh"), str(100000))
        self.assertEqual(w2n.word_to_num("nineteen"), str(19))
        self.assertEqual(w2n.word_to_num("two thousand and nineteen"), str(2019))
        self.assertEqual(
            w2n.word_to_num("Twenty Lakh Three Thousand Nineteen"), str(2003019)
        )
        self.assertEqual(
            w2n.word_to_num(
                " twenty lakh three thousand nineteen Rupees and zero paisa only"
            ),
            str(2003019) + " only",
        )
        self.assertEqual(w2n.word_to_num("three crore"), str(30000000))
        self.assertEqual(w2n.word_to_num("three lac"), str(300000))
        self.assertEqual(
            w2n.word_to_num(
                "Twelve Crore Thirty Four Lakh Fifty Six Thousand Seven Hundred Eighty Nine"
            ),
            str(123456789),
        )
        self.assertEqual(w2n.word_to_num("eleven"), str(11))
        self.assertEqual(w2n.word_to_num("Nineteen Crore"), str(190000000))
        self.assertEqual(w2n.word_to_num("one hundred and forty two"), str(142))
        self.assertEqual(w2n.word_to_num("112"), str(112))
        self.assertEqual(w2n.word_to_num("11211234"), str(11211234))
        self.assertEqual(w2n.word_to_num("five"), str(5))
        self.assertEqual(
            w2n.word_to_num("Twenty Lakh Twenty Three Thousand Forty Nine"),
            str(2023049),
        )
        self.assertEqual(w2n.word_to_num("two point three"), str(2.3))
        self.assertEqual(
            w2n.word_to_num("Twenty Lakh Twenty Three Thousand Forty Nine Point Two"),
            str(2023049.2),
        )
        self.assertEqual(w2n.word_to_num("point one"), str(0.1))
        self.assertEqual(w2n.word_to_num("one hundred thirty-five"), str(135))
        self.assertEqual(w2n.word_to_num("hundred"), str(100))
        self.assertEqual(w2n.word_to_num("thousand"), str(1000))
        self.assertEqual(w2n.word_to_num("lakh"), str(100000))
        self.assertEqual(w2n.word_to_num("crore"), str(10000000))
        self.assertEqual(w2n.word_to_num("nine point nine nine nine"), str(9.999))
        self.assertEqual(w2n.word_to_num("one lakh crore"), str(1000000000000))
        self.assertEqual(
            w2n.word_to_num(
                "there was a group of ten friends who went to the restaurant for a party, ordered thirty two dishes including ten drinks and bill came out as ten thousand five hundred and thirty paisa"
            ),
            "there was a group of 10 friends who went to the restaurant for a party, ordered 32 dishes including 10 drinks and bill came out as 10500.3",
        )

    def test_negatives(self):
        """Function to test negative cases"""
        self.assertRaises(ValueError, w2n.word_to_num, "-")
        self.assertRaises(ValueError, w2n.word_to_num, 112)


if __name__ == "__main__":
    unittest.main()
