from django.contrib import admin
from .models import Profile, Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "title")   # id va nomini ko‘rsatadi
    search_fields = ("title",)       # qidiruv
    ordering = ("id",)               # tartib bo‘yicha


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "users", "phone", "birth_date"
    )  # admin jadvalida ko‘rinadigan ustunlar
    list_filter = ("users", "birth_date")  # chap tomonda filter
    search_fields = ("user__username", "phone", "address")  # qidiruv
    ordering = ("id",)   # default tartib
    readonly_fields = ("avatar_preview",)  # rasmni faqat ko‘rsatish

    fieldsets = (
        ("Asosiy ma’lumotlar", {
            "fields": ("user", "users", "bio", "birth_date")
        }),
        ("Qo‘shimcha ma’lumotlar", {
            "fields": ("phone", "address")
        }),
        ("Avatar", {
            "fields": ("avatar", "avatar_preview")
        }),
    )

    def avatar_preview(self, obj):
        if obj.avatar:
            return f"<img src='{obj.avatar.url}' width='80' style='border-radius:10px;' />"
        return "Rasm yo‘q"
    avatar_preview.allow_tags = True
    avatar_preview.short_description = "Avatar ko‘rinishi"



from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("ism", "yosh", "telefon", "email")
    search_fields = ("ism", "email", "telefon")
