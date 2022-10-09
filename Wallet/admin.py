from ast import Call
from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Wallet,Transaction
# Register your models here.
class CustomerAdmin (admin.ModelAdmin):
    list_display = ("firstname", "lastname","address")
    search_fields  = ("firstname", "lastname",)

admin.site.register(Customer,CustomerAdmin)  

class NotificationAdmin (admin.ModelAdmin):
    list_display = ("name", "status")
    search_fields = ("name", "status")
admin.site.register(Notification,NotificationAdmin)

class WalletAdmin (admin.ModelAdmin):
    list_display = ("balance", "currency", "status")
    search_fields = ("currency", "status")
admin.site.register(Wallet, WalletAdmin)   

class AccountAdmin (admin.ModelAdmin):
    list_display = ("account_number", "balance", "name")
    search_fields = ("name","account_number" )
admin.site.register(Account,AccountAdmin)  

class TransactionAdmin (admin.ModelAdmin):
    list_display = ("transaction_amount", "origin_account","destination_account")
    search_fields = ("origin_account","destination_account")
admin .site.register(Transaction, TransactionAdmin)

class CardAdmin (admin.ModelAdmin):
    list_display = ("card_number","user_name", "wallet")
    search_fields = ("card_number","user_name")
admin.site.register(Card, CardAdmin)  

class ThirdpartyAdmin (admin.ModelAdmin):
    list_display = ("name", "phone_number")
    search_fields = ("name", "phone_number")
admin.site.register(Thirdparty, ThirdpartyAdmin)

class ReceiptAdmin (admin.ModelAdmin):
    list_display = ("receiptdate", "receipttype")
    search_fields = ("receiptdate", "receipttype")
admin.site.register(Receipt, ReceiptAdmin)

class LoanAdmin (admin.ModelAdmin):
    list_display = ("amount", "wallet", "loanterm")
    search_fields = ("amount", "wallet")
admin.site.register(Loan, LoanAdmin)

class RewardAdmin (admin.ModelAdmin):
    list_display = ("customer_id", "points")
    search_fields = ("customer_id", "points")
admin.site.register(Reward, RewardAdmin)