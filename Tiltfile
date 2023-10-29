config.define_bool("clear-crds")
config.define_bool("only-infra")

cfg = config.parse()

only_infra = cfg.get('only-infra', False)
clear_crds = cfg.get('clear-crds', False)

if clear_crds or config.tilt_subcommand == "down":
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
