import requests
from test_plus import TestCase

from mailing.views import send_email


class MailingTest(TestCase):
    EMAIL_REST_URL_FOR_TEST = 'https://sh8.email/rest/mail/'

    def test_send_email(self):
        recipients = ['9xd_test1@sh8.email', '9xd_test2@sh8.email']
        mail_data = {
            'subject': 'There is new 9xd meetup',
            'recipients': recipients,
            'text': 'Yeah new meet up is always welcome.',
            'html': html_data,
        }
        send_email(mail_data)
        for recipient in recipients:
            r = requests.get(
                self.EMAIL_REST_URL_FOR_TEST + recipient.split('@')[0] + '/list')
            self.assertEquals(r.status_code, 200)
            self.assertIn(r.text, mail_data['subject'])


html_data = '''<article class="markdown-body entry-content" itemprop="text"><table data-table-type="yaml-metadata">
  <thead>
  <tr>
  <th>layout</th>

  <th>title</th>

  <th>desc</th>

  <th>keywords</th>

  <th>date</th>

  <th>categories</th>

  <th>tags</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><div>post</div></td>

  <td><div>[제 3회] 9X년생 개발자 모임</div></td>

  <td><div>이제 갓 회사에 입사한 신입, 이게 내 길이 맞나 고민 중인 컴공과 학생, 혹은 이미 현업에서 열심히 달리고 있는 개발자. 험난한 IT 업계에서 9x년생들이 살아남는 이야기를 공유합시다. 나와 같은 직군인 또래의 이야기를 듣고, 새로운 영감과 자극을 받았으면 합니다. 또한 IT업계에서 중요한 ‘커뮤니티 활동’에 한 발자욱 더 다가가는 계기가 되었으면 합니다.</div></td>

  <td><div>9XD, 개발자, 모임</div></td>

  <td><div>2016-12-02</div></td>

  <td><div><table>
  <tbody>
  <tr>
  <td><div>meetup</div></td>
  </tr>
  </tbody>
</table></div></td>

  <td><div><table>
  <tbody>
  <tr>
  <td><div>blog</div></td>
  </tr>
  </tbody>
</table></div></td>
  </tr>
  </tbody>
</table>

<p><a href="https://camo.githubusercontent.com/9f351e8725054272400707ae3d6ab8bf69bc6545/687474703a2f2f692e696d6775722e636f6d2f763675794868312e706e67" target="_blank"><img src="https://camo.githubusercontent.com/9f351e8725054272400707ae3d6ab8bf69bc6545/687474703a2f2f692e696d6775722e636f6d2f763675794868312e706e67" alt="Imgur" data-canonical-src="http://i.imgur.com/v6uyHh1.png" style="max-width:100%;"></a></p>

<h1><a id="user-content-공지" class="anchor" href="#공지" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>공지</h1>

<p>장소는 강남역 2번출구 메리츠타워 16층 D2 Startup Factory입니다.</p>

<p>7:00~7:30 사이에 등록이니 그 사이에 오셔서 </p>

<p>프레시코드의 샐러드 &amp; 커피라디오의 아이스커피, 그리고 참가기념품을 받아 착석해주시면 됩니다.</p>

<p>(늦게 오시면 수량이 부족할 수 있는 점을 양해해주시기 바랍니다)</p>

<p>그리고 모임이 종료된 9:30에는 뒷풀이 장소로 이동할 예정인데,</p>

<p>참석하시는 분들은 현금 10,000원을 준비해주시기 바랍니다.</p>

<h2><a id="user-content-모임-설명" class="anchor" href="#모임-설명" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>모임 설명</h2>

<p>이제 갓 회사에 입사한 신입, 이게 내 길이 맞나 고민 중인 컴공과 학생, 혹은 이미 현업에서 열심히 달리고 있는 개발자. 험난한 IT 업계에서 9x년생들이 살아남는 이야기를 공유합시다. 나와 같은 직군인 또래의 이야기를 듣고, 새로운 영감과 자극을 받았으면 합니다. 또한 IT업계에서 중요한 ‘커뮤니티 활동’에 한 발자욱 더 다가가는 계기가 되었으면 합니다.</p>

<p>네트워킹 시간을 위해 자신을 소개할 수 있는 어떤것(명함, 포트폴리오 등)을 준비해오세요!</p>

<h2><a id="user-content-발표자-지원" class="anchor" href="#발표자-지원" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>발표자 지원</h2>

<p>발표자에게는 5분~10분동안 발표할 자리가 주어집니다. 회사 생활, 현재 하는 고민 등 '9x년생 개발자'와 관련있는 주제라면 무엇이든 좋으니 <a href="mailto:jayjinjay@gmail.com">jayjinjay@gmail.com</a>으로 자유롭게 문의 바랍니다.</p>

<p>(* 발표자 마감되었습니다)</p>

<h2><a id="user-content-장소" class="anchor" href="#장소" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>장소</h2>

<p>강남역 2번출구 메리츠타워 16층 D2 Startup Factory</p>

<h3><a id="user-content-후원" class="anchor" href="#후원" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>후원</h3>

<p>Naver D2
 / 참가기념품, 장소</p>

<p>이상한모임
 / 출퇴근 머그컵, 월간이모 교환권</p>

<p>캡슐코퍼레이션
 / 굿즈</p>

<p>사이냅소프트
 / 자금</p>

<p>지앤선
 / 개발 도서</p>

<p>배달의민족
 / 배달의민족 굿즈</p>

<p>커피라디오(메모지닷컴)
 / 커피</p>

<p>프레시코드
/ 샐러드 도시락</p>

<h3><a id="user-content-주최" class="anchor" href="#주최" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>주최</h3>

<p>9X년생 개발자 모임</p>

<ul>
<li><p><a href="https://www.facebook.com/groups/1565641083693087">페이스북 그룹</a></p></li>
<li><p><a href="http://www.slideshare.net/jayjin0427/2-9x-60633380">모임 소개 슬라이드</a></p></li>
</ul>

<p>[3회 모임]</p>

<p>모임: <a href="http://onoffmix.com/event/68393">http://onoffmix.com/event/68393</a></p>

<p>키노트: <a href="http://www.slideshare.net/jayjin0427/3-9x">http://www.slideshare.net/jayjin0427/3-9x</a></p>

<p>사진: <a href="https://goo.gl/photos/iizT5G4UtmuBGe">https://goo.gl/photos/iizT5G4UtmuBGe</a></p>
</article>'''
