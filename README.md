# Mongo Users Controller

> Kubernetes Controller for managing Mongo Users (and roles), for community addition.

## Prerequisite

```
brew install kind
brew install tilt-dev/tap/tilt
brew install tilt-dev/tap/ctlptl
```

Install petry & dependencies:

```
curl -sSL https://install.python-poetry.org | python3 -
poetry config virtualenvs.in-project true
poetry install
```

Setting up local cluster:

```
./scripts/delete-kind-cluster.sh
./scripts/create-kind-cluster.sh
```

## Usage

Running full k8s stack:

```
tilt up

# to stop current pods
# and clear any defined CRDs
tilt down
```

To active and start a shell in virtual environment:

```
poetry shell
```

Run controller against local config:

```
export MONGO_URI="mongodb://localhost:27017/platform?replicaSet=tilt&directConnection=true"
kopf run mongodb_users_controller/handlers.py --namespace=default
```


## Tips

Add example CRD item:

```
python mongodb_users_controller/cli.py --username testuser --password secret-password --roles read,readWrite | kubectl apply -f -
```

To check available users using mongo shell:

```
use admin
db.system.users.find()
```

Inspect CRDs in the cluster:

```
kubectl get crds
kubectl get mongouserresources.mkramb.com -o yaml
```