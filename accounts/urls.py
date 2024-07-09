from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from accounts.views import  (
    AdminOnlyView, StaffOnlyView,UserListView, UserListCreateView,
    ObtainTokenPairWithRoleView, PasswordResetRequestView,
    PasswordResetConfirmView
)

urlpatterns = [
    path('register/', UserListCreateView.as_view(), name='register'),
    path('login/', ObtainTokenPairWithRoleView.as_view(), name='login'),
    # path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
    # path('staff-only/',StaffOnlyView.as_view(), name='staff-only'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api-token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]