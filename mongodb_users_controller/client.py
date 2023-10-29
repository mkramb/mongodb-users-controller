import os
import decouple
import kubernetes
from loguru import logger

KUBE_PROD = decouple.config("KUBE_PROD", default=False, cast=bool)
KUBE_CONFIG = decouple.config(
    "KUBE_CONFIG", default=f"{os.path.expanduser('~')}/.kube/config"
)


def get_client():
    if KUBE_PROD:
        logger.info("Loading in-cluster config")
        kubernetes.config.load_incluster_config()
    else:
        logger.info("Loading from local k8s config")
        kubernetes.config.load_kube_config(config_file=KUBE_CONFIG)

    return kubernetes.client.ApiClient()
