from django.urls import path, include
from . import views


urlpatterns = [

    path('unpublished', views.unpublished_list, name='unpublished'),

    path('unpublished_posts', views.unpublished_posts, name='unpublished_posts'),
    path('published', views.published_list, name="published"),
    path('create_post', views.createpost, name='create_post'),
    path('edit_details/p=<int:id>', views.edit_details, name='edit_details'),
    path('edit_schedule_post/p=<int:id>',
         views.edit_schedule_post, name='edit_schedule_post'),
    path('schedule_posts', views.schedule_posts, name='schedule_posts'),
    path('schedule_table', views.schedule_table, name='schedule_table'),
    path('show/p=<int:id>', views.post_details, name='post_details'),
    path('delete_modal/p=<int:id>', views.delete_modal, name='delete_modal'),
    path('delete/p=<int:id>', views.delete_post, name='delete_post'),
    path('add_to_schedule/p=<int:id>',
         views.add_to_schedule, name='add_to_schedule'),
    path('schedule_modal/p=<int:id>', views.schedule_modal, name='schedule_modal'),
    path('get_posts', views.get_posts, name='get_posts'),
    path('get_products', views.get_products, name='get_products'),
    path('almazaziproducts', views.almazaziproducts,
         name='almazaziproducts'),
    path('create_post/<int:id>', views.create_post, name='create_post'),
    path('upload', views.upload, name='upload'),
    path('publish_now/p=<int:id>', views.publish_now, name='publish_now'),
    path('delete_schedule/p=<int:id>',
         views.delete_schedule, name='delete_schedule'),
    path('make_design/p=<int:id>', views.make_design, name='make_design'),
    path('new_design/p=<int:id>', views.new_design, name="new_design"),
    path('schedule_design/<int:id>', views.schedule_design, name="schedule_design"),
    path('show_pub_post/<int:id>', views.show_pub_post, name="show_pub_post"),
    path('dashheader', views.dashheader, name="dashheader"),
    path('test', views.test, name="test"),


    ##################################################################################################
    ###### Ajax_URLS ######
    #######################
    path('delete_post_ajax/p=<int:id>',
         views.delete_post_ajax, name='delete_post_ajax'),
    ##################################################################################################
    ###### WebHook_URLS ######
    #######################
    path('hooks', views.hooks, name='hooks'),
    path('shcadule', views.schedule_posts, name='scha'),

]
