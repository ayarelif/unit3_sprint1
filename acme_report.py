from pdb import set_trace as breakpoint
from random import randint, sample
import unittest
from acme import Product
import random, math

"""
- `generate_products()` should generate a given number of products (default
  30), randomly, and return them as a list
- `inventory_report()` takes a list of products, and prints a "nice" summary
"""

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_product():
    products=[]
    for number in range(my_number=30):
        adj = sample(ADJECTIVES,1)[0]
        noun1 = sample(NOUNS,1)[0]
    # name` should be e.g. `'Awesome Anvil
        name = adj +" "+ noun1
    #price` and `weight` should both be from 5 to 100 (inclusive and independent,
    #and remember - they're integers!)
        price = randint(5,100)
        weight=randint(5, 100)
    #`flammability` should be from 0.0 to 2.5 (floats)
        flammability= uniform(0.0 ,2.5)
        prod2=Product(name, price, weight, flammability)
        products.append(prod2)
    return products

def inventory_report(product):
    name_unique=[]
    price_average=[]
    weight_average=[]
    flammability_avg=[]
    for products in product:
        name_unique.append(products.name)
        price_average.append(products.price)
        weight_average.append(products.weight)
        flammability_avg.append(products.flammability)
    unique_name=len(name_unique)
    mean_price=sum(price_average)/len(price_average)
    mean_weight=sum(weight_average)/len(weight_average)
    mean_flammab=sum(flammability_avg)/len(flammability_avg)

if __name__ == '__main__':
    inventory_report(generate_products())
    print(f"ACME INVENTORY REPORT Unique Products = {uniques_name} ")
    print(f"Average Price = {mean_price} ")
    print(f"Average Price = {mean_price} ")
    print(f"Average Weight = {mean_weight} ")
    print(f"Average Flammability = {mean_flammab} ")