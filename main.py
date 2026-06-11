#!/usr/bin/env python3
"""
E-commerce 爬虫数据分析系统 - 主程序入口

使用方法:
    python main.py scrape --keyword "手机" --limit 50
    python main.py analyze --input data.json
    python main.py query --platform shopee
    python main.py export --format csv
"""

import sys
import argparse
from loguru import logger

from config.settings import LOG_CONFIG, APP_CONFIG
from ui.cli import CLIInterface


def setup_logging():
    """配置日志系统"""
    logger.remove()
    
    logger.add(
        sys.stderr,
        format=LOG_CONFIG['format'],
        level=LOG_CONFIG['level'],
    )
    
    logger.add(
        LOG_CONFIG['file'],
        format=LOG_CONFIG['format'],
        level=LOG_CONFIG['level'],
        rotation="500 MB",
        retention="7 days",
    )


def print_banner():
    """打印应用横幅"""
    banner = f"""
╔══════════════════════��═════════════════════════════════════════════════════════╗
║   E-Commerce 爬虫数据分析系统                                                  ║
║   {APP_CONFIG['name']:<34} ║
║   v{APP_CONFIG['version']:<42} ║
╚════════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def main():
    """主程序入口"""
    setup_logging()
    print_banner()
    
    logger.info(f"应用启动: {APP_CONFIG['name']} v{APP_CONFIG['version']}")
    
    try:
        cli = CLIInterface()
        cli.run()
    
    except KeyboardInterrupt:
        logger.info("应用被用户中断")
        print("\n⚠️  应用已退出")
        sys.exit(0)
    
    except Exception as e:
        logger.error(f"应用错误: {str(e)}", exc_info=True)
        print(f"❌ 发生错误: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
