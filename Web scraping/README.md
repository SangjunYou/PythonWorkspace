# 파이썬 웹스크래핑 공부
## Xpath
> html 문서에 있는 특정 element 를 지칭하는 주소(경로)이다
## requests
> html 페이지를 불러오며 동작속도가 빠르다. 다만 동적 웹 페이지의 내용을 불러올수 없는 특징이 있으며
> 주어진 url을 통해 받아온 html에 원하는 정보가 있을 때 사용하기 좋다.
## res.raise_for_status()
> requests 사용시 접속하는 사이트에 문제가 없는지 확인이 가능하다.
## selenium
> 웹 페이지를 자동화 하는 framework 이며, 동작 속도는 requests에 비해 느리지만 동적인 웹 페이지 에서 사용할수 있고
> 로그인, 어떤 결과에 대한 필터링 등 동작을 해야하는 경우 사용할수 있다.
> **사용시 크롬 버전에 맞는 크롬드라이버가 설치되있어야 한다.**
## selenium 사용법
```
file_element(s)_by_id           -> id로 찾기
file_element(s)_by_class_name   -> class name 으로 찾기
file_element(s)_by_link_text    -> 링크 text 로 찾기
file_element(s)_by_xpath        -> xpath로 찾기
  
click()                         -> 클릭
send_key()                      -> 글자 입력
clear()                         -> 내용지우기
```
## BeautifulSoup
```
find                      -> 조건에 맞는 첫번째 element
find_all                  -> 조건에 맞는 모든 element 리스트로
find_next_sibling(s)      -> 다음 형제 찾기
find_previous_sibling(s)  -> 이전 형제 찾기

soup["href"]              -> 속성
soup.get_text()           -> 텍스트
```
## CSV
```
f = open(filename, "w", encoding="utf-8-sig", newline="")
```
## headless_chrom
> 브라우저를 띄우지 않고 동작 할수 있다
> 때로는 User-Agant 정의가 필요하다
