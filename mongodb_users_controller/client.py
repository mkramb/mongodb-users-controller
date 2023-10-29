import kubernetes
from loguru import logger

from mongodb_users_controller.settings import KUBE_PROD, KUBE_CONFIG


def get_client():
    if KUBE_PROD:
        logger.info("Loading in-cluster config")
        kubernetes.config.load_incluster_config()
    else:
        logger.info("Loading from local k8s config")
        kubernetes.config.load_kube_config(config_file=KUBE_CONFIG)

    return kubernetes.client.ApiClient()
