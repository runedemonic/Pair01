## 프로젝트 소개
### 영화리뷰 게시판 & 회원가입


- 🗓

   ![](https://raw.githubusercontent.com/runedemonic/TIL/master/img/2022-10-14-17-27-53.gif)

  프로젝트 기간

  - 2022.10.14

- 💻

   

  사용 기술

  - Python, Django, HTML, CSS, Bootstrap5,beautifulsoup

- 💡

   

  배운 점

  - 멀티앱을 사용하여 각자의 기능들을 연결하여 구현하는 방법을 배웠습니다.
  - 크롤링을 하여 영화 정보를 받는 방법을 배웠습니다.
  - 에러가 발생했을 때 당황하지 않고 서로 힘을 합쳐서 해결해 나갈 수 있어서 좋았습니다. 
  - 크롤링 하는 것을 배울 수 있어서 좋은 공부가 됐습니다!
  - 다들 잘 하셔서 많이 배울 수 있었습니다. 한주한주 크롤링만 늘어나는거 같습니다.

## 🚩목적

페어 프로그래밍을 통해 영화 리뷰 커뮤니티 서비스를 개발

- **ModelForm**을 활용한 CRUD 구현
- **Staticfiles** 활용
- 

# 🧾기능 소개

##### app.reviews 

`create`: 리뷰를 작성하는 ModelForm을 제공하고 ModelForm에서 request를 받아 처리하였습니다.

`index`: DB에 저장된 모든 리뷰들을 읽어서 간단한 정보를 사용자에게 보여줍니다.

`detail`: 선택한 리뷰의 제목, 내용 등 모든 정보를 보여줍니다.

`update`: 이미 작성된 리뷰 인스턴스를 가져와서 ModelForm을 제공하고 request를 처리합니다.

`delete`: 선택한 리뷰를 삭제 후 index로 redirect 합니다.

##### app.accounts

`create`: 리뷰를 작성하는 ModelForm을 제공하고 ModelForm에서 request를 받아 처리하였습니다.

`index`: DB에 저장된 모든 회원들을 읽어서 간단한 정보를 사용자에게 보여줍니다.

`detail`: 선택한 회원의 정보를 보여줍니다.

`update`: 이미 작성된 회원 인스턴스를 가져와서 ModelForm을 제공하고 request를 처리합니다.

`delete`: 선택한 리뷰를 삭제 후 index로 redirect 합니다.

##### 네이버 영화사이트를 크롤링하여 reviews/detail에 포스터와 영화제목 받아오기

