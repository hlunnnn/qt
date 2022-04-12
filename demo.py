# import unittest
#
# from selenium import webdriver
#
#
# class TestLogin(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome()
#         cls.driver.find_element().get_attribute()
#         pass
#     @classmethod
#     def tearDownClass(cls):
#         pass
#
#     def test_login(self):
#
#         self.assertIn("hluntest001@163.com","dasdadhluntest001@162.comdasdad")
#
# if __name__ == '__main__':
#     unittest.main()



class a:
    # n = 1
    # def pr(self):
    #     self.n+=1
    #     print(self.n)

    @classmethod
    def aa(cls):
        cls.a = 3
        b = 2
        print(b)

    def cc(self):
        print(self.a)


if __name__ == '__main__':
    a.aa()
    a().cc()