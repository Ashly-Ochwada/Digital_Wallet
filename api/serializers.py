from rest_framework import serializers
from Wallet.models import Customer,Wallet,Account, Card, Loan, Notification, Receipt, Reward, Thirdparty,Transaction
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields=("firstname","email","age","address","gender")

class  WalletSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Wallet
        fields = ("balance","status")   

 
class  AccountSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Account
        fields = ("account_number", "balance", "name")             


class  CardSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Card
        fields = ("card_number","user_name")           

class  LoanSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Loan
        fields = ("amount", "loanterm")   

class  NotificationSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Notification
        fields = ("name", "status")                  

class  ReceiptSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Receipt
        fields = ("receiptdate", "receipttype")           

class  RewardSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Reward
        fields = ("customer_id", "points")   


class  ThirdpartySerializer(serializers.ModelSerializer) :
    class Meta:
        model = Thirdparty
        fields = ("name", "phone_number")   

class  TransactionSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Transaction
        fields = ("transaction_amount", "origin_account","destination_account")           