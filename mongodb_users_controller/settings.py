import os
import decouple

KUBE_PROD = decouple.config("KUBE_PROD", default=False, cast=bool)
KUBE_CONFIG = decouple.config(
    "KUBE_CONFIG", default=f"{os.path.expanduser('~')}/.kube/config"
)

MONGO_URI = decouple.config(
    "MONGO_URI",
    default="mongodb://localhost:27017/platform?replicaSet=tilt&directConnection=true",
)
