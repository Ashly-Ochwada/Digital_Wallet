from django.urls import path
from .import views
from .views import edit_account, edit_cards, edit_customer, edit_loans, edit_notifications, edit_receipts, edit_rewards, edit_thirdparties, edit_transaction, list_customers,register_card, edit_wallet,register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet, register_account


urlpatterns = [
    path("register/", register_customer, name = "registration"),
    path("customers/", list_customers, name = "customers_list"),
    path("wallets/edit/<int:id>/",edit_customer,name="edit_customer"),



    path("register/", register_wallet, name="registration"),
    path("wallets/", views.list_wallets, name = "wallets_list"),
    path("wallets/edit/<int:id>/",edit_wallet,name="edit_wallet"),



    path("register/", register_account, name="registration"),
    path("accounts/",views.list_accounts, name = "accounts_list"),
    path("wallets/edit/<int:id>/",edit_account,name="edit_account"),


    path("register/", register_transaction, name="registration"),
    path("transactions/", views.list_transactions, name = "transactions_list"),
    path("wallets/edit/<int:id>/",edit_transaction,name="edit_transaction"),



    path("register/", register_receipt, name="registration"),
    path("receipts/", views.list_receipts,name="receipts_list"),
    path("wallets/edit/<int:id>/",edit_receipts,name="edit_receipts"),


    path("register/", register_card, name="registration"),
    path("cards/", views.list_cards,name="cards_list"),
    path("wallets/edit/<int:id>/",edit_cards,name="edit_cards"),



    path("register/", register_thirdparty, name="registration"),
    path("thirdparties/", views.list_thirdparties,name="thirdparties_list"),
    path("wallets/edit/<int:id>/",edit_thirdparties,name="edit_thirdparties"),



    path("register/", register_notification, name="registration"),
    path("notifications/", views.list_notifications,name="notifications_list"),
    path("wallets/edit/<int:id>/",edit_notifications,name="edit_notifications"),


    path("register/", register_loan, name="registration"),
    path("loans/", views.list_loans,name="loans_list"),
    path("wallets/edit/<int:id>/",edit_loans,name="edit_loans"),


    path("register/", register_reward, name="registration"),
     path("rewards/", views.list_rewards,name="rewards_list"),
     path("wallets/edit/<int:id>/",edit_rewards,name="edit_rewards"),
]


#filtering



