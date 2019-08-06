from django.shortcuts import render
from .models import Book
def list_books(request):
    a = 1/0
    books=Book.objects.all()
    return render(request, 'book/list_books.html',
                  {'list': books})
def book_detail(request, id):
    b=Book.objects.get(pk=id)
    pepole_list=b.famouspeople_set.all()
    return render(request, 'book/list_people.html',
                  {'list': pepole_list})

def order(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
from django.views import View
class Order(View):
    def get(self, request):
        pass
    def post(self, request):
        pass
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning, QueryParameterVersioning
class ParamVersion(object):  # URLPathVersioning 的本质
    def determine_version(self, request, *args, **kargs):
        version = request.query_params.get('version')
        return version
class UserView(APIView):
    versioning_class = ParamVersion
    def get(self, request):
        ver = request.version
        
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.response import Response as DrfResponse
from rest_framework.pagination import PageNumberPagination
class UserView(APIView):
    def get(self, request):
        users = User.objects.all() # 获取所有数据
        pager = PageNumberPagination() # 创建分页器
        paged_users = pager.paginate_queryset(queryset=users, request=request, view=self)
        serialize_user = UserSerializer(instance=paged_users, many=True)
        return DrfResponse(serialize_user)
        


