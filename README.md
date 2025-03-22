# Tokyo Power Network Visualization

这是一个基于 Leaflet 的 GIS 可视化项目，用于展示东京地区的输电网络，包括变电站和线路。

## 功能
- 显示变电站和输电线路的地理位置。
- 支持鼠标交互，显示线路的起点和终点坐标。
- 从 SQLite 数据库动态刷新数据。
- 使用 Flask 提供后端 API。

## 项目结构
- `index.html`：前端页面，使用 Leaflet 渲染地图。
- `network.geojson`：初始的 GeoJSON 数据文件。
- `server.py`：Flask 后端服务，从 SQLite 数据库读取数据。
- `.gitignore`：忽略数据库文件和临时文件。

## 安装与运行
### 前端
1. 安装 VSCode 和 Live Server 插件。
2. 打开 `index.html`，右键选择“Open with Live Server”。

### 后端
1. 安装 Python 3.x 和依赖：
   ```bash
   pip install flask flask-cors
2. 运行后端服务：
   ```bash
   python server.py

## 数据库
- 需要 power_network.db 文件（未包含在仓库中），可通过脚本从 network.geojson 生成。

## 技术栈
- 前端：Leaflet,/HTML, JavaScript
- 后端：Flask, SQLite
- 数据格式：GeoJSON

## 下一步计划
- 添加数据编辑功能
- 支持线路删选和动态更新

## 贡献
- By Grok
- 欢迎提交 Issues 或 Pull Requests！
