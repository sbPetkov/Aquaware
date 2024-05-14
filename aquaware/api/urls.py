from django.urls import path

from aquaware.api.views import ProfileListCreateView, ProfileRetrieveUpdateDestroy, CreateUserView

urlpatterns = [
    path('profiles/', ProfileListCreateView.as_view(), name='profiles-api-view'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroy.as_view(), name='retrieve-update-delete-api-view'),
    path('profiles/create/', CreateUserView.as_view(), name='create-user-view'),

]
