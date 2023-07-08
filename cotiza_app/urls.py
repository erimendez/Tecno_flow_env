from django.contrib import admin
from .router import router
from django.urls import path 

from .views import      CotizaListView   \
                    ,   CotizaDetailView \
                    ,   CotizaCreateView \
                    ,   CotizaUpdateView \
                    ,   CotizaDeleteView

app_name = "cotiza"

urlpatterns = [
    path("", CotizaListView.as_view(), name="all"),
    path("create/", CotizaCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", CotizaDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CotizaUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CotizaDeleteView.as_view(), name="delete"),

]

urlpatterns += router.urls