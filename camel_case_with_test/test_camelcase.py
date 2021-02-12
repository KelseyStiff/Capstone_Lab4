import unittest
import camel_case
from unittest import TestCase

class TestCamelCase(TestCase): 


    def test_spaces(self):
        #one space
        self.assertEqual('helloWorld', camel_case.camel_case('Hello World'))

        #multiple spaces in front of words
        self.assertEqual('helloWorld', camel_case.camel_case('     Hello      World'))

        #multiple spaces after words
        self.assertEqual('helloWorld', camel_case.camel_case('Hello      World    '))

        #mutliple space in front of multiple words
        self.assertEqual('helloWorldHowAreYou', camel_case.camel_case('     Hello      World   how   are   you'))

        #multiple space after multiple words
        self.assertEqual('helloWorldHowAreYou', camel_case.camel_case('Hello    World   how   are   you      '))

    
    def test_empty_string(self):
        #empty string should return empty string
        self.assertEqual('', camel_case.camel_case(''))

    def test_one_word(self):
        #one word should return lowercase
        self.assertEqual('hello', camel_case.camel_case('HELLO'))

    def test_remove_special_characters(self):
        self.assertEqual('helloWorld', camel_case.remove_special_characters('@@@@!!!!  @&*  #^@* hello World $& @'))

    def test_uppercase_lowercase_combos(self):
        self.assertEqual('helloWorld', camel_case.camel_case('HeLlO WoRlD'))
        
    def test_newline_or_tab_removed(self):
        #remove new line or tab
        self.assertEqual('helloWorld', camel_case.remove_special_characters('\n hello \n World'))




if __name__ == '__main__':
    unittest.main()


