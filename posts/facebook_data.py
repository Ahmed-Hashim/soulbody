from .models import *
import requests

def add_like(post_id):
    posts=PublishedPost.objects.filter(fb_post_id=post_id)
    if len(posts)>0:
        posts[0].like_count=int(posts[0].like_count)+1
        posts[0].save()
    else:
        pass

def remove_like(post_id):
    posts=PublishedPost.objects.filter(fb_post_id=post_id)
    if len(posts)>0:
        posts[0].like_count=int(posts[0].like_count)-1
        posts[0].save()
    else:
        pass
def add_comment(post_id,wh_comment,comment_id,comment_by,comment_by_profile):
    try:
        post=PublishedPost.objects.filter(fb_post_id=post_id)[0]
    except:
        print("pass")
        post=False
    if post:
        Comment.objects.create(post_id=post,comment=wh_comment,comment_id=comment_id,comment_by=comment_by,comment_by_profile=comment_by_profile)
    else:
        print("post not exicted")
def remove_comment(comment_id):
    try:
        post_id=Comment.objects.filter(comment_id=comment_id)[0]
        post_id.delete()
    except:
        print("not excist")


def get_insights_impressions():
    try:
        response=requests.get("https://graph.facebook.com/v16.0/104133784532614/insights/page_impressions/month?access_token=EAAKhzXgGKZBMBAJXMh2UgmAAaWmh3BmHV5DAycsoAt5fchFKo9sWPRItr8lQIZC4oLipP6FwJL4fZBP0ZAX4BUGvmMZAVxuLTtLcXZBNw7aAIUUEiL4T8vkVXnHOHm5MtERn7cPUKPuuASx4gFMNvg1NuZAAGKBtjn1b6haBIP84jDxRU5EgnDgt9GHK9sovn8ZD").json()
    
        month=response["data"][0]['values'][1]['value']
        return month
    except:
        month=15
        return month

def get_insights_engaged():
    try:
        response=requests.get("https://graph.facebook.com/v16.0/104133784532614/insights/page_engaged_users/month?access_token=EAAKhzXgGKZBMBAJXMh2UgmAAaWmh3BmHV5DAycsoAt5fchFKo9sWPRItr8lQIZC4oLipP6FwJL4fZBP0ZAX4BUGvmMZAVxuLTtLcXZBNw7aAIUUEiL4T8vkVXnHOHm5MtERn7cPUKPuuASx4gFMNvg1NuZAAGKBtjn1b6haBIP84jDxRU5EgnDgt9GHK9sovn8ZD").json()
    
        month=response["data"][0]['values'][1]['value']
        return month
    except:
            month=15
            return month

