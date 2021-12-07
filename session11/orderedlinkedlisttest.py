import unittest
from orderedlinkedlist import OrderedLinkedList


class OrderedLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.lst1 = OrderedLinkedList([1,2,3,4,5,6,7,9,8])
        self.lst2 = OrderedLinkedList(["Bonsoir", "Bonjour"])

    def test_init(self):
        self.assertEqual(self.lst1.get_as_array(), [1,2,3,4,5,6,7,8,9])
        self.assertEqual(self.lst2.get_as_array(), ["Bonjour", "Bonsoir"])

    def test_add(self):
        self.lst1.add(4.5)
        self.lst1.add(78)
        self.lst1.add(-10)
        self.assertEqual([-10, 1,2,3,4,4.5,5,6,7,8,9,78], self.lst1.get_as_array())

    def test_remove(self):
        self.assertFalse(self.lst1.remove(7899))
        self.lst1.remove(10)
        self.lst1.remove(-10)
        self.lst1.remove(78)
        self.lst1.remove(4.5)
        self.assertEqual([1,2,3,4,5,6,7,8,9], self.lst1.get_as_array())

    def test_search(self):
        self.assertFalse(self.lst1.search(78987))
        self.assertEqual(self.lst1.search(4), (4, 3))


if __name__ == '__main__':
    unittest.main()