from acme import Product
from acme_report import generate_product, ADJECTIVES, NOUNS
import unittest

class AcmeProductTests(unittest.TestCase):
    """
    Making sure Acme products are the tops!
    """
    def test_default_product_price(self):
       """
       Test default product price being 10.
       """
       prod = Product('Test Product')
       self.assertEqual(prod.price, 10)
    
    def test_default__product_weight(self):
       """
       Test default product weight=20.
       """
       prod = Product('Test Product')
       self.assertEqual(prod.weight, 20)
    
    def test_explode(self):
       """
       Test default product price being 10.
       """
       prod = Product('Test Product')
       self.assertEqual(prod.explode(),"Test Product")

    def text_stealability(self):
       """
       Test for stealability
       """
       prod=Product("Test Product")
       self.assertEqual(prod.stealability(),"Test not working")

class AcmeReportTest(unittest.TestCase):

    def test_default_num_product(self):
       """
       Receive a list of length 30
       """
       prod = generate_product()
       self.assertEqual(len(prod), 30)
    
    def test_legal_names(self):
       """ generated names for a default batch of products are 
       all valid possible names to generate (adjective, space, 
       noun, from the lists of possible words)
       """
       prod = generate_product()
       for word in prod:
           self.assertIn(word.name.split()[0], ADJECTIVES)
           self.assertIn(word.name.split()[1], NOUNS)
    
if __name__ == '__main__':
    unittest.main()


"""
Part7 Questions:
- Code review is important beucase if you missed something as a structural, your peer
coluld catch it. Also, it would help to develop better and cleaner written functions

- container will help us to transport all the written code in a same format, so that any people 
who use different comuters and programs, they can read edit and improve the code.
"""
