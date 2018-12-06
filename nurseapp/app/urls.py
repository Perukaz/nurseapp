from django.urls import path

from . import views
# urls de los endpoints
urlpatterns = [
    path('datos/<int:doc>', views.CharData.as_view(), name='api-data'),
    path('heartrate/<int:bpm>', views.HeartRateEndPoint.as_view(),
         name='api-hr'),
    path('bloodpressure/<int:press>', views.BloodPressureEndPoint.as_view(),
         name='api-bp'),
]
