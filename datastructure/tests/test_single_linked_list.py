# -*- coding: utf-8 -*-
import unittest

from datastructure.linked_list.single_linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list = None

    def test_insert(self):
        self.list.insert("TestData")
        self.assertTrue(self.list.head.get_data() == "TestData")
        self.assertTrue(self.list.head.next() is None)

    def test_nextNode(self):
        pass
