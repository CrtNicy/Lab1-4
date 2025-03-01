from django.urls import path
from .views import owner_list, owner_detail, owner_create, owner_update, owner_delete, ownership_list, \
    CarOwnerCreateAndListView

urlpatterns = [
    path('', owner_list, name='owner_list'),
    path('<int:owner_id>/', owner_detail, name='owner_detail'),
    path('create/', owner_create, name='owner_create'),
    path('<int:owner_id>/update/', owner_update, name='owner_update'),
    path('<int:owner_id>/delete/', owner_delete, name='owner_delete'),
    path('ownership/', ownership_list, name='ownership_list'),
    path('owners/list/', CarOwnerCreateAndListView.as_view(), name='carowner-create'),
]
