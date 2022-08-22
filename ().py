# coding: utf-8
from blog.models import Post
post1 = Post.objects.create(title = '제목1', writer = '홍길동', content ='내용1');
post2 = Post.objects.create(title = '제목2', writer = '홍길동2', content = '내용2');
post1.save()
post2.save()
post_list = Post.objects.all()
print(post_list)
