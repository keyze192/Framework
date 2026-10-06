from rest_framework.routers import DefaultRouter
from .views import ManufacturerViewsets, ProductViewsets

router = DefaultRouter()
router.register('manufacturer', ManufacturerViewsets)
router.register('product', ProductViewsets)

urlpatterns = router.get_urls()