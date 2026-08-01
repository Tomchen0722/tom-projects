"""圖表工具：統一 Plotly 樣式，並處理 matplotlib 中文字型。"""

import matplotlib
import numpy as np
import plotly.graph_objects as go

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from .ui import C, PLOT_COLORS  # noqa: E402

# Windows 上的中文字型，避免圖裡出現豆腐方塊
matplotlib.rcParams["font.sans-serif"] = [
    "Microsoft JhengHei", "Microsoft YaHei", "PingFang TC", "DejaVu Sans",
]
matplotlib.rcParams["axes.unicode_minus"] = False


def style(fig: go.Figure, height: int = 380, **kwargs) -> go.Figure:
    """套用統一的 Plotly 版面：透明背景、淡格線、跟著深淺色模式走。"""
    fig.update_layout(
        height=height,
        margin=dict(l=50, r=20, t=45, b=45),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(size=13),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
        colorway=PLOT_COLORS,
        **kwargs,
    )
    fig.update_xaxes(gridcolor=C["grid"], zerolinecolor=C["grid"])
    fig.update_yaxes(gridcolor=C["grid"], zerolinecolor=C["grid"])
    return fig


def line(x, ys: dict, title="", xlab="", ylab="", height=380) -> go.Figure:
    """折線圖。ys 是 {圖例名稱: y 陣列}。"""
    fig = go.Figure()
    for name, y in ys.items():
        fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name=name, line=dict(width=3)))
    fig.update_layout(title=title, xaxis_title=xlab, yaxis_title=ylab)
    return style(fig, height)


def heatmap(z, x=None, y=None, title="", colorscale="Blues", height=380,
            text=None, zmin=None, zmax=None) -> go.Figure:
    """熱圖：注意力權重、混淆矩陣、卷積核都用它。"""
    fig = go.Figure(
        go.Heatmap(
            z=z, x=x, y=y, colorscale=colorscale, zmin=zmin, zmax=zmax,
            text=text, texttemplate="%{text}" if text is not None else None,
            textfont=dict(size=13),
        )
    )
    fig.update_layout(title=title)
    fig.update_yaxes(autorange="reversed")
    return style(fig, height)


def image_grid(images, titles, cmap="gray", cols=None):
    """用 matplotlib 畫一排圖片（CNN 章節用）。回傳 figure。"""
    n = len(images)
    cols = cols or n
    rows = int(np.ceil(n / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(3.1 * cols, 3.3 * rows))
    axes = np.atleast_1d(axes).ravel()
    for ax, img, t in zip(axes, images, titles):
        ax.imshow(img, cmap=cmap)
        ax.set_title(t, fontsize=11)
        ax.axis("off")
    for ax in axes[n:]:
        ax.axis("off")
    fig.patch.set_alpha(0)
    fig.tight_layout()
    return fig
