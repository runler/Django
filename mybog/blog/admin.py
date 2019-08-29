from django.contrib import admin

from .models import Article

#显示其他字段
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')
    #过滤器
    list_filter = ('pub_time',)  #元祖一个元素时候注意最后加一个逗号 ！区别

    # fieldsets = [
    #     (None, {'fields': ['title','content']}),
    #     ('Date information', {'fields': ['pub_time']}),
    # ]


admin.site.register(Article,ArticleAdmin)
