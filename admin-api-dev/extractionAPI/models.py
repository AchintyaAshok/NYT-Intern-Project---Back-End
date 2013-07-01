from django.db import models

import math

# Create your models here.

class Tag_Type(models.Model):
	tagName = models.CharField(max_length=15, primary_key=True, verbose_name = "Tag")	#	The tag is a unique element, attributed to a story (Many-To-Many)

	def __unicode__(self):
		return self.tagName

class Story(models.Model):
	story_id = models.AutoField(primary_key=True)
	headline = models.CharField(max_length=100, verbose_name="Headline")
	author_firstName = models.CharField(max_length=30, verbose_name="First Name")
	author_lastName = models.CharField(max_length=30, verbose_name="Last Name")
	timeCreated = models.DateTimeField(auto_now_add=True, editable=False)
	storyTags = models.ManyToManyField(Tag_Type, db_table="Tags_In_Story", verbose_name="Tags")		# 	The relationship table between a story and tags associated with it

	coverPhoto = models.ImageField(verbose_name="Cover Photo", upload_to="CoverPhotos", height_field="height", width_field="width")				
#	These fields need to exist in the table, but get populated by PIL when it analyzes the uploaded image
	width = models.PositiveIntegerField(editable=False)
	height = models.PositiveIntegerField(editable=False)


	def __unicode__(self):
		return self.headline


class Slide_Types(models.Model):
	type_name = models.CharField(max_length=30, primary_key=True, verbose_name="Type of Slide")

	def __unicode__(self):
		return self.type_name


class Slide(models.Model):
	slide_id = models.AutoField(primary_key=True)
	typeOfSlide = models.ForeignKey(Slide_Types, verbose_name="Type of Slide")				#	Each slide must be designated a type existing in the Slide_Types table
	story = models.ForeignKey(Story, verbose_name="Belonging to Story")
	summary = models.CharField(max_length=500, verbose_name="Description", null=True)

	def __unicode__(self):
		toRet = str(self.slide_id) + " - " + str(self.summary)
		return toRet


class Image(models.Model):
	image_id = models.AutoField(primary_key=True)
	slide = models.ForeignKey(Slide, verbose_name="Belonging to Slide")

	image = models.ImageField(upload_to="Images", height_field="height", width_field="width", verbose_name="Photo")
	#	These fields need to exist in the table, but get populated by PIL when it analyzes the uploaded image
	width = models.PositiveIntegerField(verbose_name="Width (pixels)", editable=False)
	height = models.PositiveIntegerField(verbose_name="Height (pixels)", editable=False)

	#	Metadata about the photo that poster needs to include
	photo_credit = models.CharField(max_length=50, verbose_name="Photo Credit")
	caption = models.CharField(max_length=150, verbose_name="Image Caption")
	dateTaken = models.DateField(auto_now=False, null=True, verbose_name="Date Photo Taken")			#	They input when the photo was taken? this is an optional value

	def __unicode__(self):
		# return str(self.slide_id)
		toRet = str(self.image_id) + " - " + str(self.caption)
		return toRet

	# def __unicode__(self):
	# 	toRet = "Part of Slide:\t" + str(self.slide) + "\nCaption:\t" + self.caption
	# 	return toRet

	# x, y coords, z-index (integers) 