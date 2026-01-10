from django.conf import settings

from apps.common import views


class MenuView(views.MenuView):
    queryset = [
        settings.LINK("Показать краткое описанием языка HTML", "html_info"),
        settings.LINK("Показать краткое описание статьи для блога", "blog_preview"),
        settings.LINK("Показать виджет статьи в блоге", "article_widget"),
    ]

    back = "html-css"


class HTMLInfoView(views.BaseTemplateView):
    template_name = "hw9/html_info.html"

    title = "Краткое описанием языка HTML"
    back = "hw9"


class BlogPreviewView(views.BaseTemplateView):
    template_name = "hw9/blog_preview.html"

    title = "Краткое описание статьи для блога"
    back = "hw9"


class ArticleWidgetView(views.BaseTemplateView):
    template_name = "hw9/article_widget.html"

    title = "Виджет статьи в блоге"
    back = "hw9"
