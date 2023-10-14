### Requirements
  - brew install bazel
  - version: 6.3.2-homebrew

### Run and Build
```shell
cd main

bazel build :app
```
```shell
cd main

bazel run :app
```
```shell
cd main

bazel run :hello -- \
  --age=45 \
  --job='running'
```
```shell
cd main

nohup bazel run :hello -- \
  --age=45 \
  --job='running' &
```
```shell
cd main

nohup bazel run :hello -- \
  --age=45 \
  --job='running' \
  --num_a=45 \
  --num_b=99 &
```

```shell
nohup bazel run main:hello -- \
  -n='elbowai' \
  --age=45 \
  --job='running' \
  --num_a=45 \
  --num_b=99 &
```
### Get helpful information
```shell
bazel run main:hello -- \
  --age=45 \
  --job='running' \
  --helpfull
```
```shell
sh run.sh
```

```python
python hello.py --age=99 --job='stopped'
```
```python
python test/test_example.py
```
### Dockerize Bazel
```shell
# build
docker build -t hello-python-bazel .
# run
docker run -it --rm hello-python-bazel
docker run -it hello-python-bazel

docker exec -it hello-python-bazel bash
```
```shell
docker run -it \
-e name=worldboss \
-e age=45 \
-e job=running \
-e num_a=99 \
-e num_b=100 \
hello-python-bazel
```
### Pass ENV file
```shell
docker build -t hello-python-bazel .

docker run -it --env-file env_vars.env hello-python-bazel
```
### Using Docker Compose
```shell
docker-compose up
docker-compose down
```