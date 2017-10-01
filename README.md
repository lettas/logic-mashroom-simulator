logic-mashroom-simulator
========================


```sh
$ python3 main.py
```


10000 回試行

```sh
$ for i in `seq 10000`; do  python3 main.py >> result.txt ; done;
```

集計

```sh
$ cat result.txt | sort | uniq -c | sort -nr | head
```
