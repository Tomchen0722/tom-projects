"""路由層。web=後台網頁,api=JSON API,line_bp=LINE webhook 與員工自助頁。"""

from .web import bp as web_bp
from .api import bp as api_bp
from .line_bp import bp as line_bp

__all__ = ["web_bp", "api_bp", "line_bp"]
