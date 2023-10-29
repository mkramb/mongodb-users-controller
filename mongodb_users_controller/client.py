import os
import kubernetes
from loguru import logger
from decouple import config


def get_client():
    LOCAL = config("LOCAL", default=False, cast=bool)

    if LOCAL:
        logger.info("Loading from local k8s config")
        user_home = os.path.expanduser("~")
        kube_config = config("KUBE_CONFIG", default=f"{user_home}/.kube/config")
        kubernetes.config.load_kube_config(config_file=kube_config)
    else:
        logger.info("Loading in-cluster config")
        config.load_incluster_config()

    return kubernetes.client.ApiClient()
