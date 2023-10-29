import json
import argparse

from mongodb_users_controller.client import get_client
from mongodb_users_controller.crds import MongoUserResource


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
