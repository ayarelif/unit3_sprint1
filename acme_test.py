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
- Code review is important beucase of its desing. 
Overal desing is the post important part of data rewieing. 
Thus, this covers the correction od code, test contant, 
functionality changes and so on
-There are many users to work on the same projects or,
to make the changes on the same project.Thus, ducker provides
containers whcih are the platform as a service. it uses OS level visulization
to get the software in the containers. Each contains have its own sowfare, libraries,
and files. It is independent and single package.
"""
