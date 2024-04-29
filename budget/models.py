from django.db import models
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field

class Budget(models.Model):
    """Model representing a budget"""
    category = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """String for representing the Model object."""
        return self.category

    def get_absolute_url(self):
        """Returns the URL to access a detail record for the budget."""
        return reverse('budget-detail', args=[str(self.id)])


class Payment(models.Model):

    """Model representing a specific payment to a category."""
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='payments')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.amount} on {self.date}"

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this payment."""
        return reverse('payment-detail', args=[str(self.id)])