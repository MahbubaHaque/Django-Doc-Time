from django.shortcuts import render

# Create your views here.
def videocall(request):
    print('video chatingg .....')
    return render(request, 'video_call.html')