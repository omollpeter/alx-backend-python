class ToyStore:
    def send_email(self, customer_email, message):
        print(f"Sending email to {customer_email}: {message}")
    
    def buy_toy(self, customer_email):
        # Some logic for buying a toy
        self.send_email(customer_email, "Thank you for buying a toy!")
