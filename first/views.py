from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
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
    query_count=query.count()
    print(query_count)
    p={
        'data':query,
        'data_count':query_count,
    }
    return render(request, 'view.html', p)

# This is to view Single Data
def single_data(request, ab):
    query=FirstModel.objects.get(id=ab)

    p={
        'url_params':ab,
        'data':query,
    }
    return render(request, 'single_data.html', p)
    
def update_data(request, ab):
    if request.method == "POST":
        product = get_object_or_404(FirstModel, id=ab)
        product.model_name = request.POST['model_name']
        product.save()
        return redirect('listing')

    p={

    }
    return render(request, 'update_data.html', p)
    
def delete_data(request , ab):
    query = FirstModel.objects.get(id = ab)
    query.delete()
    return redirect('viewdata')

