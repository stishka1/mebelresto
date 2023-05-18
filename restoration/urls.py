from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('page/<int:page_number>/', views.index, name='index'),

    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),

    # path('<pk>/', views.detail, name='detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Поиск по тегам с автозаполнением на ajax и javascript
    path('live_search/', views.live_search, name='live_search'),
    # Отдельная страница с результатами поиска (нажат enter)
    path('search/', views.search, name='search_results'),

    path('post_modal/<int:id>/', views.post_modal, name='post_modal'),
    
    # ссылка на пост (детальная страница)
    path('<slug:slug>/', views.detail, name='detail'),
    
    # выборка постов по тегу
    path('tag/<str:tag_slug>/', views.tag_list, name='tag_list'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
