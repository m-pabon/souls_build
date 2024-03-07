from django.contrib import admin
from .models import Weapon, AttackAttribute, DefenseAttribute, Scaling, RequiredAttribute


class AttackAttributeInline(admin.TabularInline):
    model = AttackAttribute
    extra = 0


class DefenseAttributeInline(admin.TabularInline):
    model = DefenseAttribute
    extra = 0


class ScalingInline(admin.TabularInline):
    model = Scaling
    extra = 0


class RequiredAttributeInline(admin.TabularInline):
    model = RequiredAttribute
    extra = 0


class WeaponAdmin(admin.ModelAdmin):
    inlines = [AttackAttributeInline, DefenseAttributeInline, ScalingInline, RequiredAttributeInline]


# Register the admin class for the Weapon model
admin.site.register(Weapon, WeaponAdmin)
