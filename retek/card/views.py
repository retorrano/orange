from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from .models import Test
from .forms import TestAddForm, TestEditForm
# Create your views here.

@method_decorator(xframe_options_exempt, name='dispatch')
@login_required
def Index(request):
    not_framed=True
    return render(request,'index.html',{'not_framed':not_framed})

class TestAdd(CreateView):
    model = Test
    form_class = TestAddForm
    template_name = "card/save.html"
    success_url="/card"

class TestEdit(UpdateView):
    model = Test
    form_class = TestEditForm
    template_name = "card/save.html"
    success_url="/card"

class TestDelete(DeleteView):
    model = Test
    template_name="delete.html"
    success_url="/card"

def TestReader(request):
    return render(request,'card/reader.html')

def TestReaderAjax(request):
    card_number=request.GET.get('card_number')
    print(card_number)
    test = Test.objects.get(card_number=card_number)
    print(test.name)
    data = {
                'name' : test.name,
                'address':test.address,
        }   
    
    return JsonResponse(data)    
@login_required
def TestList(request):
    tests = Test.objects.all().order_by('name')
    paginator = Paginator(tests,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    not_framed = True
    return render(request, 'card/list.html',{'page_obj':page_obj,'not_framed':not_framed,})

