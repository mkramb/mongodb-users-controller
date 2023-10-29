import kopf
import asyncio

from mongodb_users_controller.api import get_client
from mongodb_users_controller.crds import MongoUserResource

LOCK: asyncio.Lock


@kopf.on.startup()
async def on_startup(logger, **kwargs):
    global LOCK
    LOCK = asyncio.Lock()

    logger.info("Installing CRDs")
    kubernetes_client = get_client()
    MongoUserResource.install(kubernetes_client, exist_ok=True)


@kopf.on.create("mongouserresources")
async def on_create(spec, name, namespace, logger, **kwargs):
    resource = MongoUserResource(**spec)

    print(f"CREATE ===> {resource.username}")
    print(f"CREATE ===> {resource.password}")


@kopf.on.delete("mongouserresources")
async def on_delete(spec, name, namespace, logger, **kwargs):
    resource = MongoUserResource(**spec)

    print(f"DELETE ===> {resource.username}")
    print(f"DELETE ===> {resource.password}")
