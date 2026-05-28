from django.db import models


class ConversionLog(models.Model):
    TONE_CHOICES = [
        ('soft', '부드럽게'),
        ('firm', '단호하게'),
        ('boss', '상사 앞 버전'),
        ('official', '회의록에 남겨도 되는 버전'),
    ]

    input_text = models.TextField(verbose_name='입력한 속마음')
    tone = models.CharField(max_length=20, choices=TONE_CHOICES, verbose_name='선택한 말투')
    result_1 = models.TextField(verbose_name='변환 결과 1')
    result_2 = models.TextField(blank=True, verbose_name='변환 결과 2')
    result_3 = models.TextField(blank=True, verbose_name='변환 결과 3')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='변환일시')

    class Meta:
        verbose_name = '변환 이력'
        verbose_name_plural = '변환 이력 목록'
        ordering = ['-created_at']

    def __str__(self):
        return f'[{self.get_tone_display()}] {self.input_text[:30]}'


class ConversionTemplate(models.Model):
    TONE_CHOICES = [
        ('soft', '부드럽게'),
        ('firm', '단호하게'),
        ('boss', '상사 앞 버전'),
        ('official', '회의록에 남겨도 되는 버전'),
    ]

    name = models.CharField(max_length=100, verbose_name='템플릿 이름')
    keywords = models.CharField(max_length=500, verbose_name='키워드 (쉼표로 구분)', help_text='예: 왜,굳이,어떻게')
    tone = models.CharField(max_length=20, choices=TONE_CHOICES, verbose_name='말투')
    result_1 = models.TextField(verbose_name='변환 결과 1')
    result_2 = models.TextField(verbose_name='변환 결과 2', blank=True)
    result_3 = models.TextField(verbose_name='변환 결과 3', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        verbose_name = '변환 템플릿'
        verbose_name_plural = '변환 템플릿 목록'

    def __str__(self):
        return f'[{self.get_tone_display()}] {self.name}'

    def get_keywords_list(self):
        return [k.strip() for k in self.keywords.split(',') if k.strip()]
