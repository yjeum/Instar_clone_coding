온라인에 있는 branch로 변경하기<br>
git branch -r<br>
git checkout -t <git branch -r에서 내가 가고 싶은 branch> 

|ID|Depth 1|Depth 2|내용|
|:--:|:--:|:--:|:--:|
|user|로그인/회원관리|회원가입|아이디, 이름, 비밀번호 ,사용자 이름<br>프로필 첨부 가능(기본이미지 첨부)<br>가입완료 클릭 시 로그인 페이지로 이동<br>이용 약관 가입|
|user|로그인/회원관리|로그인|아이디 비밀번호 입력<br>오류가 있으면 오류메시지 출력<br>로그인 완료 시 메인 페이지로 이동|
|user|로그인/회원관리|로그아웃|로그아웃 후 메인페이지로 이동|
|user|프로필페이지|회원정보 수정|아이디 변경 불가<br>이름, 이메일 변경 가능<br>사진 첨부 가능<br>수정 완료 후 프로필 페이지로 이동|
|user|프로필페이지|비밀번호 변경|비밀번호 변경 후 프로필 페이지로 이동|
|user|프로필페이지|회원 탈퇴|탈퇴 시 로그아웃 후 탈퇴처리 메인페이지로 이동|
|user|프로필페이지|게시글확인|해당 유저가 작성한 게시글 보여줌|
|user|프로필페이지|팔로우&언팔로우|본인의 페이지가 아니라면 팔로우 언팔로우 가능|
|user|프로필페이지|팔로잉&팔로워|해당 유저가 팔로잉 하고 있는 유저의 숫자<br>해당 유저를 팔로워 하고 있는 유저의 숫자<br>누르면 목록으로|
|post|게시글관리|메인페이지 게시글 보기|해당 게시글을 누르면 디테일 페이지 팝업<br>게시글의 contents, comments, likes, 작성자 표기|
|post|게시글관리|상세 게시글 보기|디테일 페이지 팝업<br>게시글의 contents, comments, likes, 작성자 표기|
|post|게시글관리|게시글 게시|사진 첨부 필수, 내용 첨부 가능, 해쉬태그<br>생성 후 메인페이지로 이동|
|post|게시글관리|게시글 수정|사진 수정 불가능, 내용 수정 가능, 해쉬태그 수정 가능<br>수정 후 메인페이지로 이동<br>게시글 작성자만 수정 가능|
|post|게시글관리|게시글 삭제|해당 게시글 작성자만 삭제 가능<br>삭제 후 메인페이지로 이동|
|comment|댓글관리|댓글 작성|메인페이지에서 작성 가능<br>디테일페이지에서 작성 가능|
|comment|댓글관리|댓글 수정|수정하려는 페이지에서 수정 후 해당 부분만 불러오기|
|comment|댓글관리|댓글 보기|해당 게시글 페이지에서만 출력<br>해당 댓글의 좋아요 수 출력<br>해당 댓글 좋아요 가능(토글)<br>해당 댓글 작성자, 댓글 내용 출력|
|comment|댓글관리|댓글 삭제|작성자만 삭제 가능<br>삭제 후 해당 페이지의 그 부분만 새로고침<br>대댓글도 함께 삭제|
|comment|대댓글관리|대댓글 작성|해당 글의 디테일페이지에서만 가능|
|comment|대댓글관리|대댓글 삭제|해당 글의 디테일페이지에서만 가능<br>해당 대댓글의 작성자만 삭제 가능|
|comment|대댓글관리|대댓글 수정|해당 글의 디테일페이지에서만 가능<br>해당 대댓글의 작성자만 수정 가능|
|comment|대댓글관리|대댓글 보기|해당 글의 디테일페이지에서만 가능<br>좋아요 수 출력<br>해당 대댓글 좋아요 기능(토글)|
|hash|해쉬태그|해쉬태그|검색관련된건데 추후 상의 필요<br>알고리즘 구현 필요|
