from django.urls import path
from Authentication import views

urlpatterns = [
    path("", views.index, name="index"),

    # ====Authentication Urls
    path("signup/", views.signUp, name="signUp"),
    path("signIn/", views.signIn, name="signIn"),
    path("sign_out/", views.signOut, name="signOut"),






    path("FAQ/", views.FAQ, name="FAQ"),
    path("dashboard/", views.userDashboard, name="dashboard"),
    path("AboutUs/", views.aboutUs, name="aboutUs"),
    path("contact_Us/", views.contactUs, name="contact"),
    path("settings/", views.settings, name="settings"),
    path("split/", views.splitPage, name="split"),
    path("upload/", views.UploadPage, name="upload"),
    path("storage/", views.storage, name="storage"),
]
