from django.db import models
from django.contrib.auth.models import User

class UserPayment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='payment_types')
    card_number = models.CharField(max_length=16)
    exp_date = models.CharField(max_length=5)
    cvv = models.IntegerField()

    @property
    def obscured_num(self):
        """Obscure the account number

        Returns:
            string: ex. **********1234
        """
        return '*'*(len(self.card_number) - 4)+self.card_number[-4:]