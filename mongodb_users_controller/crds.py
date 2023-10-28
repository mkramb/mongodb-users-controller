from dataclasses import dataclass, field
from apischema import schema
from kubecrd import schemabase

@dataclass(frozen=True, order=True)
class UserResource(schemabase.KubeResourceBase):
    __group__ = 'mkramb.github.io'
    __version__ = 'v1'

    id: str
    name: str
    tags: list[str] = field(
        default_factory=list,
        metadata=schema(
            description='regroup multiple resources',
            unique=False,
        ),
    )