from django.http import JsonResponse


### User Based Views ###
def create_user(request):
    return JsonResponse({})

def retrieve_destroy_user(request, user=None):
    return JsonResponse({})


### Todo Based Views ###
def list_create_todo(request):
    return JsonResponse({})

def retrieve_update_destroy_todo(request, todo=None):
    return JsonResponse({})