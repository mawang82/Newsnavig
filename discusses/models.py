from django.db import models
from django.contrib.auth.models import User
from topics.models import Topic
from django.contrib.contenttypes import generic
from comments.models import Comment
from votes.models import Vote
from shares.models import Share
from collect.models import Collect


class Discuss(models.Model):
	'''
	'''
	id = models.IntegerField(primary_key=True)
	
	is_boutique = models.BooleanField(default=False)
	
	title = models.CharField(max_length=210)
	detail = models.TextField(blank=True)
	
	start_user = models.ForeignKey(User)
	start_time = models.DateTimeField(auto_now_add=True)
	last_active_time = models.DateTimeField(blank=True, null=True)
	
	topics = models.ManyToManyField(Topic, related_name="topic_discuss")
	
	n_comments = models.IntegerField(default=0)
	n_collecter = models.IntegerField(default=0)
	n_supporter = models.IntegerField(default=1)
	n_shares = models.IntegerField(default=1)
	
	comments = generic.GenericRelation(Comment)
	
	supporters = generic.GenericRelation(Vote)
	
	shares = generic.GenericRelation(Share)
	
	collecters = generic.GenericRelation(Collect)
	
	class Meta:
		ordering = ["-last_active_time"]
	
	def __unicode__(self):
		return self.title + ' ' + str(n_comments)
	
	
	
	