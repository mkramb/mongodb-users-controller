cfg = config.parse()

if config.tilt_subcommand == "down":
    print("Removing MongoDB Users Controller CRDs")
    local("kubectl get crds -oname | grep \"mkramb.com\" | xargs kubectl delete")

docker_prune_settings(
    disable=False,
    num_builds=3,
    keep_recent=2
)

# mongodb
k8s_yaml([".k8s/mongodb.yaml"])
k8s_resource(
    "mongodb-standalone",
    port_forwards=["27017:27017"]
)
