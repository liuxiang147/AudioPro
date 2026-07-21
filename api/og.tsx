import { ImageResponse } from '@vercel/og';

export const config = { runtime: 'edge' };

export default async function handler() {
  return new ImageResponse(
    (
      <div
        style={{
          height: '100%',
          width: '100%',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          background: 'linear-gradient(135deg, #0a0a12 0%, #1a0a2e 100%)',
          fontFamily: '"Segoe UI", system-ui, sans-serif',
        }}
      >
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '60px 80px',
            textAlign: 'center',
          }}
        >
          <div
            style={{
              fontSize: 72,
              fontWeight: 700,
              background: 'linear-gradient(90deg, #ff2d95, #8b5cf6)',
              backgroundClip: 'text',
              color: 'transparent',
              marginBottom: 16,
              lineHeight: 1.2,
            }}
          >
            AudioPro 工具箱
          </div>
          <div
            style={{
              fontSize: 28,
              color: '#a78bfa',
              marginBottom: 40,
              letterSpacing: 2,
            }}
          >
            在线音频转换 · 提取 · 裁剪 · 元数据
          </div>
          <div
            style={{
              display: 'flex',
              gap: 16,
              fontSize: 16,
              color: '#666',
            }}
          >
            <span style={{ padding: '8px 16px', border: '1px solid rgba(139,92,246,.3)', borderRadius: 8 }}>
              MP3 · WAV · FLAC · OGG · AAC · M4A · Opus
            </span>
          </div>
          <div
            style={{
              marginTop: 40,
              fontSize: 14,
              color: '#444',
            }}
          >
            所有处理在浏览器本地完成 · 文件不上传服务器
          </div>
        </div>
      </div>
    ),
    {
      width: 1200,
      height: 630,
    },
  );
}
