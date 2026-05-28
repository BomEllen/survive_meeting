import os
import json
import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import ConversionLog

TONE_LABELS = {
    'soft': '부드럽게',
    'firm': '단호하게',
    'boss': '상사 앞 버전',
    'official': '회의록에 남겨도 되는 버전',
}

TONE_PROMPTS = {
    'soft': '갈등 없이 부드럽고 배려 있게, 상대방 감정을 존중하면서',
    'firm': '단호하고 명확하게, 프로답고 논리적으로',
    'boss': '상사 앞에서 예의 바르고 공손하게, 능력 있어 보이도록',
    'official': '공식 회의록에 남겨도 될 만큼 격식 있고 중립적으로',
}

def calculate_scores(input_text):
    import random
    danger_words = ['짜증', '화나', '싫어', '왜 나만', '말도 안 돼', '미치겠', '개같은']
    danger_count = sum(1 for w in danger_words if w in input_text)
    inner_preservation = max(30, min(95, 70 + random.randint(-10, 15) - danger_count * 5))
    safety = max(40, min(99, 80 + random.randint(-5, 15) - danger_count * 8))
    survival = max(35, min(98, 75 + random.randint(-10, 20) - danger_count * 3))
    return {
        'inner_preservation': inner_preservation,
        'safety': safety,
        'survival': survival,
    }

def convert_with_gemini(input_text, tone):
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        raise Exception('GEMINI_API_KEY 환경변수가 설정되지 않았습니다.')

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    tone_desc = TONE_PROMPTS.get(tone, TONE_PROMPTS['soft'])

    prompt = f"""당신은 직장인의 속마음을 회의에서 말할 수 있는 정중한 비즈니스 표현으로 바꿔주는 전문가입니다.

아래 속마음을 [{tone_desc}] 말투로 회의에서 실제로 쓸 수 있는 문장 3개로 변환해주세요.

규칙:
- 반드시 한국어로 작성
- 각 문장은 실제 회의에서 바로 쓸 수 있어야 함
- 원래 말하려는 핵심 의도는 유지할 것
- 공격적이거나 감정적인 표현은 제거할 것
- 번호나 설명 없이 문장만 3개 출력 (줄바꿈으로 구분)

속마음: {input_text}

변환 결과 (3개, 줄바꿈으로 구분):"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    lines = [l.strip() for l in text.split('\n') if l.strip()]
    # 번호 제거 (1. 2. 3. 또는 - 로 시작하는 경우)
    cleaned = []
    for line in lines:
        if line and line[0].isdigit() and len(line) > 2 and line[1] in '.):':
            line = line[2:].strip()
        elif line.startswith('- '):
            line = line[2:].strip()
        if line:
            cleaned.append(line)

    return cleaned[:3] if cleaned else [text]


def index(request):
    return render(request, 'converter/index.html')


@csrf_exempt
@require_POST
def convert(request):
    try:
        data = json.loads(request.body)
        input_text = data.get('text', '').strip()
        tone = data.get('tone', 'soft')

        if not input_text:
            return JsonResponse({'error': '텍스트를 입력해주세요.'}, status=400)

        if tone not in TONE_LABELS:
            tone = 'soft'

        results = convert_with_gemini(input_text, tone)
        scores = calculate_scores(input_text)

        ConversionLog.objects.create(
            input_text=input_text,
            tone=tone,
            result_1=results[0] if len(results) > 0 else '',
            result_2=results[1] if len(results) > 1 else '',
            result_3=results[2] if len(results) > 2 else '',
        )

        return JsonResponse({
            'results': results,
            'tone_label': TONE_LABELS[tone],
            'scores': scores,
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
