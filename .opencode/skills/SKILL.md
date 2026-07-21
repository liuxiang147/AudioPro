---
name: audiopro
description: AudioPro Django web app — online audio converter, extractor, trimmer, and metadata viewer. I maintain and improve this project.
---

# AudioPro

Django 项目，一个在线的音频转换 & 提取工具，纯前端 ffmpeg.wasm 处理，文件不上传服务器。

## 项目结构

```
audiopro/
├── audiopro/                  # Django 项目配置
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── converter/                 # 主应用
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── converter/
│           └── index.html     # 音频工具页面（含 CSS + JS + AI 助手）
├── requirements.txt           # django>=4.2
├── runtime.txt                # python-3.11
├── vercel.json                # Vercel 部署配置
├── manage.py
└── .opencode/skills/SKILL.md  # 本文件
```

## 部署

GitHub: https://github.com/liuxiang147/AudioPro
Vercel 自动部署，Framework 选 Django。

## 修改指南

- 前端逻辑都在 `index.html` 里（单页应用）
- Django 只做页面路由和 API 端点
- 加新功能时改 `index.html` 的 JS + 对应 UI 即可
- 修改后 `git push`，Vercel 自动重新部署
