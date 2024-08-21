from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from blog.models import Category, Post, Comment, Contact, Tag, Profile

class PostAdmin(admin.ModelAdmin):
    list_display=('display_title', 'author', 'category', 'is_published', 'created_at', 'updated_at','display_tags_count', 'display_actions')
    list_filter=('is_published','category', 'tags')
    list_editable=('is_published',)
    # list_per_page=1
    list_max_show_all = 100
    search_fields = ('title',)

    def display_tags_count(self, post):
        return post.tags.count()
    
    def display_actions(self, post):
        return format_html(
                        '<a href="{}" class="addLink">Voir</a>&nbsp;'
                        '<a href="{}" class="addLink">Editer</a>&nbsp;'
                        '<a href="{}" class="addLink">Supprimer</a>&nbsp;',
                        reverse("admin:blog_post_change", args=[post.id]),
                        reverse("admin:blog_post_change", args=[post.id]),
                        reverse("admin:blog_post_delete", args=[post.id]),
                        )
    
    display_tags_count.short_description = "tags count"
    display_actions.short_description = "Actions"

    def display_title(self, post):
        no_icon = '<img src="/public/admin/img/icon-no.svg" alt="False">'
        yes_icon = '<img src="/public/admin/img/icon-yes.svg" alt="True">'

        if post.is_published:
            title = '<span style="color:green;">'+ post.title + '</span>'
            return format_html(yes_icon +' '+ title)
        else:
            title = '<span style="color:red;">'+ post.title + '</span>'
            return format_html(no_icon +' '+ title)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

class ContactAdmin(admin.ModelAdmin):
    list_display=('civility', 'name', 'email', 'subject')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Profile)