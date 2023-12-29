# BandWallBackend

> 要求：Python 3.10+

搭建：
`pip install fastapi pydantic tinydb "uvicorn[standard]"`

激活虚拟环境：
`conda activate py310`

运行：
`uvicorn main:app --reload`

后台运行：`sudo vim /etc/rc.local` 末尾添加

```
su - liang -c "cd /home/liang/BandWallBackend/ && nohup /home/liang/miniconda3/envs/py310/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --reload  > log.txt 2>&1 &"
```

查看端口占用（应该有两个，一个uvicorn一个python进程）：
`lsof -i:8000`

停止：
把占用端口的程序的PID给杀掉就行
`kill -9 123123`
