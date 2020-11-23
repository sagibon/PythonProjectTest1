from unittest import TestCase
from Package1.Worker import Worker

class TestWorker(TestCase):
    def setUp(self):
        self.bob = Worker('Bob', 'Marshall', 1970, 7, 5, "ha rav, kook 29", "Il")
        self.sagi = Worker('sagi', 'bondarenko', 1999, 11, 29, "ha rav, kook 29", "Il")
        print('setUP')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        self.assertEqual(self.bob.full_name(), "Bob Marshall")

    def test_age(self):
        age = 2020 - self.bob.birth_year
        self.assertEqual(50, age)
        if age < 0:
            self.fail()

    def test_age_past(self):#valid, normal age
        res = self.sagi.age()
        print(self.sagi.age())
        self.assertTrue(res == "sagi is 21 years old")

    def test_age_future(self):#not valid, negative age
        self.bob1 = Worker("bob", "mar", 2030, 11, 28, "afula", "israel")
        res = self.bob1.age()
        print(self.bob1.age())
        self.assertTrue(res == "error")

    def test_age_now(self):#valid, infant age
        self.bob1 = Worker("bob", "mar", 2020, 11, 28, "afula", "israel")
        res = self.bob1.age()
        print(self.bob1.age())
        self.assertTrue(res == "bob is 0 years old")

    def test_days_to_birthday(self):
        self.assertIn("6", self.sagi.days_to_birthday())
        pass

    def test_greet(self):
        self.assertEqual(self.bob.greet(self.sagi), 'Bob says hello to sagi')
        print(self.bob.greet(self.sagi))


    def test_location(self):
        """bob = Worker('Bob', 'Marshall', 1999, 11, 29, "23 Ha-Rav Kook St, Hadera", "Israel")
        self.assertTrue("23 Ha-Rav Kook St, HaderaA", bob.location())"""
        pass

