from django.shortcuts import render
from rest_framework import viewsets
from Wallet.models import Customer,Wallet,Account, Card, Loan, Notification, Receipt, Reward, Thirdparty,Transaction
from .serializers import CustomerSerializer,WalletSerializer,AccountSerializer,CardSerializer,LoanSerializer,NotificationSerializer,ReceiptSerializer,RewardSerializer,ThirdpartySerializer,TransactionSerializer
from rest_framework import views
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset= Customer.objects.all()
    serializer_class =CustomerSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset= Wallet.objects.all()
    serializer_class =WalletSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset= Account.objects.all()
    serializer_class =AccountSerializer   

class CardViewSet(viewsets.ModelViewSet):
    queryset= Card.objects.all()
    serializer_class =CardSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset= Loan.objects.all()
    serializer_class =LoanSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset= Notification.objects.all()
    serializer_class = NotificationSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset= Receipt.objects.all()
    serializer_class = ReceiptSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset= Reward.objects.all()
    serializer_class = RewardSerializer

class ThirdpartyViewSet(viewsets.ModelViewSet):
    queryset= Thirdparty.objects.all()
    serializer_class = ThirdpartySerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset= Transaction.objects.all()
    serializer_class = TransactionSerializer    
# withdraw
# transfer
# request loan
# repay loan
# buy airtime

class AccountDepositView(views.APIView):
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)
    
