from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def process_text(request):
    if request.method == 'POST':
        received_text = request.POST.get('text', '')
        ## Add code here
        response = received_text + "dks3hd"
        print(received_text)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request method'})
