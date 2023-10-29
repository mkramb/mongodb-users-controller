from kr8s.asyncio.objects import APIObject
from pymongo import MongoClient

from mongodb_users_controller.crds import MongoUserResource
from mongodb_users_controller.settings import MONGO_URI


class MongoUserResourceConfig(APIObject):
    version = f"{MongoUserResource.__group__}/{MongoUserResource.__version__}"
    kind = MongoUserResource.__name__.lower()
    singular = MongoUserResource.singular()
    plural = MongoUserResource.plural()
    endpoint = MongoUserResource.plural()
    namespaced = True

    async def user_create(self):
        client = MongoClient(MONGO_URI)
        client.get_database().command(
            "createUser",
            self.spec.username,
            pwd=self.spec.password,
            roles=self.spec.roles,
        )
        client.close()

    async def user_delete(self):
        client = MongoClient(MONGO_URI)
        client.get_database().command("dropUser", self.spec.username)
        client.close()
