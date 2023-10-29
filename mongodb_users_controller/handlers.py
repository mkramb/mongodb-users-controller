import kopf
import asyncio
import loguru

from mongodb_users_controller.client import get_client
from mongodb_users_controller.crds import MongoUserResource
from mongodb_users_controller.models import MongoUserResourceConfig

LOCK: asyncio.Lock


@kopf.on.startup()
async def on_startup(**kwargs):
    global LOCK
    LOCK = asyncio.Lock()

    loguru.logger.info("Installing CRDs")
    kubernetes_client = get_client()
    MongoUserResource.install(kubernetes_client, exist_ok=True)


@loguru.logger.catch
@kopf.on.create(MongoUserResourceConfig.kind)
async def on_create(body, namespace, **kwargs):
    resource = MongoUserResourceConfig(body, namespace=namespace, api=get_client())
    await resource.user_create()
    loguru.logger.info(f"Created User: {resource.spec.username}")


@loguru.logger.catch
@kopf.on.delete(MongoUserResourceConfig.kind)
async def on_delete(body, namespace, **kwargs):
    resource = MongoUserResourceConfig(body, namespace=namespace, api=get_client())
    await resource.user_delete()

    loguru.logger.info(f"Deleted User: {resource.spec.username}")
