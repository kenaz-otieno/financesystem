from django.contrib.auth import get_user_model

User = get_user_model()


class AccountNoBackend:

    def authenticate(self, account_no=None, password=None):
        try:
            user = User.objects.get(account_no=account_no)
            if user and user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None