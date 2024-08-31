from aiogram import Router


def setup_routers() -> Router:
    from . import user_interaction

    router = Router()

    router.include_router(user_interaction.router)

    return router
