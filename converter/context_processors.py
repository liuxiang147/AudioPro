from django.conf import settings

def analytics(request):
    return {
        'analytics_provider': getattr(settings, 'ANALYTICS_PROVIDER', 'none'),
        'analytics_id': getattr(settings, 'ANALYTICS_ID', ''),
        'analytics_host': getattr(settings, 'ANALYTICS_HOST', ''),
        'ai_gateway_key': getattr(settings, 'AI_GATEWAY_KEY', ''),
    }
