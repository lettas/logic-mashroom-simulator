logic-mashroom-simulator
========================


```
$ python3 main.py
```


10000 回試行

```
$ for i in `seq 10000`; do  python3 main.py >> result.txt ; done;
```

集計

```
$ cat result.txt | sort | uniq -c | sort -nr | head
```
