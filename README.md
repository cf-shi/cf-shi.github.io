# Chunfeng Shi · 个人学术主页

网站：<https://cf-shi.github.io/>

仓库：<https://github.com/cf-shi/cf-shi.github.io>

纯 HTML 和 CSS 静态主页，无需安装前端框架或编译，关闭 JavaScript 也能浏览。

## 维护入口

| 内容 | 文件 |
| --- | --- |
| 简介、论文、经历、项目、荣誉、学术活动 | `index.html` |
| 字体、间距、颜色、手机排版 | `assets/css/style.css` |
| 头像和论文图片 | `assets/images/` |
| 日常更新、发布和回退说明 | [中文维护指南](docs/maintenance.md) |
| 论文、动态、教学模板 | [内容模板](docs/content-templates.md) |
| 本地资源与结构检查 | `scripts/check_site.py` |

根目录的 `null.jpg` 和 `paper7.jpg` 是原站未引用图片，暂时保留，避免误删可能在别处使用的素材。

## 本地预览

可以直接双击 `index.html`，也可以在本仓库文件夹运行：

```powershell
python scripts/check_site.py
python -m http.server 8000 --bind 127.0.0.1
```

浏览器打开 <http://127.0.0.1:8000>，结束预览按 `Ctrl+C`。
