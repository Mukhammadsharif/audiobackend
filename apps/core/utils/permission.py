from rest_framework.exceptions import PermissionDenied


def permission(perm):
    def wrapper(func):
        def check(view, request, *args, **kwargs):
            if not request.user.has_perm(perm):
                raise PermissionDenied()

            return func(view, request, *args, **kwargs)
        return check
    return wrapper
