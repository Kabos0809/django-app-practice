from datetime import date
from django.db.models import query
from django.http import request
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, redirect
from .models import article_form
from .forms import categorie_form


class IndexView(TemplateView):
    template_name = 'index.html'

class Complete_View(TemplateView):
    template_name = 'complete.html'

def formview(request):
    form = categorie_form()
    context = {'form' : form}
    if request.method == 'POST':
        data = request.POST
        title = data['title']
        rnk_min = data['rnk_min']
        rnk_max = data['rnk_max']
        num = data['num']
        per = data['per']
        comments = data['comments']
        hard = data['hard']

        article_form.objects.create(
            title = title,
            rnk_min = rnk_min,
            rnk_max = rnk_max,
            num = num,
            per = per,
            comments = comments,
            hard = hard,
        )
        return redirect('complete/')
    return render(request, 'form.html', context)

class Article_list(ListView):
    template_name = 'article_list.html'
    model = article_form
    ordering = ['-date']

class Article_detail(DetailView):
    template_name = 'detail.html'
    model = article_form
    context_object_name = 'object'
    queryset = article_form.objects.all()
