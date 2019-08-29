# 引入admin模块
from django.contrib import admin
# 引入数据模型类
from .models import Article

#显示其他字段
class ArticleAdmin(admin.ModelAdmin):
    '''
    创建ArticleAdmin类，继承于admin.ModelAdmin
    '''
    list_display = ('title','content','pub_time')       # 配置展示列表
    # 配置过滤器，在右侧过滤框
    list_filter = ('pub_time',)  #元祖一个元素时候注意最后加一个逗号 ！区别
    # 配置可搜索的字段，在上头搜索栏
    search_fields = ('content',)
    # 配置只读字段
    readonly_fields = ('pub_time',)

    # fieldsets = [
    #     (None, {'fields': ['title','content']}),
    #     ('Date information', {'fields': ['pub_time']}),
    # ]

# 绑定 Article 模型到 ArticleAdmin 管理后台
admin.site.register(Article,ArticleAdmin)
