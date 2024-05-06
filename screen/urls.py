from django.urls import path
from .Views.ScreenView import ApiProof, ScreenView, Exec, SaveScreen,AsyncTask, EmailToken
from .Views.TokenView import Token
from .Views.UserView import User
from .Views.InfoView import Info
from rest_framework.authtoken import views

urlpatterns = [
    
    path('', ScreenView.as_view(), name="main_menu"),
    path('confirmar', Exec.as_view(), name="execute"),
    path('save_image', SaveScreen.as_view(), name="save"),
    path('save_image_db', ScreenView.as_view(), name="save_db"),
    path('proof', AsyncTask.as_view()),
    path('token', EmailToken.as_view()),
    path('token_confirm/<str:token>', Token.TokenConfirm.as_view(), name="token_confirm"),
    path('details_price/<id_img>/<price_current>', User.UserIPriceDetails.as_view(), name="user_Details"),

    path('details/<id_img>', User.ApiDetails.as_view()),
    
    path('prueba', ApiProof.as_view()),
    
    #info empresa
    
    path('about_us', Info.About.as_view(), name="about_us"),
    path('contact', Info.Contact.as_view(), name="contact"),
    path('termns', Info.Terms.as_view(), name="terms"),
    path('privacy', Info.Privacy.as_view(), name="privacy")
]