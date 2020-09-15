from pdb import set_trace as breakpoint
from random import randint, sample, uniform
from acme import Product
import unittest
"""
- `generate_products()` should generate a given number of products (default
  30), randomly, and return them as a list
- `inventory_report()` takes a list of products, and prints a "nice" summary
"""

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_product(num_product=30):
    products=[]
    for _ in range(num_product):
        adj = sample(ADJECTIVES,1)[0]
        noun1 = sample(NOUNS,1)[0]
    # name` should be e.g. `'Awesome Anvil
        name = adj +" "+ noun1
    #price` and `weight` should both be from 5 to 100 (inclusive and independent,
    #and remember - they're integers!)
        price = randint(5,100)
        weight=randint(5, 100)
    #`flammability` should be from 0.0 to 2.5 (floats)
        flammability= uniform(0.0, 2.5)
        prod2=Product(name, price, weight, flammability)
        products.append(prod2)
    return products

def inventory_report(products):
    name_unique=[]
    price_average=[]
    weight_average=[]
    flammability_avg=[]
    for number in products:
        name_unique.append(number.name)
        price_average.append(number.price)
        weight_average.append(number.weight)
        flammability_avg.append(number.flammability)
    unique_name=len(set(name_unique))
    mean_price=sum(price_average)/len(price_average)
    mean_weight=sum(weight_average)/len(weight_average)
    mean_flammab=sum(flammability_avg)/len(flammability_avg)

    print(f"Unique Products name: {unique_name}")
    print(f"Average Price: {mean_price}")
    print(f"Average Weight: {mean_weight}")
    print(f"Average Flammability: {mean_flammab}")
    return unique_name, mean_price, mean_weight,mean_flammab
if __name__ == '__main__':
    inventory_report(generate_product())
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
