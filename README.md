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