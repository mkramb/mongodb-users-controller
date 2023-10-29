from dataclasses import dataclass, field
from kubecrd import schemabase
from apischema import schema

from mongodb_users_controller._api import get_client


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
            description="List of User roles",
            unique=False,
        ),
    )


def main():
    print(MongoUserResource().crd_schema())


if __name__ == "__main__":
    main()
