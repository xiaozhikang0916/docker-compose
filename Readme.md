一个docker-compose来启动aria需要的所有东西

包括nginx, BGmi, bgmi_http aria2 aria2ng

clone本项目到本地, 然后运行

```bash
python bootstrap.py
```

在


运行, 构建和运行镜像.

```bash
docker-compose up
 ```

所有持久化的数据会储存在`./data`文件夹中


