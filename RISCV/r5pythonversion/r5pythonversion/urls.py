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

from django.conf.urls import url
from . import views
from . import Display_settings
from . import Simulator_buttons
from . import Display_Info
urlpatterns = [
    url(r'^$', views.home),
    url(r'^displayI', Display_Info.Display_info_I, name='displayI'),
    url(r'^Mdisplay', Display_Info.Display_info_IM, name='Mdisplay'),
    url(r'^IMCdisplay', Display_Info.Display_info_IMC, name='IMCdisplay'),
    url(r'^execute', Simulator_buttons.index, name='index'),
    url(r'^step', Simulator_buttons.step_by_step, name='step'),
    url(r'^reset', Simulator_buttons.reseting, name='reset'),
    url(r'^prev', Simulator_buttons.prev, name='prev'),
    url(r'^dump', Simulator_buttons.dump, name='dump'),
    url(r'^dec', Display_settings.decimal, name='dec'),
    url(r'^hex', Display_settings.hex, name='hex'),
    url(r'^unsign', Display_settings.unsigned, name='unsign'),
    url(r'^ascii', Display_settings.ascii, name='ascii'),

]
