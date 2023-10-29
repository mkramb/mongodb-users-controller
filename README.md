# Mongo Users Controller

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

Run controller against local config:

```
LOCAL=true kopf run mongodb_users_controller/handlers.py  \
    --namespace=default --verbose
```


## Tips

Add example CRD item:

```
LOCAL=true python mongodb_users_controller/cli.py \
    --username example-user \
    --password example-secret-password
```
