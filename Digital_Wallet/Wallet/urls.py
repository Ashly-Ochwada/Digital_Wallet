from django.urls import path
from .import views
from .views import list_customers,register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet, register_account


urlpatterns = [
    path("register/", register_customer, name = "registration"),
    path("customers/", list_customers, name = "customers_list"),


    path("register/", register_wallet, name="registration"),
    path("wallets/", views.list_wallets, name = "wallets_list"),


    path("register/", register_account, name="registration"),
    path("accounts/",views.list_accounts, name = "accounts_list"),


    path("register/", register_transaction, name="registration"),
    path("transactions/", views.list_transactions, name = "transactions_list"),



    path("register/", register_receipt, name="registration"),
    path("receipts/", views.list_receipts,name="receipts_list"),


    path("register/", register_card, name="registration"),
    path("cards/", views.list_cards,name="cards_list"),



    path("register/", register_thirdparty, name="registration"),
    path("thirdparties/", views.list_thirdparties,name="thirdparties_list"),



    path("register/", register_notification, name="registration"),
    path("notifications/", views.list_notifications,name="notifications_list"),


    path("register/", register_loan, name="registration"),
    path("loans/", views.list_loans,name="loans_list"),


    path("register/", register_reward, name="registration"),
     path("rewards/", views.list_rewards,name="rewards_list"),
]


#filtering



