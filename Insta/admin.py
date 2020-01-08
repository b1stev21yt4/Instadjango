from django.contrib import admin

from Insta.models import Post, PostTwo, InstaUser, Like, Comment, UserConnection


class FollowingInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'creator'

class FollowerInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'following'

# class PostAdmin(admin.ModelAdmin):
#     inlines = [
#         CommentInline,
#         LikeInline,
#     ]

class UserAdmin(admin.ModelAdmin):
    inlines = [
        FollowerInline,
        FollowingInline,
    ]
# Register your models here.
admin.site.register(Post)
admin.site.register(PostTwo)
admin.site.register(InstaUser, UserAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(UserConnection)
