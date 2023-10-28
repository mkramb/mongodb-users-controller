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
./scripts/kind-cluster-delete.sh
./scripts/kind-cluster-create.sh
```

## Usage

Running full k8s stack:

```
tilt up

# to stop current pods
tilt down
```