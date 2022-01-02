import views
from datetime import date


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

# routes = {
# #     '/': views.Index(),
#     '/index/': views.Index(),
# #     '/about/': views.About(),
# #     '/contact/': views.Contact(),
# #     '/study_programs/': views.StudyPrograms(),
# #     '/course_list/': views.CoursesList(),
# #     '/create_course/': views.CreateCourse(),
# #     '/create_category/': views.CreateCategory(),
# #     '/category_list/': views.CategoryList(),
# #     '/copy_course/': views.CopyCourse()
# }
