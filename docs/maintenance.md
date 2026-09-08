# 个人主页维护指南

## 修改内容

在编辑器中打开整个项目文件夹，不要用 Word 编辑 HTML。保留标签，修改里面的文字；遇到 `&` 请写成 `&amp;`。

| 要修改的内容 | 在 index.html 中搜索 |
| --- | --- |
| 简介、研究方向、邮箱、单位 | `id="about"` |
| 论文 | `id="publications"` |
| 教育与工作经历 | `id="experience"` |
| 项目与专利 | `id="projects"` |
| 荣誉 | `id="honors"` |
| 审稿与教材 | `id="service"` |
| 页脚日期 | `Last update` |

新增论文时复制一整个 `div.item` 块，替换标题、作者、期刊、年份、链接和图片。重点论文放在折叠区前，其他论文放在 `details` 内。完整示例见 [内容模板](content-templates.md)。

作者顺序、通讯作者标记、发表状态和 DOI 以论文原文为准。现有 IF/TOP 标注沿用原站，本次未重新核验；以后请注明指标年份或省略容易过时的数值。原站未明确入职日期和具体职称，本次未补写，确认后可加入简介和经历。

## 图片与附件

- 头像：`assets/images/profile.jpg`；当前论文配图：`paper1.jpg` 至 `paper6.jpg`。
- 新图片用 `2026-short-paper-name.jpg` 这样的名称，小写英文、数字和连字符。
- 公开附件可新建 `assets/files/`；私人资料、未公开论文、原始数据放在仓库之外。
- `null.jpg` 和 `paper7.jpg` 未被首页引用，暂时保留。
- 本次将七张在用图片移到 `assets/images/`，主页引用已更新。如曾分享根目录下的独立图片链接，请改为新地址。

## 一次完整更新

```powershell
cd E:\OneDrive\Github_hub\cf-shi.github.io
git status
git pull --ff-only
```

先确认工作区干净，再拉取远端。编辑内容、修改页脚更新日期，然后检查和预览：

```powershell
python scripts/check_site.py
python -m http.server 8000 --bind 127.0.0.1
```

打开 <http://127.0.0.1:8000>，查看桌面和手机宽度下的图片、导航、折叠区及论文链接。工具仅检查本地资源、锚点和基础结构，不检查外部链接可用性，也不核实学术信息。结束预览按 `Ctrl+C`。

```powershell
git diff --check
git diff
git status
git add index.html assets docs README.md
git diff --cached --stat
git commit -m "Update publications and academic profile"
git push origin main
```

只暂存准备公开的文件；若修改工具或配置，按文件名补充 `git add`。没有改动时无需提交。

推送后查看 GitHub 仓库的 **Actions**，等 Pages 构建成功，再访问 <https://cf-shi.github.io/>。部署可能需要几分钟，必要时强制刷新。沿用原仓库 Pages 设置；未来若重新设置，分支发布源应为 `main` 和 `/(root)`，不要改成仅有维护文档的 `/docs`。

## 网络与冲突

第一次下载用 `git clone`，已有仓库以后用 `git pull`，不要反复下载 ZIP 或建立“最终版”副本。

此电脑本次通过本地代理 `127.0.0.1:7897` 连通 GitHub，并使用 OpenSSL 解决 Windows TLS 凭据错误。普通命令不能连通时，可使用下列单次设置（不修改全局配置）：

```powershell
git -c http.proxy=http://127.0.0.1:7897 -c http.sslBackend=openssl pull --ff-only
git -c http.proxy=http://127.0.0.1:7897 -c http.sslBackend=openssl push origin main
```

仅在代理正在运行且端口仍为 7897 时使用。若需要认证，按 Git 凭据管理器正规登录提示操作，不要把密码或令牌写入仓库或聊天。

如果拉取或推送提示分支分叉、远端有更新，先查看 `git status`，请助手协助合并，不要 `push --force`。

## 回退与改版

用 `git log --oneline -10` 查看历史。需要撤销已发布提交时，在工作区干净的前提下用 `git revert 提交编号`，解决可能的冲突后再推送。它会新增撤销记录并保留历史。执行前确认提交编号，不确定时请助手协助。

较大改版先运行 `git switch -c redesign-homepage`，预览验证后再合并到 `main`。Git 已记录版本，不需要 `index-final-v2.html`。

## 逐步扩展

1. 现在优先保持简介、方向、代表论文和联系方式准确。
2. 有新成果时增加 News，按年月倒序；首页放最近几条，旧记录折叠或归档。
3. 有实际教学与指导记录时，再增加 Teaching / Students，写明年度和本人职责。
4. 内容较多后，将完整论文和历年动态拆成独立页面；需要多页统一模板时再考虑静态网站生成器。

长期参考 [谢再鹏主页](https://zach82.github.io/) 的年度动态和成果积累方式，当前延续 [方双康](https://sk-fun.fun/) 的图文论文展示，以及 [刘天润](https://trliu-hhu.github.io/) 的简介与代表成果优先顺序。
