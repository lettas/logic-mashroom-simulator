logic-mashroom-simulator
========================


```sh
$ python3 main.py
```


10000 回試行

```sh
$ python3 main.py 10000 > result.txt
```

集計

```sh
$ cat result.txt | sort | uniq -c | sort -nr | head
```
