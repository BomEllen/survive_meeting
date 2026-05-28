from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='ConversionTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='템플릿 이름')),
                ('keywords', models.CharField(help_text='예: 왜,굳이,어떻게', max_length=500, verbose_name='키워드 (쉼표로 구분)')),
                ('tone', models.CharField(choices=[('soft', '부드럽게'), ('firm', '단호하게'), ('boss', '상사 앞 버전'), ('official', '회의록에 남겨도 되는 버전')], max_length=20, verbose_name='말투')),
                ('result_1', models.TextField(verbose_name='변환 결과 1')),
                ('result_2', models.TextField(blank=True, verbose_name='변환 결과 2')),
                ('result_3', models.TextField(blank=True, verbose_name='변환 결과 3')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
            ],
            options={'verbose_name': '변환 템플릿', 'verbose_name_plural': '변환 템플릿 목록'},
        ),
    ]
