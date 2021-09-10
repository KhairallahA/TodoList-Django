from django.urls import path
from .views import (
    ListNotes,
    CreateNotes,
    DetailNotes,
    UpdateNotes,
    DeleteNotes
)


app_name = "notes"

urlpatterns = [
    path('', ListNotes.as_view(), name="note-list"),
    path('create/', CreateNotes.as_view(), name="note-create"),
    path('<int:pk>/', DetailNotes.as_view(), name="note-detail"),
    path('<int:pk>/update/', UpdateNotes.as_view(), name="note-update"),
    path('<int:pk>/delete/', DeleteNotes.as_view(), name="note-delete"),
]





# urlpatterns = [
#     path('', ListNotes, name="note-list"),
#     path('create/', CreateNotes, name="note-create"),
#     path('<int:pk>/', DetailNotes, name="note-detail"),
#     path('<int:pk>/update/', UpdateNotes, name="note-update"),
#     path('<int:pk>/delete/', DeleteNotes, name="note-delete"),
# ]