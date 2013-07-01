from django.contrib import admin
from django.contrib.contenttypes import generic
from extractionAPI.models import *


class ImageAdmin(admin.ModelAdmin):
	fieldsets = [
		('Photo', {'fields':['image']}),
		# ('Photo', {'fields':['image', 'width', 'height']}),
		('Photo Data', {'fields':['caption', 'photo_credit']}),
		('Date Taken', {'fields':['dateTaken']}),
	]

class ImageInline(admin.StackedInline):
	model = Image

	fieldsets = [
	('Photo', {'fields':['image']}),
	# ('Photo', {'fields':['image', 'width', 'height']}),
	('Photo Data', {'fields':['caption', 'photo_credit']}),
	('Date Taken', {'fields':['dateTaken']}),
	]

	extra = 1

class SlideInline(admin.StackedInline):
	
	model = Slide
	extra = 1
	radio_fields = {'typeOfSlide':admin.HORIZONTAL}


class SlideAdmin(admin.ModelAdmin):

	inlines = [ImageInline]



class StoryAdmin(admin.ModelAdmin):
	
	fieldsets = [
		('New Story', {'fields':['headline']}),
		('Cover Photo', {'fields':['coverPhoto']}),
		('Author' , {'fields':['author_firstName','author_lastName']}),
		('Tags', {'fields':['storyTags']}),
	]

	inlines = [SlideInline]


admin.site.register(Story, StoryAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Tag_Type)
admin.site.register(Slide_Types)

