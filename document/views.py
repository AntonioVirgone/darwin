from django.shortcuts import render, redirect

from document.forms import PostForm
from .models import Document


# Create your views here.
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print(str(form))
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'manager/document_edit.html', {'form': form})


def post_detail(request, pk):
    # for e in Document.objects.all():
    #     print(e.pk)

    if Document.objects.filter(pk=pk):
        doc = Document.objects.get(pk=pk)
        print(doc)

    return render(request, 'manager/document_detail.html')

