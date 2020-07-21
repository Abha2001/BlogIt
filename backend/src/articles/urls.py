from .views import ArticleView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'', ArticleView)

urlpatterns=router.urls

