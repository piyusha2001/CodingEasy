from django.urls import path
from home import views


urlpatterns = [
    # Pages
    path('', views.index, name='index'),
    path('feature/', views.feature, name='home-feature'),
    path('pricing/', views.pricing, name='home-pricing'),
    path('contact/', views.contact, name='home-contact'),
    path('team/', views.our_team, name='home-team'),
    path('editor/', views.editor, name='home-editor'),
    path('listtemplates/', views.listtemplates, name='listtemplates'),
    path('listtemplates1/', views.listtemplates1, name='listtemplates1'),
    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('delete/<int:uid>', views.delete_user, name="delete_account"),
    path('subscribe/', views.subscribe, name='newsletter'),
    # Courses
    path('html/', views.html, name='html'),
    path('html1/', views.html1, name='html1'),
    path('css/', views.css, name='css'),
    path('css1/', views.css1, name='css1'),
    path('js/', views.js, name='js'),
    path('js1/', views.js1, name='js1'),
    path('jQuery/', views.jQuery, name='jQuery'),
    path('jQuery1/', views.jQuery1, name='jQuery1'),
    path('c/', views.c_course, name='c'),
    path('c1/', views.c_course1, name='c1'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),
    path('bootstrap1/', views.bootstrap1, name='bootstrap1'),
    path('py/', views.py, name='py'),
    path('py1/', views.py1, name='py1'),
    path('cpp/', views.cpp, name='cpp'),
    path('cpp1/', views.cpp1, name='cpp1'),
    path('ml/', views.ml, name='ml'),
    path('ml1/', views.ml1, name='ml1'),
    path('django/', views.django, name='django'),
    path('django1/', views.django1, name='django1'),
    path('git/', views.git, name='git'),
    path('git1/', views.git1, name='git1'),
    path('course_video/', views.course_video, name='course_video'),
        path('course_video/', views.course_video, name='course_video'),

    # Quiz Pages URLs here
    path('quiz/', views.quizHome, name='home-quiz'),
    path('quiz/python/', views.quizPython, name='home-quizPython'),


    # To add url to a new Course

    # path('newcourse/', views.newcourse, name='newcourse'),  -> for rendering course
    # path('newcourse1/', views.newcourse1, name='newcourse1'),  -> for rendering sub topics

    # Do not forget to add/update views in views.py file
]
