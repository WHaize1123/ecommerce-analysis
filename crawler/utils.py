#!/usr/bin/env python3
"""
爬虫工具函数
"""

import random
import time
from typing import List
from config.settings import CRAWLER_CONFIG


def get_random_user_agent() -> str:
    """
    获取随机User-Agent
    
    Returns:
        User-Agent字符串
    """
    return random.choice(CRAWLER_CONFIG['user_agents'])


def delay_request(min_delay: float = None, max_delay: float = None) -> None:
    """
    请求延迟 - 避免被识别为爬虫
    
    Args:
        min_delay: 最小延迟(秒)
        max_delay: 最大延迟(秒)
    """
    if min_delay is None:
        min_delay = CRAWLER_CONFIG['delay_between_requests']
    if max_delay is None:
        max_delay = CRAWLER_CONFIG['delay_between_requests'] + 3
    
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)


def format_price(price_str: str) -> float:
    """
    格式化价格字符串为浮点数
    
    Args:
        price_str: 价格字符串
        
    Returns:
        浮点数价格
    """
    try:
        cleaned = price_str.replace('¥', '').replace('$', '').replace(',', '').strip()
        return float(cleaned)
    except:
        return 0.0


def format_rating(rating_str: str) -> float:
    """
    格式化评分字符串为浮点数
    
    Args:
        rating_str: 评分字符串
        
    Returns:
        浮点数评分
    """
    try:
        import re
        match = re.search(r'\d+\.?\d*', rating_str)
        if match:
            return float(match.group())
    except:
        pass
    return 0.0
