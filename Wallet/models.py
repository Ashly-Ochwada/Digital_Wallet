from datetime import datetime

from django.db import models

# #onboard customer
# deposit money
# withdraw money
# transfer money
# get a Loan
# repay a Loan
# generate digital cards
# Eearn rewards


# Create your models here.
class Customer(models.Model):
    firstname=models.CharField(max_length=15,null=True)
    lastname=models.CharField(max_length=15,null=True)
    address=models.TextField(null=True)
    # email=models.EmailField(default=10)
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    age = models.PositiveSmallIntegerField(default= False)
    nationality = models.CharField(max_length=15,blank=True)
    id_number = models.CharField(max_length=15,blank=True)
    phone_number = models.CharField(max_length=15,blank=True)
    email = models.EmailField(default=False)
    MARITAL_STATUS = (
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('S', 'Single')
    )
    marital_status = models.CharField(max_length=1,choices = MARITAL_STATUS,null=True)
    employment_status = models.CharField(max_length=20,default=None)

class Wallet(models.Model):    
   balance=models.IntegerField()
   currency=models.CharField(max_length=50,null=True)
   status=models.CharField(max_length=20,null=True)
   date=models.DateTimeField()
   amount=models.IntegerField()
   pin=models.PositiveSmallIntegerField()

class Account(models.Model):
    account_number=models.IntegerField(null=True)
    account_type=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=20,null=True)
    balance=models.IntegerField
    name=models.CharField(max_length=15, null=True)
    def deposit(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.account_balance += amount
           self.save()
           message = f"You have deposited {amount}, your new balance is {self.account_balance}"
           status = 200
       return message, status

    def transfer(self, destination, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount < self.account_balance:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.account_balance -= amount
           self.save()
           destination.deposit(amount)
          
           message = f"You have transfered {amount}, your new balance is {self.account_balance}"
           status = 200
       return message, status   

class Transaction(models.Model):
    transaction_code=models.CharField(max_length=20,null=True)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,null=True)
    transaction_amount=models.IntegerField(null=True)
    transaction_type=models.CharField(max_length=20,null=True)
    transaction_charge=models.IntegerField(null=True)
    transactiondateandtime=models.DateTimeField(default=datetime.now)
    origin_account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True,related_name="account_a")
    destination_account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True,related_name="account_b")

class Receipt(models.Model):
    receiptdate=models.DateTimeField()
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,null=True)
    number=models.IntegerField
    file=models.FileField(max_length=20)
    receipttype=models.CharField
    amount=models.BigIntegerField  



class Card(models.Model):
    card_number=models.IntegerField(null=True)
    user_name=models.CharField(max_length=20,null=True)
    date_issue=models.DateTimeField(default=datetime.now)
    card_type=models.CharField(max_length=20,null=True)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,null=True)
    Account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)



class Thirdparty(models.Model):
    name=models.CharField(max_length=20,null=True)
    account=models.ForeignKey(on_delete=models.CASCADE,to=Account,null=True)
    phone_number=models.CharField(max_length=20,null=True)
    id=models.PositiveSmallIntegerField(primary_key=True)


class Notification(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    name=models.CharField(max_length=20,null=True)
    date_and_time=models.DateTimeField(default=datetime.now)
    status=models.CharField(max_length=20)
   
class Loan(models.Model):
    loan_number=models.IntegerField(null=True)
    loan_type =models.CharField(max_length=32,null=True)
    amount=models.BigIntegerField(null=True)
    dateandtime=models.DateTimeField(default=datetime.now)
    wallet=models.ForeignKey(null=True,on_delete=models.CASCADE,to=Wallet)
    loanbalance=models.IntegerField(null=True)
    loanterm=models.IntegerField(null=True)
    payduedate=models.DateTimeField(default=datetime.now)

class Reward(models.Model):
    transaction = models.ForeignKey(on_delete=models.CASCADE,to=Transaction)
    customer_id=models.IntegerField(null=True)
    description=models.TextField(max_length=1500)
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
    date_and_time=models.DateTimeField(default=datetime.now)
    points=models.IntegerField(null=True)