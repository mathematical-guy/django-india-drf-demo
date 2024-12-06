from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from myapp.views import DRFWizardAPIVIew, DjangoWizardListView, DRFWizardViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("wizards", DRFWizardViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('django-wizards', django_wizard_list_view),
    path('django-wizards/', DjangoWizardListView.as_view()),
    path('drf-wizards/', DRFWizardAPIVIew.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
