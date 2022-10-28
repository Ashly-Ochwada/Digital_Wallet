from django.shortcuts import render,redirect

# from Digital_Wallet.Wallet.models import Notification
from .models import Account, Card, Customer, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet, Loan
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

def edit_customer(request,id):
    customer=Customer.objects.get(id=id)
    if request.method =="POST":
        form=CustomerRegistrationForm(request.POST,instance=Customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile",id=customer.id)
    else:
        form=CustomerRegistrationForm(instance=Customer)
        return render(request,"wallet/edit_customer.html",{"form":form})    

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

def edit_wallet(request,id):
    wallet=Wallet.objects.get(id=id)
    if request.method =="POST":
        form=WalletRegistrationForm(request.POST,instance=Wallet)
        if form.is_valid():
            form.save()
            return redirect("wallet_profile",id=wallet.id)
    else:
        form=WalletRegistrationForm(instance=Wallet)
        return render(request,"wallet/edit_wallet.html",{"form":form})


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

def edit_account(request,id):
    account=Account.objects.get(id=id)
    if request.method =="POST":
        form=AccountRegistrationForm(request.POST,instance=Account)
        if form.is_valid():
            form.save()
            return redirect("account_profile",id=account.id)
    else:
        form=AccountRegistrationForm(instance=Account)
        return render(request,"wallet/edit_account.html",{"form":form})



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
def edit_transaction(request,id):
    transaction=Transaction.objects.get(id=id)
    if request.method =="POST":
        form=TransactionRegistrationForm(request.POST,instance=Transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_profile",id=transaction.id)
    else:
        form=TransactionRegistrationForm(instance=Transaction)
        return render(request,"wallet/edit_transaction.html",{"form":form})



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
def edit_receipts(request,id):
    receipt=Receipt.objects.get(id=id)
    if request.method =="POST":
        form=ReceiptRegistrationForm(request.POST,instance=Receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_profile",id=receipt.id)
    else:
        form=ReceiptRegistrationForm(instance=Receipt)
        return render(request,"wallet/edit_receipt.html",{"form":form})              



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
def edit_cards(request,id):
    card=Card.objects.get(id=id)
    if request.method =="POST":
        form=CardRegistrationForm(request.POST,instance=Receipt)
        if form.is_valid():
            form.save()
            return redirect("card_profile",id=card.id)
    else:
        form=CardRegistrationForm(instance=Card)
        return render(request,"wallet/edit_card.html",{"form":form}) 



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
def edit_thirdparties(request,id):
    thrirdparty=Thirdparty.objects.get(id=id)
    if request.method =="POST":
        form=ThirdpartyRegistrationForm(request.POST,instance=Thirdparty)
        if form.is_valid():
            form.save()
            return redirect("thirdparty_profile",id=thrirdparty.id)
    else:
        form=ThirdpartyRegistrationForm(instance=Thirdparty)
        return render(request,"wallet/edit_thirdparty.html",{"form":form}) 


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
def edit_notifications(request,id):
    notification=Notification.objects.get(id=id)
    if request.method =="POST":
        form=NotificationRegistrationForm(request.POST,instance=Notification)
        if form.is_valid():
            form.save()
            return redirect("notification_profile",id=notification.id)
    else:
        form=NotificationRegistrationForm(instance=Notification)
        return render(request,"wallet/edit_notification.html",{"form":form}) 



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
def edit_loans(request,id):
    loan=Loan.objects.get(id=id)
    if request.method =="POST":
        form=LoanRegistrationForm(request.POST,instance=Loan)
        if form.is_valid():
            form.save()
            return redirect("loan_profile",id=loan.id)
    else:
        form=LoanRegistrationForm(instance=Loan)
        return render(request,"wallet/edit_loan.html",{"form":form}) 


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
def edit_rewards(request,id):
    reward=Reward.objects.get(id=id)
    if request.method =="POST":
        form=RewardRegistrationForm(request.POST,instance=Reward)
        if form.is_valid():
            form.save()
            return redirect("reward_profile",id=reward.id)
    else:
        form=RewardRegistrationForm(instance=Reward)
        return render(request,"wallet/edit_reward.html",{"form":form})     


        