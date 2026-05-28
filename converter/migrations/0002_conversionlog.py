from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('converter', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='ConversionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_text', models.TextField(verbose_name='입력한 속마음')),
                ('tone', models.CharField(choices=[('soft', '부드럽게'), ('firm', '단호하게'), ('boss', '상사 앞 버전'), ('official', '회의록에 남겨도 되는 버전')], max_length=20, verbose_name='선택한 말투')),
                ('result_1', models.TextField(verbose_name='변환 결과 1')),
                ('result_2', models.TextField(blank=True, verbose_name='변환 결과 2')),
                ('result_3', models.TextField(blank=True, verbose_name='변환 결과 3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='변환일시')),
            ],
            options={'verbose_name': '변환 이력', 'verbose_name_plural': '변환 이력 목록', 'ordering': ['-created_at']},
        ),
    ]
