
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'basic.user_manage.home'),
    url(r'^register$', 'basic.user_manage.register', name = 'register'),
    url(r'^login$', 'django.contrib.auth.user_manage.login', {'template_name':'login.html'}),
    url(r'^logout$', 'django.contrib.auth.user_manage.logout_then_login', name = 'logout'),
    url(r'^edit-profile$', 'basic.user_manage.edit_profile', name= 'editProfile'),
    url(r'^view-profile/(?P<uname>\w+)$', 'basic.user_manage.view_profile', name = 'viewProfile'),
    url(r'^reset-password$', 'basic.user_manage.reset_password', name = 'resetPassword'),
    url(r'^new-password/(?P<token>.*)$', 'basic.user_manage.new_password', name = 'newPassword'),
    url(r'^edit-schedule$', 'basic.user_manage.edit_schedule', name= 'editSchedule'),
    url(r'^add-follower/(?P<uname>\w+)$', 'basic.user_manage.add_follower', name = 'addFollower'),
    url(r'^remove-follower/(?P<uname>\w+)$', 'basic.user_manage.remove_follower', name = 'removeFollower'),

# test and learning related url 
    url(r'^get-test$','basic.test.get_test',name ='gettest' ),
    url(r'^get-resul$','basic.test.get_result',name ='getresult' ),
    url(r'^test-create$','basic.test.test_create',name ='testcreate' ),
    url(r'^test-add-question$','basic.test.test_add_question',name ='testaddquestion' ),
    url(r'^test-save-question$','basic.test.test_save_question',name ='testsavequestion' ),
    url(r'^test-edit-question$','basic.test.test_edit_question',name ='testeditquestion' ),
    url(r'^test-delete-question$','basic.test.test_delete_question',name ='testdeletequestion' ),
    url(r'^test-post$','basic.test.test_post',name ='testpost' ),
    url(r'^get-learningResult$','basic.test.get_learningResult',name ='getlearningResult' ),
    url(r'^skip-question$','basic.test.skip_question',name ='skipquestion' ),
    url(r'^exit-learning$','basic.test.exit_learning',name ='exitlearning' ),
    url(r'^show-tips$','basic.test.show_tips',name ='showtips' ),
    url(r'^get-discussion$','basic.test.get_discussion',name ='getdiscussion' ),
    url(r'^create-learning$','basic.test.create_learning',name ='createlearning' ),
    url(r'^learning-add-question$','basic.test.learning_add_question',name ='learningaddquestion' ),
    url(r'^learning-save-question$','basic.test.learning_save_question',name ='learningsavequestion' ),
    url(r'^learning-edit-question$','basic.test.learning_edit_question',name ='learningeditquestion' ),
    url(r'^learning-delete-question$','basic.test.learning_delete_question',name ='learningdelete_question' ),
    url(r'^learning-post$','basic.test.learning_post',name ='learningpost' ),
]
