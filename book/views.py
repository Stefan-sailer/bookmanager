from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {
        'name' : '双11'
    }
    return render(request, 'book/index.html', context=context)


def shop(request, local_id, shop_id):

    return HttpResponse('li的shop')

def register(request):
    data = request.POST
    print(data)
    return HttpResponse("OK_request")

def json(request):
    body = request.body
    # print(body)
    import json
    body_str=body.decode()
    body_dict=json.loads(body_str)
    print(body_dict)


    return HttpResponse('OK_json')

def set_cookie(request):
    username = request.GET.get('username')

    response = HttpResponse('set_cookies')

    response.set_cookie('name', username)
    return response