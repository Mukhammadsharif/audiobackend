from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from users.utils.authentication import sign_in_response


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    authentication_classes = [SessionAuthentication]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        return Response(sign_in_response(request.user))


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    authentication_classes = [SessionAuthentication]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        return Response(sign_in_response(request.user))
