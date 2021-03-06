# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-23 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='课程名')),
                ('is_banner', models.BooleanField(default=False, verbose_name='是否轮播')),
                ('desc', models.CharField(max_length=520, verbose_name='课程描述')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('degree', models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=10, verbose_name='难度')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟数)')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('category', models.CharField(max_length=20, verbose_name='课程类别')),
                ('you_need_know', models.CharField(default='一颗勤学的心和坚持不懈的精神是本课程必要前提', max_length=500, verbose_name='课程须知')),
                ('teacher_tell', models.CharField(default='按时交作业,不然叫家长', max_length=300, verbose_name='老师告诉你')),
                ('tag', models.CharField(max_length=15, verbose_name='课程标签')),
                ('course_img', models.ImageField(upload_to='course/%Y/%m', verbose_name='课程封面')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('course_org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='所属机构')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='讲师')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='名称')),
                ('download', models.FileField(upload_to='course/resourse/%Y/%m', verbose_name='资源文件')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '课程资源',
                'verbose_name_plural': '课程资源',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='章节名')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='视频名')),
                ('url', models.CharField(default='https://www.cnblogs.com/Tridents/', max_length=100, verbose_name='访问地址')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长(分钟数)')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Lesson', verbose_name='章节')),
            ],
            options={
                'verbose_name': '章节视频',
                'verbose_name_plural': '章节视频',
            },
        ),
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'indexes': [],
                'verbose_name': '轮播课程',
                'proxy': True,
                'verbose_name_plural': '轮播课程',
            },
            bases=('course.course',),
        ),
    ]
