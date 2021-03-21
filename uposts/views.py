from uposts.models import Posts
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'uposts/index.html'
    context_object_name = 'posts_list'
    def get_queryset(self):
        return Posts.objects.all()
