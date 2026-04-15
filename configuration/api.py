from ninja import NinjaAPI
from core.api import router as core_router
from user.api import router as user_router

api = NinjaAPI(
    title="LiveDocX API",
    version="1.0.0"
)

api.add_router("/core/", core_router)
api.add_router("/user/", user_router)
