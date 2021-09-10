from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.urls import reverse
from .models import Notes
from .forms import NotesForm


class ListNotes(ListView):
    template_name = 'notes.html'
    queryset = Notes.objects.all()

class CreateNotes(CreateView):
    template_name = 'change.html'
    form_class = NotesForm
    queryset = Notes.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)
    
class DetailNotes(DetailView):
    template_name = 'detail.html'
    # queryset = Notes.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Notes, id=id_)

class UpdateNotes(UpdateView):
    template_name = 'change.html'
    form_class = NotesForm
    # queryset = Notes.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Notes, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteNotes(DeleteView):
    template_name = 'delete.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Notes, id=id_)

    def get_success_url(self):
        return reverse('notes:note-list')













# def ListNotes(request):
#     queryset = Notes.objects.all()
#     context = {
#         "title": "Notes",
#         "obj": queryset
#     }
#     return render(request, 'notes.html', context)

# def DetailNotes(request, pk):
#     query = get_object_or_404(Notes, id=pk)
#     context = {
#         "title": "Detail",
#         "obj": queryset
#     }
#     return render(request, 'detail.html', context)

# def CreateNotes(request):
#     form = NotesForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('note-list')
#     context = {
#         "title": "Add Notes",
#         "form": form,
#         "btn": "Create"
#     }
#     return render(request, 'change.html', context)

# def UpdateNotes(request, pk):
#     query = get_object_or_404(Notes, id=pk)
#     form = NotesForm(request.POST or None, instance=query)
#     if form.is_valid():
#         form.save()
#         return redirect('note-list')
#     context = {
#         "title": "Edit Notes",
#         "form": form,
#         "btn": "Edit"
#     }
#     return render(request, 'change.html', context)

# def DeleteNotes(request, pk):
#     query = get_object_or_404(Notes, id=pk)
#     if request.method == "POST":
#         query.delete()
#         return redirect('note-list')
#     context = {
#         "delete": query
#     }
#     return render(request, "delete.html", context)