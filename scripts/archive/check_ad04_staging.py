import json, sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\piyus\.gemini\antigravity\brain\253e6085-f880-4a72-b935-20afe2df40a6\.system_generated\logs\transcript.jsonl'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        obj = json.loads(line)
        content = str(obj.get('content', ''))
        if 'Ad 04' in content and ('PAUSED' in content or 'staged' in content or 'Ads Manager' in content):
            step = obj.get('step_index')
            src = obj.get('source')
            if src == 'MODEL':
                print(f"Step {step}: {content[:300]}...\n---\n")
