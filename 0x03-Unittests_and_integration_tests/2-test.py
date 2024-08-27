from unittest.mock import patch
import unittest

class ToyStore:
    def send_email(self, customer_email, message):
        print(f"Sending email to {customer_email}: {message}")
    
    def buy_toy(self, customer_email):
        # Some logic for buying a toy
        self.send_email(customer_email, "Thank you")


class TestToyStore(unittest.TestCase):
    @patch.object(ToyStore, "send_email")
    def test_buy_toy_sends_email(self, mock_send_email):
        store = ToyStore()
        store.buy_toy("cutomer@gnaul.com")

        mock_send_email.assert_called_once_with('cutomer@gnaul.com', "Thank you")
