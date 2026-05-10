from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, PedidoViewSet

router = DefaultRouter()

router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = router.urls