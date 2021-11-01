from django.contrib import admin
from .models import Question, Choice, Vote

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)

class ReadonlyAdminMixin():
    def has_add_permission(self,request):
        return False
    def has_change_permission(self,*args):
        return False
    def has_delete_permission(self,*args):
        return False
class VoteAdmin(ReadonlyAdminMixin, admin.ModelAdmin):
    list_display= ('voter_name', 'vote_data', 'choice')
admin.site.register(Vote, VoteAdmin)