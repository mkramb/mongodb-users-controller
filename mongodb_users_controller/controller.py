import kopf
import kubernetes
import asyncio

from crds import UserResource

LOCK: asyncio.Lock


@kopf.on.startup()
async def startup_fn(logger, **kwargs):
    global LOCK
    LOCK = asyncio.Lock()
    install_crd()


def install_crd():
    kubernetes.config.load_kube_config()
    k8s_client = kubernetes.client.ApiClient()
    UserResource.install(k8s_client, exist_ok=True)