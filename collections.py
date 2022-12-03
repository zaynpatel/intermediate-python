# import all collection methods from pkge
from collections import *

# list of overstock
overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]

# create deque
split_prices = deque()

for item in overstock_items: 
  if item[1] > 20.00:
    split_prices.appendleft(item)
  else: 
    split_prices.append(item)

#print(split_prices)  

ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

bundles = []

while len(split_prices) >= 5:
  bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(), split_prices.popleft(), split_prices.popleft()]

  calculate_price = sum(b[1] for b in bundle_list)
  bundles.append(ClothesBundle(bundle_list, calculate_price))

print(bundles)

promoted_bundles = []

for every_bundle in bundles:
  if every_bundle[1] >= 100:
    promoted_bundles.append(every_bundle)

print(list(promoted_bundles))
