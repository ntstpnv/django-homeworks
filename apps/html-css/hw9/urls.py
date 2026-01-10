from django.urls import path

from . import views


urlpatterns = [
    path("", views.MenuView.as_view(), name="hw9"),
    path("html-info/", views.HTMLInfoView.as_view(), name="html_info"),
    path("blog-preview/", views.BlogPreviewView.as_view(), name="blog_preview"),
    path("article-widget/", views.ArticleWidgetView.as_view(), name="article_widget"),
]
