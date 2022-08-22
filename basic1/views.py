from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("안녕!! Django!!")

def greet(request):
    return render(request, 'basic1/greet.html')

def fruit_form(request):
    return render(request, 'basic1/fruit_form.html')

def fruit(request):
    input = request.POST.get('favorite')
    print('input = ', input)

    input2 = request.POST.get('browser')
    print('input2 = ', input2)

    input3 = request.POST.get('hobby')
    print('input3 = ', input3)

    input4 = request.POST.get('book')
    print('input4 = ', input4)
    print('request.POST = ', request.POST)

    # return HttpResponse('당신은'+input+ '^_^' + \
    #                     '<br>브라우저로 '+input2+'를 사용하시네요.'+ \
    #                     '<br>취미는 '+ input3+ ' 이군요.' + \
    #                     '<br>책을 읽고 당신은 ('+ input4 + ') 라고 적었습니다.')
    data = {'i1': input,'i2':input2 ,'i3':input3, 'i4':input4} # ▶ django에서 변수 설정 // 변수명 : 변수값
    return render(request, 'basic1/result1.html', data)


# ▽ 지욱.ver
# def fruit(request):
#     favorite = request.POST.get('favorite')
#     hobby = request.POST.get('hobby')
#     book = request.POST.get('book')
#     browser = request.POST.get('browser')
#     print(f'favorite = {favorite}, hobby = {hobby}, book = {book}, browser = {browser}')
#     result = '좋아하는 과일 : ' + favorite + \
#              '<br>취미 : ' + hobby + \
#         '<br>좋아하는 책 : ' + book + \
#         '<br>사용하는 브라우저 : '+ browser
#     return HttpResponse(result)


# ▽ 그냥 해봄.ver
# def fruit(request):
#     ans = '빡빡이'
#     input = request.POST.get('favorite')
#     if ans == input :
#         print('input = ', input)
#
#         input2 = request.POST.get('browser')
#         print('input2 = ', input2)
#
#         input3 = request.POST.get('hobby')
#         print('input3 = ', input3)
#
#         input4 = request.POST.get('book')
#         print('input4 = ', input4)
#         print('request.POST = ', request.POST)
#
#         return HttpResponse('당신은'+input+ '◝(⁰▿⁰)◜' + \
#                             '<br>( ´ ▽ ` )ﾉ  브라우저로 '+input2+'를 사용하시네요.'+ \
#                             '<br>(￣▽￣)ノ   취미는 '+ input3+ ' 이군요.' + \
#                             '<br>(^０^)ノ  책을 읽고 당신은 ('+ input4 + ') 라고 적었습니다.')
#     else :
#         return HttpResponse( input + '라고 입력하셨네요...(´д｀)' + \
#                             '<br>제대로 하시죠..? ( ง ᵒ̌ ∽ᵒ̌)ง⁼³₌₃' )


