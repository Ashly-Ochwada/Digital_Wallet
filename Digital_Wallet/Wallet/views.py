from django.shortcuts import render

# from Digital_Wallet.Wallet.models import Notification
from .models import Account, Card, Customer, Notification, Receipt, Reward, Transaction, Wallet, Loan
# Create your views here.
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegistrationForm,TransactionRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdpartyRegistrationForm, WalletRegistrationForm

# Create your tests here.
# handles the http request #

def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm()
        if form.is_valid():
            form.save()
    else:
        form = CustomerRegistrationForm()        
    return render(request, "wallet/register_customer.html", 
    {"form": form}
        )

def list_customers(request):
    customers = Customer.objects.all()
    return render(request,"wallet/customer_list.html",
    {"Customers": customers} )

# 

def register_wallet(request):
        if request.method == "POST":
            form = WalletRegistrationForm()
            if form.is_valid():
                form.save()
        else:
            form = WalletRegistrationForm()             

        return render(request, "wallet/register_wallet.html",
      {"form": form}
          )
def list_wallets(request):
    wallets = Wallet.objects.all()
    return render(request,"wallet/wallet_list.html",
    {"Wallets": wallets} )         



def register_account(request):
        if request.method == "POST":
            form = AccountRegistrationForm()
            if form.is_valid():
                form.save()
        else:
            form = AccountRegistrationForm()   

        return render(request, "wallet/register_account.html",
        {"form": form}
        )
def list_accounts(request):
    accounts = Account.objects.all()
    return render(request,"wallet/account_list.html",
    {"Accounts": accounts} )  


def register_transaction(request):
            if request.method == "POST":
                form = TransactionRegistrationForm()
                if form.is_valid():
                   form.save()
            else:
                form = TransactionRegistrationForm()   
            return render(request, "wallet/register_transaction.html",
            {"form": form}
            )   
def list_transactions(request):
    transactions= Transaction.objects.all()
    return render(request,"wallet/transaction_list.html",
    {"Transactions": transactions} )              



def register_receipt(request):
         if request.method == "POST":
                form = ReceiptRegistrationForm()
                if form.is_valid():
                   form.save()
         else:
            form = ReceiptRegistrationForm()   
            return render(request, "wallet/register_receipt.html",
            {"form": form}
            )
def list_receipts(request):
    receipts= Receipt.objects.all()
    return render(request,"wallet/receipt_list.html",
    {"Receipts": receipts} )            



def register_card(request):
        if request.method == "POST":
            form = CardRegistrationForm()
            if form.is_valid():
                form.save()
        else:
            form = CardRegistrationForm()
        return render(request, "wallet/register_card.html",
        {"form": form}
        )
def list_cards(request):
    cards= Card.objects.all()
    return render(request,"wallet/card_list.html",
    {"Cards": cards} )   



def register_thirdparty(request):
        if request.method == "POST":
            form = ThirdpartyRegistrationForm()
            if form.is_valid():
                form.save()
        else:
            form = ThirdpartyRegistrationForm()        
        return render(request, "wallet/register_thirdparty.html",
        {"form": form}
        )
def list_thirdparties(request):
    thirdparties= Card.objects.all()
    return render(request,"wallet/thirdparty_list.html",
    {"Thirdparties": thirdparties} )



def register_notification(request):
    if request.method == "POST":
        form = NotificationRegistrationForm()
        if form.is_valid():
            form.save()
    else:
        form = NotificationRegistrationForm()        
    return render(request, "wallet/register_notification.html",
    {"form": form}
    )
def list_notifications(request):
    notifications= Notification.objects.all()
    return render(request,"wallet/notification_list.html",
    {"Notifications": notifications} )




def register_loan(request):
    if request.method == "POST":
        form = LoanRegistrationForm()
        if form.is_valid():
            form.save()
    else:
        form = LoanRegistrationForm()
    return render(request, "wallet/register_loan.html",
    {"form": form}
    ) 
def list_loans(request):
    loans= Loan.objects.all()
    return render(request,"wallet/loan_list.html",
    {"Loans": loans} )



def register_reward(request):
    if request.method == "POST":
        form = RewardRegistrationForm()
        if form.is_valid():
            form.save()
    else:
        form  = RewardRegistrationForm()
    return render(request, "wallet/register_reward.html",
    {"form": form}
    )   
def list_rewards(request):
    rewards= Reward.objects.all()
    return render(request,"wallet/reward_list.html",
    {"Loans": rewards} )      