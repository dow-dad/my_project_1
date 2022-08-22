from django.db import models

# 블로그 게시물 정보 1개를 저장할 객체
class Post(models.Model):
# 게시물 제목을 저장할 속성
# CharField : 글자수 제한이 있는 문자열
# max_length = 300 :  글자수 300까지 저장
    title = models.CharField(max_length = 300)
    writer = models.CharField(max_length = 100)
    content = models.TextField()
#Text,Field() : 글자수 제한없는 문자열
    created_at = models.DateTimeField(auto_now_add = True)
#models.DateTimeField : 날짜와 시간 저장

    def __str__(self):
        return'[id = '+str(self.id)+",title = "+self.title+",writer = "+self.writer+',content = '+self.content+',created_at = '+str(self.created_at)+"]"
