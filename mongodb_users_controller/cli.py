import yaml
import argparse

from mongodb_users_controller.crds import MongoUserResource


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--roles", default="")
    args = parser.parse_args()

    input = {
        "username": args.username,
        "password": args.password,
        "roles": args.roles.split(","),
    }

    example_crd = MongoUserResource(**input)
    print(yaml.dump(example_crd.serialize(), indent=4))


if __name__ == "__main__":
    main()
