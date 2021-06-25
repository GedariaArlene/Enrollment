from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
	path ('',views.EStudent),
	path('students', views.List, name="students"),
	path('requirement.html', views.Requirements, name="requirement"),
	path('specialization.html', views.Specialization, name="specialization"),
	path('schedule.html', views.Schedule, name="schedule"),	
	path('Done.html', views.Done, name="Done"),	
	

	# path('edit/<int:id>', views.edit),  
 #    path('update/<int:id>', views.update),  
 #    path('delete/<int:id>', views.destroy),
]

'''
urlpatterns = [
    path('', views.ActivityList.as_view(), name='activity_list'),
    path('view/<int:pk>', views.ActivityDetail.as_view(), name='activity_detail'),
    path('new', views.ActivityCreate.as_view(), name='activity_new'),
    path('edit/<int:pk>', views.ActivityUpdate.as_view(), name='activity_edit'),
    path('delete/<int:pk>', views.ActivityDelete.as_view(), name='activity_delete')
]'''

