一个docker-compose来启动aria需要的所有东西

包括nginx, BGmi, bgmi_http aria2 aria2ng

不再需要安装python和bgmi到本地

如果你已经有一个nginx在运行, 可以去掉compose中的nginx,
参照[nginx.conf](nginx/conf.d/nginx.conf)

clone本项目到本地, 然后运行

```bash
git clone https://github.com/BGmi/docker-compose.git bgmi
cd bgmi
python bootstrap.py
```
会自动运行所有镜像, 访问localhost:8888即可看到web页面

在`.env`文件生成和ariang下载完成后, 不再需要`bootstrap.py`,
而是跟普通的compose一样使用`docker-compose up`来启动docker-compose.

在本文件夹内使用`docker-compose run bgmi`来代替`bgmi`命令

**如果你修改了设置, 仍然需要通过`docker-compose restart`重启bgmi_http来让修改生效. **

所有的文件会以当前的uid和gid进行写入

## 修改设置

在运行过`bootstrap.py`后会在当前文件夹下新建一个`.env`文件,
可以修改`PORT`来修改nginx最终监听的端口

所有持久化的数据会储存在`./data`文件夹中, 番剧默认会位于
`./data/bangumi` 如果你需要修改番剧保存地址可以直接修改
`docker-compose.yml#services.bgmi.volumes`, 把对应的路径挂载到`/bgmi/bangumi`

## todo

还没找到一个好办法来运行定时任务, 比如更新aria2c的tracker列表, 
调用`bgmi update -d`来下载番剧

所以请手动添加这些命令到宿主机的crontab中.

```crontab
0 */2 * * *  cd /path/to/bgmi; /path/to/docker-compose run bgmi update -d
0 */12 * * *  cd /path/to/bgmi; /path/to/docker-compose run bgmi cal --force-update --download-cover
```