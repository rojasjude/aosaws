import unittest
from time import sleep

import aosaws_methods as methods


class AosAppPositiveTestCases(unittest.TestCase):  # create class

    @staticmethod
    def test_create_aos():
        methods.setUp()
        # create account
        methods.create_user()
        methods.logout()
        methods.login()
        # check website components
        methods.check_text()
        methods.check_tab_menu()
        methods.check_logo()
        methods.contact_us()
        methods.check_social_media()
        methods.homepage()
        # add to cart and check out
        methods.click_tablets()
        methods.add_cart()
        methods.checkout()
        methods.check_order()
        methods.view_order()
        methods.homepage()
        # validate no order, delete account and validate deleted account
        methods.logout()
        sleep(2.5)
        methods.login()
        #methods.validate_no_order()
        methods.delete_account()
        methods.login_deleted_account()
        # end
        methods.tearDown()


if __name__ == "__main__":
    unittest.main()
