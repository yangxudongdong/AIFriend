from django.contrib import admin
from web.models.user import UserProfile
from web.models.character import Character
from web.models.friend import Friend, Message


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',) #逗号不能删，否则这里会被解析成一个元素，而不是一个列表（实际上应该是一个列表）
# Register your models here.

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    raw_id_fields = ('author',)

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    raw_id_fields = ('me', 'character',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    raw_id_fields = ('friend',)
