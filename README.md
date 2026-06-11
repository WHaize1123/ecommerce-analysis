# E-commerce 爬虫数据分析系统

**毕业设计项目**：商务网站数据爬虫的分析应用

## 📋 项目简介

这是一个完整的电商数据爬虫系统，具备以下功能：
- 🔍 多平台电商网站数据爬取
- 📊 产品数据深度分析
- 📈 可视化数据展示
- 💾 多格式数据导出
- 🎨 用户友好的交互界面

## 🎯 核心功能

### 1. 数据采集模块
- 支持多个电商平台爬取
- 异步并发爬虫技术
- 反爬虫机制（User-Agent轮换、请求延迟等）

### 2. 数据分析模块
- 价格统计分析
- 评分评价分析
- 库存状态分析
- 平台对比分析

### 3. 数据可视化
- 价格分布图
- 评分分布图
- 平台对比图

### 4. 数据导出
- CSV 格式
- Excel 格式
- JSON 格式

## 🚀 快速开始

### 环境要求
- Python 3.8+
- pip 包管理器

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行程序

**爬取数据：**
```bash
python main.py scrape --keyword "手机" --limit 50
```

**查询数据库：**
```bash
python main.py query --platform shopee
```

**数据分析：**
```bash
python main.py analyze --input data.json
```

**导出数据：**
```bash
python main.py export --format csv
```

## 📁 项目结构

```
ecommerce-analysis/
├── crawler/                 # 爬虫模块
├── analysis/                # 分析模块
├── database/                # 数据库模块
├── ui/                      # 用户界面
├── config/                  # 配置文件
├── tests/                   # 测试文件
├── main.py                  # 主程序入口
└── requirements.txt         # 依赖包
```

## ⚠️ 免责声明

本项目仅供学习和研究使用。使用时请遵守相关法律法规和网站规则。

## 📄 许可证

MIT License
