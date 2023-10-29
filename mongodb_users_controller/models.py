from kr8s.asyncio.objects import APIObject

from mongodb_users_controller.crds import MongoUserResource


class MongoUserResourceConfig(APIObject):
    version = f"{MongoUserResource.__group__}/{MongoUserResource.__version__}"
    kind = MongoUserResource.__name__.lower()
    singular = MongoUserResource.singular()
    plural = MongoUserResource.plural()
    endpoint = MongoUserResource.plural()
    namespaced = True

    async def user_create(self):
        print("Creating USER")
        print(f"USERNAME ===> {self.spec.username}")
        print(f"PASSWORD ===> {self.spec.password}")

    async def user_delete(self):
        print("Deleting USER")
        print(f"USERNAME ===> {self.spec.username}")
        print(f"PASSWORD ===> {self.spec.password}")
