from django.http import HttpResponse


# Create your views here.
def home(request):
    dir_name = request.GET.get('dir_name')
    file_name = request.GET.get('file_name')

    file_path = './deploy_document/' + dir_name + "/" + file_name
    with open(file_path, 'rb') as doc:
        response = HttpResponse(doc.read(), content_type='application/ms-word')
        response['Content-Disposition'] = 'attachment;filename=' + file_name
        return response
