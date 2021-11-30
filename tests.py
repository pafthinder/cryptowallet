import unittest 
from wallet import Wallet 
from asset import * 

class TestWallet(unittest.TestCase):
    
    def test_wallet_has_an_initial_value(self):
        test_wallet = Wallet()
        self.assertNotEqual(test_wallet.value, None)

    def test_wallet_has_empty_assets_list(self):
        test_wallet = Wallet()
        self.assertEqual(test_wallet.assets_list, [])


class TestAsset(unittest.TestCase):

    test_asset = Asset() 


    # TODO - how to mock? 
    # TODO - do I need to test if object was properly created? what else could be created? 

if __name__ == "__main__":
    unittest.main()