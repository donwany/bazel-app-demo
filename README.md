### Run and Build
```shell
cd absl-demo

bazel build :app
```
```shell
cd absl-demo

bazel run :app
```
```shell
bazel run :hello -- \
  --age=45 \
  --job='running'
```
```shell
nohup bazel run :hello -- \
  --age=45 \
  --job='running' &
```
```shell
nohup bazel run :hello -- \
  --age=45 \
  --job='running' \
  --num_a=45 \
  --num_b=99 &
```

```python
python hello.py --age=99 --job='stopped'
```