from django.urls import path
from .import views

#app_name = "course"

urlpatterns = [
    # urls for courses
    path('list/',views.ListCourse.as_view(),name='list_course'),
    path('list/<int:pk>/',views.CourseRetrieve.as_view(),name='course_info'),
    path('createcourse/<int:pk>/<int:upk>/',views.CreateCourse,name='create_course'),
    path('updatecourse/<int:pk>/',views.UpdateCourse.as_view(),name='update_course'),
    path('viewcourse/<int:pk>/',views.ViewEnrolledCourse.as_view(),name='view_course'),
    path('deletecourse/<int:pk>/',views.DeleteCourse,name='delete_course'),
    path('enrollcourse/<int:pk>/<int:upk>/',views.EnrollCourse,name='enroll_course'),
    path('mycourses/<int:upk>/',views.MyCourses,name='mycourses'),
    path('mycoursesteacher/<int:upk>/',views.TeacherCourses,name='mycoursesteacher'),

    # Urls for modules
    path('createmodule/<int:pk>/',views.CreateModule,name='create_module'),
    path('deletemodule/<int:pk>/', views.DeleteModule, name='delete_module'),
    path('updatemodule/<int:pk>/', views.UpdateModule, name='update_module'),
    path('getmodules/<int:pk>/', views.GetModules, name='read_module'),
    path('createmodulefile/<int:pk>/',views.CreateModuleFile,name='create_modulefile'),
    path('deletemodulefile/<int:pk>/',views.DeleteModuleFile,name='delete_modulefile'),
    path('getmodulefiles/<int:pk>/',views.GetModuleFiles,name='read_modulefile'),

    # urls for coupon generation
    path('coupon/<int:count>/<int:pk>/',views.CouponGenerator,name='coupon_generator'),
    path('availablecoupon/<int:pk>/',views.AvailableCoupon,name='available_coupon'),
    path('issuedcoupon/<int:pk>/',views.IssuedCoupon,name='issued_coupon'),
    path('issuecoupon/',views.IssueCoupon,name='issue_coupon'),

    # Urls for subjects
    path('createsubject/<int:pk>/',views.CreateSubject,name='create_subject'),
    path('updatesubject/<int:pk>/',views.UpdateSubject,name='update_subject'),
    path('deletesubject/<int:pk>/',views.DeleteSubject,name='delete_subject'),
    path('subjectlist/',views.SubjectList,name='list_subject'),
    path('subject/<int:pk>/',views.ViewSubject,name='view_subject'),
    path('teachersubject/<int:upk>/',views.TeacherSubject,name='teacher_subject'),
    path('coursecount/',views.coursecount,name='course_count'),
    path('courses/<int:pk>/',views.CoursesIntheSubject,name='course_in_subject'),

]