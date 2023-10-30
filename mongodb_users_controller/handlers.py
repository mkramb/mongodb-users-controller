import kopf
import asyncio
import loguru

from mongodb_users_controller.client import get_client
from mongodb_users_controller.crds import MongoUserResource
from mongodb_users_controller.models import MongoUserModel

LOCK: asyncio.Lock


@kopf.on.startup()
@loguru.logger.catch()
async def on_startup(**kwargs):
    global LOCK
    LOCK = asyncio.Lock()

    loguru.logger.info("Installing CRDs")
    kubernetes_client = get_client()
    MongoUserResource.install(kubernetes_client, exist_ok=True)


@kopf.on.create(MongoUserModel.kind)
@loguru.logger.catch()
async def on_create(body, namespace, **kwargs):
    resource = MongoUserModel(body, namespace=namespace, api=get_client())
    await resource.user_create()

    loguru.logger.info(f"Created User: {resource.spec.username}")


@kopf.on.delete(MongoUserModel.kind)
@loguru.logger.catch()
async def on_delete(body, namespace, **kwargs):
    resource = MongoUserModel(body, namespace=namespace, api=get_client())
    await resource.user_delete()

    loguru.logger.info(f"Deleted User: {resource.spec.username}")
