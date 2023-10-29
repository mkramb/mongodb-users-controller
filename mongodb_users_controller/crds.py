import json
import argparse
from dataclasses import dataclass, field
from kubecrd import schemabase
from apischema import schema

from mongodb_users_controller.api import get_client


@dataclass
class UserRole:
    role: str
    database: str


@dataclass()
class MongoUserResource(schemabase.KubeResourceBase):
    __group__ = "mkramb.com"
    __version__ = "v1"

    username: str
    password: str

    roles: list[UserRole] = field(
        default_factory=list,
        metadata=schema(
            description="List of user roles",
            unique=False,
        ),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    args = parser.parse_args()

    kubernetes_client = get_client()
    example_crd = MongoUserResource(username=args.username, password=args.password)
    example_crd.save(kubernetes_client)

    print(json.dumps(example_crd.serialize(), indent=4))


if __name__ == "__main__":
    main()
