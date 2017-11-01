from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='MyTestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charfield', models.CharField(max_length=255)),
                ('datefield', models.DateField()),
                ('datetimefield', models.DateTimeField()),
                ('decimalfield', models.DecimalField(decimal_places=2, max_digits=10)),
                ('floatfield', models.FloatField()),
                ('integerfield', models.IntegerField()),
                ('timefield', models.TimeField()),
                ('uuidfield', models.UUIDField()),
            ],
        ),
    ]
