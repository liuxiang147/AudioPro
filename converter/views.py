from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'converter/index.html')

def health(request):
    return JsonResponse({'status': 'ok', 'app': 'AudioPro'})

def og_image(request):
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0a0a12"/>
      <stop offset="100%" style="stop-color:#1a0a2e"/>
    </linearGradient>
    <linearGradient id="title" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ff2d95"/>
      <stop offset="100%" style="stop-color:#8b5cf6"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <text x="600" y="280" font-family="system-ui, sans-serif" font-size="72" font-weight="700" fill="url(#title)" text-anchor="middle">AudioPro 工具箱</text>
  <text x="600" y="350" font-family="system-ui, sans-serif" font-size="28" fill="#a78bfa" text-anchor="middle">在线音频转换 · 提取 · 裁剪 · 元数据</text>
  <rect x="360" y="390" width="480" height="40" rx="8" fill="none" stroke="rgba(139,92,246,.3)" stroke-width="1"/>
  <text x="600" y="417" font-family="system-ui, sans-serif" font-size="16" fill="#666" text-anchor="middle">MP3 · WAV · FLAC · OGG · AAC · M4A · Opus</text>
  <text x="600" y="490" font-family="system-ui, sans-serif" font-size="14" fill="#444" text-anchor="middle">所有处理在浏览器本地完成 · 文件不上传服务器</text>
</svg>'''
    return HttpResponse(svg, content_type='image/svg+xml; charset=utf-8')
