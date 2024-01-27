from django.urls import path

from registration.views import SignInApiView, SignUpApiView


urlpatterns = [
    path("signin/", SignInApiView.as_view(), name="signin"),
    path("signup/", SignUpApiView.as_view(), name="signup"),
]
