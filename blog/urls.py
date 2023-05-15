from django.urls import path
from blog.views import CreatePost,AllPost,SpecificPost
from . import views
#starting from post they are using class based view

urlpatterns = [

    path("createpost",CreatePost,name = "createpost"),
    path("allpost",AllPost,name = "allpost"),
    path("allpost/<int:id1>",SpecificPost,name = "sppost"),

    path("post/new",views.PostCreateView.as_view(),name = "post-create"),
    path("post/<int:pk>/",views.PostDetailView.as_view(),name = "post-sp"),
    path("pages/<int:page>/",AllPost,name = "pages"),
    path("post/view/",views.PostListView.as_view(),name = "post-all"),
    path("post/myposts/",views.UserPostListView.as_view(),name = "user-post-all"),
    path("post/<str:u1>/",views.OtherUserPostListView.as_view(),name = "other-post-all"),
    path("post/<int:pk>/update/",views.PostUpdateView.as_view(),name = "post-update"),
    path("post/<int:pk>/delete/",views.PostDeleteView.as_view(),name = "post-delete"),
    path("posts/<int:id1>/",views.CommentPost,name = "post-comment"),
    path("posts/<int:id1>/approve/",views.CommentApprove,name = "post-approve"),
]    


