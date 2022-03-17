from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from first.models import FirstModel


def first_view(request):
    # p={}

    # p['word']='This is from the Backend'
    # p['am']='Anything'

    p={
        'word':'This is from the Backend',
        'second':'anything'
        
        }
    return render(request, 'first.html', p)

def create_form(request):
    p={}
    if request.method == 'POST':
        firstname_frontend=request.POST['firstname']
        lastname_frontend=request.POST['lastname']
        query=FirstModel.objects.create(
            firstname=firstname_frontend,
            lastname=lastname_frontend,
        )
        # query.save()
        return redirect('viewdata')
        

    return render(request, 'create_form.html', p)
    
def view_data(request):
    # p={}
    # query=FirstModel.objects.filter(firstname__contains='a')
    query=FirstModel.objects.all()
    p={
        'data':query
    }
    return render(request, 'view.html', p)
    
    