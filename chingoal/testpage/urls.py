
from django.conf.urls import include, url
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^$','testpage.views.homepage',name ='gobackhomepage'),
    # url(r'^photo/(?P<username>.+)','grumblr.views.get_photo',name='photo'),
    url(r'^get-test$','testpage.views.get_test',name ='gettest' ),
    url(r'^get-learn/(?P<level>[0-5]{1})/(?P<lesson>[1-6]{1})$','testpage.views.get_learn',name ='getlearn' ),
    url(r'^get-result$','testpage.views.get_result',name ='getresult' ),
    url(r'^test-create$','testpage.views.test_create',name ='testcreate' ),
    url(r'^test-add-q-mc/(?P<maxid>[0-9])$','testpage.views.test_add_question_mc',name ='testaddmcq' ),
    url(r'^test-add-q-tr/(?P<maxid>[0-9])$','testpage.views.test_add_question_tr',name ='testaddtrq' ),
    url(r'^test-save-question$','testpage.views.test_save_question',name ='testsavequestion' ),
    url(r'^test-edit-question$','testpage.views.test_edit_question',name ='testeditquestion' ),
    url(r'^test-delete-question$','testpage.views.test_delete_question',name ='testdeletequestion' ),
    url(r'^test-post$','testpage.views.test_post',name ='testpost' ),
    url(r'^get-learningResult$','testpage.views.get_learningResult',name ='getlearningResult' ),
    url(r'^skip-question$','testpage.views.skip_question',name ='skipquestion' ),
    url(r'^exit-learning$','testpage.views.exit_learning',name ='exitlearning' ),
    url(r'^show-tips$','testpage.views.show_tips',name ='showtips' ),
    url(r'^get-discussion$','testpage.views.get_discussion',name ='getdiscussion' ),
    url(r'^create-learning$','testpage.views.create_learning',name ='createlearning' ),
    url(r'^learning-add-question$','testpage.views.learning_add_question',name ='learningaddquestion' ),
    url(r'^learning-save-question$','testpage.views.learning_save_question',name ='learningsavequestion' ),
    url(r'^learning-edit-question$','testpage.views.learning_edit_question',name ='learningeditquestion' ),
    url(r'^learning-delete-question$','testpage.views.learning_delete_question',name ='learningdelete_question' ),
    url(r'^learning-post$','testpage.views.learning_post',name ='learningpost' ),
]
