from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import sweetify
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView
from posts.uploads3 import upload_file
from posts.uploadtofacebook import uptofb
from .models import Post, PublishedPost, Schedule, AlmazadiProducts, Category
from crmsb.models import *
from .forms import PostForm, ScheduleForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from .image_des import *
from .uploadimg import *
from django.contrib import messages
import json
from pytz import timezone as tz
#from .get_posts import main, products_checking
from .resize_image import resize_img
from django.views.decorators.csrf import csrf_exempt
from .facebook_data import *
import random
from .openai import *
from django.contrib.auth.mixins import LoginRequiredMixin
import sweetify
from django.core.files.storage import default_storage
import boto3
from django.conf import settings


def get_json(request, *args, **kwargs):
    post_lists = Post.objects.all()
    post_published_count = Post.objects.filter(published=True).count()
    post_unpublished_count = Post.objects.filter(published=False).count()
    published_precent = round(
        post_published_count / post_unpublished_count*100)
    data = {
        'name': published_precent
    }
    return JsonResponse(data)

# Create your views here.


@login_required
def dashboard(request):
    post_lists = Post.objects.all()
    post_published = PublishedPost.objects.all()
    category = Category.objects.all()
    categoreis = ""
    index = 0
    for cat in category:
        if index == len(category)-1:
            categoreis = f"{categoreis}'{cat}'"
        else:
            categoreis = f"{categoreis}'{cat}',"
            index += 1
################ LEADS################
    shops_prospect = Customer.objects.filter(
        Situation__contains='Prospect').count()
    shops_active = Customer.objects.filter(
        Situation__contains='Active').count()
    try:
        lead_target = round(shops_active/shops_prospect*100)
    except:
        lead_target = 0
############### Insights################
    monthly_impressions = get_insights_impressions()
    monthly_engaged = get_insights_engaged()

# Dashboard Chats Data
    try:
        post_published_count = PublishedPost.objects.all().count()
        post_unpublished_count = Post.objects.filter(published=False).count()

# Dashboard Chats Data

        post_count = Post.objects.all().count()
        published_precent = round(
            post_published_count / post_unpublished_count*100)

        context = {
            'published': post_published,
            'post_count': post_count,
            'category': category,
            'lead_target': lead_target,
            'shops_active': shops_active,
            'monthly_impressions': monthly_impressions,
            'monthly_engaged': monthly_engaged,
            'post_published': post_published_count,
            'post_unpublished': post_unpublished_count,
            'precent': published_precent,
            'posts': post_lists,

        }
    except:
        context = {'post_published': post_published}

    return render(request, 'post/dashboard.html', context)


@login_required
def dashheader(request):

    qoutes = list(Quotes.objects.all())
    # if you want only a single random item
    if len(Quotes.objects.all()) >= 1:
        random_q = random.choice(qoutes)
    else:
        random_q = "We are delighted to have you among us. On behalf of all the members and the management, we would like to extend our warmest welcome and good wishes!"

    context = {'random_q': random_q, }
    return render(request, 'post/dashboardheader.html', context)


@login_required
def show_pub_post(request, id):
    post = PublishedPost.objects.get(pk=id)
    comments = post.comments.all()
    context = {'post': post, 'comments': comments}
    return render(request, 'post/modals/show_published_posts_data.html', context)


@login_required
def get_posts(request):
    context = {'title': "Almazadi Posts"}
    return render(request, 'post/get_posts.html', context)


@login_required
def almazaziproducts(request):
    products = AlmazadiProducts.objects.all().filter(
        created_post=False).order_by('-id')
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj}
    return render(request, 'post/new_posts.html', context)


@login_required
def get_products(request):
    # refresh_products.delay()
    products = AlmazadiProducts.objects.all().filter(
        created_post=False).order_by('-id')
    count = 0
    links = products_checking()
    for link in links:
        try:
            message = f"{link['add_title']} \n متوفر الان على تطبيق المزادي\n من خلال {link['add_owner']}"
            if link['category'] == 'Multimédia':
                categorys = "Multimedia"
            elif link['category'] == 'Productive Family':
                categorys = 'Productive Fami'
            elif link['category'] == 'Professional Equipment':
                categorys = 'Professional Eq'
            else:
                categorys = link['category']
                category = Category.objects.get(name__contains=categorys)
            if "store" in link['link']:
                edit_link = f"https://almazadi.com/admin/products/{link['link'].split('/')[-1]}/edit"
            else:
                edit_link = f"https://almazadi.com/admin/posts/{link['link'].split('/')[-1]}/edit"
            if link['add_image'] != "https://almazadi.com/storage/app/default/picture.jpg":
                AlmazadiProducts.objects.create(
                    add_title=link['add_title'],
                    imagelink=link['add_image'],
                    edit_link=edit_link,
                    add_link=link['link'],
                    owner=link['add_owner'],
                    category=category,
                    message=message
                )
                count += 1
                # print(f"new ad/s added .")
            else:
                pass
        except Exception as e:
            pass
    if count > 0:
        sweetify.success(request, f"{count} new ad/s added .")
    else:
        sweetify.info(request, f"0 New ads.")
    context = {'products': products}
    return render(request, 'post/new_posts.html', context)


@login_required
def create_post(request, id):
    product = AlmazadiProducts.objects.get(pk=id)

    Post.objects.create(imagelink=product.imagelink,
                        category=product.category, message=product.message)
    product.created_post = True
    product.save()
    return HttpResponse(status=204,
                        headers={
                            'HX-Trigger': json.dumps({
                                "changeNotification": None,
                                "changeAds": None,
                                "showMessage": f"Your post has been created.",
                                "type": "bg-success"
                            })
                        })


@login_required
def upload(request):
    if request.method == 'POST':
        get_posts(request)
        return redirect("unpublished")
    return render(request, 'post/upload.html')


@login_required
def unpublished_list(request):
    # Paginator
    post_lists = Post.objects.filter(published=False)
    paginator = Paginator(post_lists, 8)  # Show 8 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        id_list = request.POST.getlist('boxes')
        if 'published' in request.POST:
            # Update database PUBLISH
            Post.objects.filter(pk__in=id_list).update(published=True)
            for id in id_list:
                post = Post.objects.get(pk=id)
                print(post.imagelink)
                uptofb(post.imagelink, post.message)
            return redirect('published')
        elif 'delete' in request.POST:
            # Update database delete
            Post.objects.filter(pk__in=id_list).delete()
            return redirect('unpublished')
        elif 'schedule' in request.POST:
            # Schedule posts
            for id in id_list:
                post = Post.objects.get(pk=id)
                myobject = Schedule(
                    imagelink=post.imagelink,
                    design_link=post.design_link if post.design_link else None,
                    message=post.message,
                    category_id=post.category_id,
                    timezone=""
                )
                myobject.save()
                post.delete()
            return redirect('schedule_posts')

    context = {
        'posts': page_obj,
        'title': 'Unpublished Posts'
    }
    return render(request, 'post/posts_unpublished.html', context)


@login_required
def published_list(request):

    published_list = PublishedPost.objects.get_queryset().order_by('id')
    paginator = Paginator(published_list, 8)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': page_obj,
               'title': 'Published Posts'

               }
    return render(request, 'post/posts_published.html', context)


def unpublished_posts(request):
    post_lists = Post.objects.filter(published=False)
    paginator = Paginator(post_lists, 8)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': page_obj,
               }
    return render(request, 'post/unpublished_posts_listing.html', context)



"""def delete_my_model_instance(pk):
    my_model_instance = pk

    # Check if the instance has an image
    if my_model_instance.design_link:
        # Initialize a connection to your AWS S3 bucket
        s3 = boto3.client('s3', aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY)

        # Delete the image file from AWS S3
        s3.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                         Key=my_model_instance.design_link.name)

"""
@login_required
def publish_now(request, id):
    postupdate = Post.objects.filter(pk=int(id))
    post = Post.objects.get(pk=id)
    if request.method == "GET":
        return render(request, 'post/modals/publish.html', {"post": post})
    if request.user.profile.access_token:
        if post.design_link:
            link = f"{post.design_link.url}"
            # link='almazadi-marketing.com/media/images/designs/thumb-816x460-0b8df0adf409ce6e11b76c8e41e3d5ed.jpeg'
        else:
            link = post.imagelink
        message = post.message
        access_token = request.user.profile.access_token
        data = uptofb(link, message, access_token)
        try:
            post_id = data['post_id']
            fb = f'https://facebook.com/{post_id}'
            PublishedPost.objects.create(
                link=post.imagelink,
                message=message,
                category_id=post.category_id,
                published_date=datetime.now(
                    tz(request.user.profile.timezone)).strftime('%Y-%m-%d %H:%M:%S'),
                scheduled_by=request.user,
                fb_post_id=post_id,
                fblink=fb+post_id)
            postupdate.update(published=True, design_link=None)
            delete_my_model_instance(post)
            return HttpResponse(status=204,
                                headers={
                                    'HX-Trigger': json.dumps({
                                        "postsChange": None,
                                        "changeNotification": None,
                                        "close": "close",
                                        "showMessage": f"Your post has been published.",
                                        "type": "bg-success"
                                    })
                                })
        except:
            return HttpResponse(status=204,
                                headers={
                                    'HX-Trigger': json.dumps({
                                        "close": "close",
                                        "showMessage": f"Access Token Expired.",
                                        "type": "bg-danger"
                                    })
                                })
    else:
        return HttpResponse(status=204,
                            headers={
                                'HX-Trigger': json.dumps({
                                    "close": "close",
                                    "showMessage": f"You dont have permissions to publish post",
                                    "type": "bg-danger"
                                })
                            })


@login_required
def post_details(request, id):
    post_details = Post.objects.get(id=id)
    if request.method == 'POST' and 'publish' in request.POST:
        print(post_details)
        post = Post.objects.filter(pk=int(id)).values('imagelink', 'message')
        link = post[0]['imagelink']
        message = post[0]['message']
        uptofb(link, message)
        post.update(published=True)
        return redirect(unpublished_list)

    context = {'post_details': post_details,
               'title': 'Post Details'
               }
    return render(request, 'post/post_detail.html', context)


@login_required
def post_details(request, id):
    post_details = Post.objects.get(id=id)
    if request.method == 'POST' and 'publish' in request.POST:
        print(post_details)
        post = Post.objects.filter(pk=int(id)).values('imagelink', 'message')
        link = post[0]['imagelink']
        message = post[0]['message']
        uptofb(link, message)
        post.update(published=True)
        return redirect(unpublished_list)

    context = {'post_details': post_details,
               'title': 'Post Details'
               }
    return render(request, 'post/post_detail.html', context)


@login_required
def createpost(request):
    submitted = False
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your post has been added to unpublished list")
            return redirect(unpublished_list)
    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted = True

    context = {'form': form,
               'submitted': submitted,
               'title': 'Create Post'
               }
    return render(request, 'post/create_post.html', context)


@login_required
def edit_details(request, id):
    post_details = Post.objects.get(pk=id)
    form = PostForm(request.POST or None, instance=post_details)
    if form.is_valid():
        form.save()
        return redirect("post_details", id)
    context = {'post_details': post_details, 'form': form,
               'title': 'Edit Post'

               }
    return render(request, 'post/edit_post.html', context)


@login_required
def delete_modal(request, id):
    post = Post.objects.get(pk=id)
    if request.method == "GET":
        return render(request, 'post/modals/delete.html', {"post": post})


@login_required
def delete_post(request, id):
    post = Post.objects.get(pk=id)
    if request.method == "DELETE":
        post.delete()
        return HttpResponse(status=204,
                            headers={
                                'HX-Trigger': json.dumps({
                                    "postsChange": None,
                                    "close": "close",
                                    "showMessage": f"Your post has been Deleted.",
                                    "type": "bg-success"
                                })
                            })


@login_required
def delete_schedule(request, id):
    post = Schedule.objects.get(pk=id)
    if request.method == "GET":
        return render(request, "post/modals/delete_schedule.html", {"post": post})
    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=204,
                            headers={
                                'HX-Trigger': json.dumps({
                                    "scheduleChange": None,
                                    "close": "close",
                                    "showMessage": f"Your post has been Deleted.",
                                    "type": "bg-success"
                                })
                            })


@login_required
def schedule_posts(request):
    # sweetify.success(request, f"{0} new ad/s added .")
    context = {'title': 'Scheduled Post'
               }
    return render(request, 'post/schedule_posts.html', context)


@login_required
def schedule_table(request):
    scheduled_list = Schedule.objects.all()
    context = {'posts': scheduled_list,
               }
    return render(request, 'post/schedule_table.html', context)


@login_required
def schedule_modal(request, id):
    post = Post.objects.get(pk=id)
    if request.htmx:
        return render(request, "post/modals/schudule.html", {"post": post})


@login_required
def add_to_schedule(request, id):
    post = Post.objects.get(pk=id)
    if post.design_link:
        myobject = Schedule(imagelink=post.imagelink, design_link=post.design_link,
                            message=post.message, category_id=post.category_id, timezone="")
    else:
        myobject = Schedule(imagelink=post.imagelink, message=post.message,
                            category_id=post.category_id, timezone="")
    myobject.save()
    post.delete()
    return HttpResponse(status=204,
                        headers={
                            'HX-Trigger': json.dumps({
                                "postsChange": None,
                                "close": "close",
                                "showMessage": f"Your post has been Schuduled.",
                                "type": "bg-success"
                            })
                        })


@login_required
def edit_schedule_post(request, id):
    post_details = Schedule.objects.get(pk=id)
    form = ScheduleForm(instance=post_details)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES, instance=post_details)
        if form.is_valid():
            form.save()
            post_details.schedule = True
            post_details.save()
            return redirect('schedule_posts')
    context = {'post_details': post_details, 'form': form,

               }
    return render(request, 'post/edit_schedule_post.html', context)


def make_design(request, id):
    post_details = Post.objects.get(pk=id)
    category = post_details.category
    # print(category)
    link = post_details.imagelink
    mergename = link.split('/')[-1]
    name = mergename.split('.')[0]+".webp"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    location = f'{BASE_DIR}/media/images/designs/'+name
    locationdel = f'{BASE_DIR}/media/images/designs/'+mergename
    # print(name)
    design(link, category, post_details)
    upload_file(location, "almazadi", f"images/designs/{name}")
    Post.objects.filter(pk=int(id)).update(
        design_link=f"images/designs/{name}", design=True)
    if os.path.exists(locationdel):
        os.remove(locationdel)
        os.remove(location)
    return HttpResponse(status=204,
                        headers={
                            'HX-Trigger': json.dumps({
                                "postsChange": None,
                                "close": "close",
                                "showMessage": f"Your Design Are Ready.",
                                "type": "bg-success"
                            })
                        })


def new_design(request, id):
    post_details = Post.objects.get(pk=id)
    link = post_details.imagelink
    location = "images/designs/"+link.split('/')[-1]
    Post.objects.filter(pk=int(id)).update(design_link=location, design=True)
    return HttpResponse(status=204,
                        headers={
                            'HX-Trigger': json.dumps({
                                "showMessage": f"Your Design Are Ready.",
                                "type": "bg-success"
                            })
                        })


def schedule_design(request, id):
    post_details = Schedule.objects.get(pk=id)
    link = post_details.imagelink
    location = "images/designs/"+link.split('/')[-1]
    design(link)
    Schedule.objects.filter(pk=int(id)).update(design_link=location)
    return redirect(request.META.get('HTTP_REFERER'))


def delete_post_ajax(request, id):
    post = Schedule.objects.get(pk=id)
    post.delete()
    return JsonResponse({})


def test(request):
    return render(request, 'post/test.html')


@csrf_exempt
def hooks(request, *args, **kwargs):
    if request.method == "POST":
        data = json.loads(request.body)
        ######### GET_DATA###########
        post_id = data["entry"][0]["changes"][0]["value"]["post_id"]
        type = data["entry"][0]["changes"][0]["value"]["item"]
        value = data["entry"][0]["changes"][0]["value"]["verb"]

        ######### LIKES###########
        if type == "reaction":
            if value == 'add':
                add_like(post_id)
                return HttpResponse(status=204,
                                    headers={
                                        'HX-Trigger': json.dumps({
                                            "showMessage": f"New Post like.",
                                            "postsChange": None,
                                            "type": "bg-success"
                                        })
                                    })
            elif value == 'remove':
                remove_like(post_id)
            else:
                print("bad_id")
        elif type == "comment":

            comment = data["entry"][0]["changes"][0]["value"]["message"]
            comment_id = data["entry"][0]["changes"][0]["value"]["comment_id"]
            comment_by = data["entry"][0]["changes"][0]["value"]["from"]["name"]
            comment_by_profile = f'https://www.facebook.com/{data["entry"][0]["changes"][0]["value"]["from"]["id"]}'
            if value == 'add':
                add_comment(post_id, comment, comment_id,
                            comment_by, comment_by_profile)
                print("Comment added")
            elif value == 'remove':
                remove_comment(comment_id)
                print("Comment removed")
            else:
                print("Error")

        return HttpResponse("success", 200)
    else:
        VERIFY_TOKEN = 'ALMAZADIMADATOKEN'
        if request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')


def schedule_posts(request):

    Schedule_Posts.delay(request.user.id, "15")
    sweetify.success(
        request, 'We received your request Successfully ', text=f'Thank you for choosing us', button='Ok', timer=5000)
    return HttpResponse("success", 200)
