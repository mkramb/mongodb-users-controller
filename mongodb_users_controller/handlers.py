import kopf
import asyncio
import logging
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


@kopf.on.create(MongoUserResourceConfig.kind)
async def on_create(body, namespace, **kwargs):
    try:
        kubernetes_client = get_client()
        resource = await MongoUserResourceConfig(
            body, namespace=namespace, api=kubernetes_client
        )

        await resource.user_create()
    except logging.exception as error:
        loguru.logger.error("Error creating Mongo User", error)


@kopf.on.delete(MongoUserResourceConfig.kind)
async def on_delete(body, namespace, **kwargs):
    try:
        kubernetes_client = get_client()
        resource = await MongoUserResourceConfig(
            body, namespace=namespace, api=kubernetes_client
        )

        await resource.user_delete()
    except logging.exception as error:
        loguru.logger.error("Error deleting Mongo User", error)
