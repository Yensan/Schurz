from django.contrib import admin
from .models import *
admin.site.register(FamousPeople)
class PeopleInline(admin.StackedInline):
    model = FamousPeople
    extra = 3
class BookAdmin(admin.ModelAdmin):
    # 查询页面的效果
    list_display = ['id','title','pubDate'] # 显示哪些信息
    list_filter = ['pubDate'] # 根据哪些字段过滤
    search_fields = ['title'] # 根据哪些字段搜索
    list_per_page = 7 # 分页条数
    # 添加和修改页面的效果
    fieldsets = [('base', {'fields':['title']}),
                 ('time', {'fields':['pubDate']})] # 分组
    inlines = [PeopleInline, ] # 添加时自动嵌入
admin.site.register(Book, BookAdmin)
