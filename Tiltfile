cfg = config.parse()

docker_prune_settings(
    disable=False,
    num_builds=3,
    keep_recent=2
)

# mongodb
k8s_yaml(["mongo.yaml"])
k8s_resource(
    "mongodb-standalone",
    port_forwards=["27017:27017"]
)
