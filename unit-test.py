import surfshop
import unittest

class TestClass(unittest.TestCase):
  # note
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  def test_add_surfboard(self):
    message = self.cart.add_surfboards(quantity=1)
    self.assertEqual(message, f'Successfully added 1 surfboard to cart!')
  
  """
  def test_add_surfboards(self):
    message_two = self.cart.add_surfboards(quantity=2)
    self.assertEqual(message_two, f'Successfully added 2 surfboards to cart')
  """

  def test_add_surfboard(self):
    for i in range(2,5):
      with self.subTest(i=i):
        message = self.cart.add_surfboards(i)
        self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
        self.cart = surfshop.ShoppingCart()
    
  @unittest.skip
  def test_add_too_many_surfboards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards(), 5)

  def __str__(self):
    return 'Cart cannot have more than 4 surfboards in it!'

  #@unittest.expectedFailure
  #def test_apply_locals_discount(self):
      #self.cart.apply_locals_discount()
      #self.assertTrue(self.cart.locals_discount)

unittest.main()
