from rest_framework import routers

from post_app.viewsets import PostViewset

router = routers.DefaultRouter()
router.register(r'posts', PostViewset)