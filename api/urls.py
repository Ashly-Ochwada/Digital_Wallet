from django.urls import path,include
from rest_framework import routers
from .views import AccountViewSet, CardViewSet, CustomerViewSet, LoanViewSet, NotificationViewSet, ReceiptViewSet, RewardViewSet, ThirdpartyViewSet, TransactionViewSet, WalletViewSet,AccountDepositView


router = routers.DefaultRouter()
router.register(r"customers",CustomerViewSet)
router.register(r"wallets", WalletViewSet)
router.register(r"accounts", AccountViewSet)
router.register(r"cards", CardViewSet)
router.register(r"loans", LoanViewSet)
router.register(r"notifications", NotificationViewSet)
router.register(r"receipts", ReceiptViewSet)
router.register(r"rewards", RewardViewSet)
router.register(r"thirdparties", ThirdpartyViewSet)
router.register(r"transactions", TransactionViewSet)

urlpatterns=[
    path("",include(router.urls)),
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),


]



