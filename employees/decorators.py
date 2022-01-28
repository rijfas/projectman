from django.contrib.auth.decorators import login_required, user_passes_test


def manager_login_required(function):
    actual_decorator = user_passes_test(lambda u: u.is_manager)
    return actual_decorator(function)
