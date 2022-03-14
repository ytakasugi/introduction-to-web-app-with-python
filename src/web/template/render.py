import os

import settings

def render(template_name: str, context: dict):
    template_path = os.path.join(settings.TEMPLATE_DIR, template_name)

    with open(template_path) as f:
        template = f.read()
        
    # 可変長の返り値を返す。型は`dict`型
    return template.format(**context)