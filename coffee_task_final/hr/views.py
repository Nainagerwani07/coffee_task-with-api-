from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Category
from .forms import PersonForm

from django.http import HttpResponse
from django.core import serializers


class CategoryListView(ListView):
    model = Category
    context_object_name = 'people'


class CategoryCreateView(CreateView):
    print('dcfvgb')
    model = Category
    form_class = PersonForm
    success_url = reverse_lazy('ajax_load_cities')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = PersonForm
    success_url = reverse_lazy('category_changelist')


def load_cities(request):
    print("ajax-----call")

    machineid = request.GET.get('machine')
    if machineid == '':
        machineid = '0'
    machine_id = int(machineid)
    print('-----',machine_id)

    type1 = request.GET.get('Type')
    print('------->',type1)
    if type1 == '':
        type1 = '0'
    category = int(type1)

    coffee_Pods = request.GET.get('coffeePod')
    if coffee_Pods == '':
        coffee_Pods = '0'
    coffee_pod = int(coffee_Pods)

    flavour = request.GET.get('flavour')
    if flavour == '':
        flavour = '0'
    flav = int(flavour)

    wl = request.GET.get('wl')
    if wl == '':
        wl = '0'
    water = int(wl)
    
    pack_size = request.GET.get('packsize')
    if pack_size == '':
        pack_size = '0'
    pack = int(pack_size)

    # choice = Category.objects.filter(machine=machine_id,Type=Type,coffeePod=coffeePods,flavour=flavour,wl=water,packsize=packsize).order_by('name')
    # choice = Category.objects.filter(machine=machine_id,Type=Type,cate).order_by('name')
    
    # print(choice)
    # for c in choice:
        # print(c.name)
        # print(c.machine)

    if coffee_pod != 00 and flav == 00 and pack == 00 and machine_id == 00 and category == 00 and water == 00:
        options = Category.objects.filter(coffeePod=coffee_pod).order_by('option')
    elif coffee_pod == 00 and flav != 00 and pack == 00 and machine_id == 00 and category == 00 and water == 00:
        options = Category.objects.filter(flavour=flav).order_by('option')
    elif coffee_pod == 00 and flav ==00 and pack !=00 and machine_id == 00 and category == 00 and water == 00:
        options = Category.objects.filter(packsize=pack).order_by('option')
    elif coffee_pod != 00 and flav != 00 and pack == 00 and machine_id == 00 and category == 00 and water == 00:
        options = Category.objects.filter(coffeePod=coffee_pod,flavour=flav).order_by('option')
    elif coffee_pod == 00 and flav != 00 and pack != 00 and machine_id == 00 and category == 00 and water == 00:
        options = Category.objects.filter(packsize=pack,flavour=flav).order_by('option')
    elif coffee_pod != 00 and flav == 00 and pack != 00 and machine_id == 00 and category == 00 and water == 00:
        options = Category.objects.filter(packsize=pack,coffeePod=coffee_pod).order_by('option')
    elif coffee_pod != 00 and flav != 00 and pack != 00 and machine_id == 00 and category == 00 and water == 00:
        options = Category.objects.filter(flavour=flav,packsize=pack,coffeePod=coffee_pod).order_by('option')

    


    elif machine_id != 00 and category == 00 and water == 00 and flav == 00 and pack == 00 and coffee_pod == 00:
        options = Category.objects.filter(machine=machine_id).order_by('option')
        
    elif machine_id == 00 and category != 00 and water == 00 and flav == 00 and pack == 00 and coffee_pod == 00:
        options = Category.objects.filter(Type=category).order_by('option')

    elif machine_id == 00 and category ==00 and water !=00 and flav == 00 and pack == 00 and coffee_pod == 00:
        options = Category.objects.filter(wl=water).order_by('option')

    elif machine_id != 00 and category != 00 and water == 00 and flav == 00 and pack == 00 and coffee_pod == 00:
        options = Category.objects.filter(machine=machine_id,Type=category).order_by('option')

    elif machine_id == 00 and category != 00 and water != 00 and flav == 00 and pack == 00 and coffee_pod == 00:
        options = Category.objects.filter(wl=water,Type=category).order_by('option')

    elif machine_id != 00 and category == 00 and water != 00 and flav == 00 and pack == 00 and coffee_pod == 00:
        options = Category.objects.filter(wl=water,machine=machine_id).order_by('option')

    elif machine_id != 00 and category != 00 and water != 00 and flav == 00 and pack == 00 and coffee_pod == 00:
        options = Category.objects.filter(Type=category,wl=water,machine=machine_id).order_by('option')

    else:
        print('else')

    # JsonResponseData = {}
    JsonResponseData = serializers.serialize('json',options)    
    # print(JsonResponseData)

    file = open("hr/jsonFile.json","w")
    file.write(JsonResponseData)
    file.close()




    # print(options)
    for o in options:
            print(o.id,'->',o.option)

    return render(request, 'hr/city_dropdown_list_options.html', {'options': options,'hi':'123456'})

def json_File(request):
    file = open("hr/jsonFile.json")
    return HttpResponse(file)
