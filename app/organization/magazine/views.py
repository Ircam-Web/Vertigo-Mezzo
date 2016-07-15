from django.shortcuts import render
from django.utils import timezone
#from django.views.generic import *
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.base import *
from django.shortcuts import get_object_or_404

from organization.magazine.models import Article, Brief
from organization.core.views import SlugMixin

# Create your views here.
class ArticleDetailView(SlugMixin, DetailView):

    model = Article
    template_name='magazine/article/article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        return context

class ArticleListView(SlugMixin, ListView):

    model = Article
    template_name='magazine/article/article_list.html'
    # context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        return context


# Create your views here.
class BriefDetailView(SlugMixin, DetailView):

    model = Brief
    template_name='magazine/inc_brief.html'
    context_object_name = 'brief'

    def get_context_data(self, **kwargs):
        context = super(BriefDetailView, self).get_context_data(**kwargs)
        return context