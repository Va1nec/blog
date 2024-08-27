from django.shortcuts import render
from .models import video 
# Create your views here.

def video_list(request):
    videos = video.objects.all()
    return render(request, 'playlist/video_list.html', {'videos': videos})

def video_add(request):
    if request.method == "POST":
        title = request.POST['title']
        embed_code = request.POST['embed_code']
        Video.objects.create(title=title, embed_code=embed_code)
        return redirect('video_list')
    return render(request, 'playlist/video_add.html')