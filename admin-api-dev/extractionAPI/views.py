from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from extractionAPI.models import *	# import the models in the models.py file for the app

import json, collections

@require_http_methods(["GET", "POST"])


#cached_stories = Story.objects.all()
#cached_slides = Slide.objects.all()


def index(request):
	return HttpResponse("<h3>This is the Index.</h3>")

def test(request):
	return HttpResponse("<h3>You're at the API Call!</h3>");


def get_all_stories(request):
	
	stories = []

	for story in Story.objects.all():
		storyObj = get_story_object(story)
		stories.append(storyObj)

	jsonString = json.dumps(stories)

	return HttpResponse(jsonString, mimetype='application/json')



def get_story_object(story):
	storyObj = collections.OrderedDict()
	storyObj['story_id'] = story.story_id
	storyObj['headline'] = story.headline
	storyObj['author'] = story.author_firstName + ' ' + story.author_lastName
	#storyObj['date-created'] = story.timeCreated

	# Compile data about the coverphoto and include it as an entry
	coverphotoInfo = collections.OrderedDict()
	coverphotoInfo['url'] = story.coverPhoto.url
	coverphotoInfo['width'] = story.coverPhoto.width
	coverphotoInfo['height'] = story.coverPhoto.height
	storyObj['coverPhoto'] = coverphotoInfo

	tagList = []
	for tag in story.storyTags.all():	#	the all() function gets all the elements for the field which is m2m
		tagList.append(str(tag))
	storyObj['Tags'] = tagList


	storyObj['slides'] = get_slides_for_story(story.story_id)	

	return storyObj	



def get_slides_for_story(story_id):

	slides = []
	slidesInStory = Slide.objects.filter(story=str(story_id))
	
	for slide in slidesInStory:
		slideObj = get_slide_object(slide)
		slides.append(slideObj)

	return slides



def get_slide_object(slide):
	slideObj = collections.OrderedDict()
	slideObj['slide_id'] = slide.slide_id
	slideObj['slide_type'] = str(slide.typeOfSlide)
	slideObj['summary'] = slide.summary
	slideObj['images'] = get_images_for_slide(slide.slide_id)

	return slideObj


def get_images_for_slide(slide_id):

	imagesForSlide = Image.objects.filter(slide=str(slide_id))
	images = []

	for img in imagesForSlide:
		imageObject = get_image_object(img)
		images.append(imageObject)

	return images

def get_image_object(img):
	imageObj = collections.OrderedDict()
	imageObj['image_id'] = img.image_id
	imageObj['image_url'] = img.image.url 	# give the absolute path to the image so it can be pulled
	imageObj['width'] = img.image.width
	imageObj['height'] = img.image.height
	imageObj['caption'] = img.caption
	imageObj['credit'] = img.photo_credit
	#imageObj['date-taken'] = image.dateTaken

	return imageObj










