"""r5pythonversion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.conf.urls import url
from django.urls import include, re_path
from . import views
from . import Display_settings
from . import Simulator_buttons
from . import Display_Info
urlpatterns = [
    re_path(r'^$', views.home),
    re_path(r'^displayI', Display_Info.Display_info_I, name='displayI'),
    re_path(r'^Mdisplay', Display_Info.Display_info_IM, name='Mdisplay'),
    re_path(r'^IMCdisplay', Display_Info.Display_info_IMC, name='IMCdisplay'),
    re_path(r'^execute', Simulator_buttons.index, name='index'),
    re_path(r'^step', Simulator_buttons.step_by_step, name='step'),
    re_path(r'^reset', Simulator_buttons.reseting, name='reset'),
    re_path(r'^prev', Simulator_buttons.prev, name='prev'),
    re_path(r'^dump', Simulator_buttons.dump, name='dump'),
    re_path(r'^dec', Display_settings.decimal, name='dec'),
    re_path(r'^hex', Display_settings.hex, name='hex'),
    re_path(r'^unsign', Display_settings.unsigned, name='unsign'),
    re_path(r'^ascii', Display_settings.ascii, name='ascii'),

]
