# 内容模板

先把全部占位文字替换为真实信息，再复制到 `index.html` 对应位置。此文件不会自动显示在主页。

## 论文

重点论文放在 Publications 的 `details` 之前，其余放入折叠区。没有配图时删除整个 `item-img` 块。

```html
<div class="item">
  <div class="item-img">
    <img src="assets/images/2026-paper-short-name.jpg"
         alt="研究方法或结果的简短说明" loading="lazy">
  </div>
  <div class="item-content">
    <div class="title">论文完整标题</div>
    <div class="authors"><strong>Chunfeng Shi</strong>, 其他作者.</div>
    <div class="venue">期刊或会议名称, 年份</div>
    <div class="links">
      <a href="https://doi.org/替换为真实DOI" target="_blank" rel="noopener noreferrer">[Paper Link]</a>
    </div>
  </div>
</div>
```

## 动态

有实际进展后，在简介后、论文前添加此栏目，并在导航加上 `<a href="#news">News</a>`。

```html
<section id="news">
  <h2>News</h2>
  <ul class="timeline">
    <li><strong>YYYY-MM:</strong> 已确认的学术动态。</li>
  </ul>
</section>
```

## 教学

确认任课信息后，在 `</main>` 前添加栏目，并在导航加上 `<a href="#teaching">Teaching</a>`。

```html
<section id="teaching">
  <h2>Teaching</h2>
  <ul class="timeline">
    <li><strong>学年与学期:</strong> 课程名称、课程对象和本人职责。</li>
  </ul>
</section>
```
