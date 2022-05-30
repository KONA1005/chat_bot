'''
1. 법률상담/구조사례 url 형식만 넣어놓은거고(제대로 안쓰면 안떠서), 앞으로 다 채워넣야합니다
2. 대, 소 메뉴 작업 끝

'''

from flask import Flask, jsonify
import sys

application = Flask(__name__)

@application.route("/api/main", methods=["POST"])
# 메인2 @ 웰컴블록
def main():
    response = {
"version": "2.0",
  "template": {
    "outputs": [
      {
        "simpleText": { 
          "text": "무엇을 도와드릴까요?"
        }
      }
    ],
      
    "quickReplies": [
      {
        "messageText": "노동",
        "action": "message",
        "label": "노동",
       
      },
      {
        "messageText": "주택임대차",
        "action": "message",
        "label": "주택임대차"
      },
      {
        "messageText": "상가임대차",
        "action": "message",
        "label": "상가임대차"
      },
      {
        "messageText": "손해배상",
        "action": "message",
        "label": "손해배상" 
      },
      {
        "messageText": "민사일반",
        "action": "message",
        "label": "민사일반" 
      },
      {
        "messageText": "물권",
        "action": "message",
        "label": "물권" 
      },
      {
        "messageText": "채권",
        "action": "message",
        "label": "채권" 
      },
      {
        "messageText": "계약",
        "action": "message",
        "label": "계약" 
      },
      {                                                                                                     
        "messageText": "상사",
        "action": "message",
        "label": "상사" 
      },
      {
        "messageText": "민사소송",
        "action": "message",
        "label": "민사소송" 
      },
      {
        "messageText": "친족",
        "action": "message",
        "label": "친족" 
      },
      {
        "messageText": "상속",
        "action": "message",
        "label": "상속" 
      },
      {
        "messageText": "가사소송",
        "action": "message",
        "label": "가사소송" 
      },
      {
        "messageText": "가족관계등록",
        "action": "message",
        "label": "가족관계등록" 
      },
      {
        "messageText": "민사집행",
        "action": "message",
        "label": "민사집행" 
      },
      {
        "messageText": "보전처분",
        "action": "message",
        "label": "보전처분" 
      },
      {
        "messageText": "개인회생 파산 및 면책",
        "action": "message",
        "label": "개인회생 파산 및 면책" 
      },
      {
        "messageText": "형법",
        "action": "message",
        "label": "형법" 
      },
      {
        "messageText": "형사소송",
        "action": "message",
        "label": "형사소송" 
      },
      {
        "messageText": "행정",
        "action": "message",
        "label": "행정" 
      },
      {
        "messageText": "헌법",
        "action": "message",
        "label": "헌법" 
      },
      {
        "messageText": "채무자대리",
        "action": "message",
        "label": "채무자대리" 
      },
      {
        "messageText": "기타",
        "action": "message",
        "label": "기타" 
      },
    ]
  }
}
    return jsonify(response)

 
# 노동메뉴
@application.route("/api/workmenu", methods=["POST"])
def workmenu():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "노동관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "임금 및 퇴직금",
        "action": "message",
        "label": "임금 및 퇴직금",
       
      },
      {
        "messageText": "해고",
        "action": "message",
        "label": "해고"
      }
    ]  
  } 
}
    return jsonify(response)

## 노동 ##
# 임금 및 퇴직금
@application.route("/api/workmoney1", methods=["POST"])
def workmoney1 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"임금 및 퇴직금",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTA2/MDAxNjUzMDMwODc5ODQ1.EUMy-EeQ2fm_IOpW2RERsJALVitrqLjKF0HgI7PxUBcg.67_2LGbEl4W7iZhHNieWy-6fX2pBCGh07ytLpUIEG4wg.JPEG.sjkor1005/KakaoTalk_20220520_143036541.jpg?type=w800",
          "description":"임금 및 퇴직금청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=04efbb9252474228ab1edbbc6ddbadf1&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 해고
@application.route("/api/ufire", methods=["POST"])
def ufire ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"해고",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTA2/MDAxNjUzMDMwODc5ODQ1.EUMy-EeQ2fm_IOpW2RERsJALVitrqLjKF0HgI7PxUBcg.67_2LGbEl4W7iZhHNieWy-6fX2pBCGh07ytLpUIEG4wg.JPEG.sjkor1005/KakaoTalk_20220520_143036541.jpg?type=w800",
          "description":"해고무효확인 및 임금청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=d1d071e8060047dc8bff140c16a87163&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 주택임대차메뉴
@application.route("/api/house", methods=["POST"])
def house():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "주택임대차 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "대항력",
        "action": "message",
        "label": "대항력",
      },
      {
        "messageText": "소액임차인의 최우선변제권",
        "action": "message",
        "label": "소액임차인의 최우선변제권"
      },
      {
        "messageText": "임차보증금 · 차임 증감",
        "action": "message",
        "label": "임차보증금 · 차임 증감"
      },
      {
        "messageText": "기타 주택임대차",
        "action": "message",
        "label": "기타 주택임대차"
      },
      {
        "messageText": "임차권등기명령",
        "action": "message",
        "label": "임차권등기명령"
      }
    ]  
  } 
}
    return jsonify(response)

## 주택임대차 6개 ##
# 기타 주택임대차
@application.route("/api/etchouseimdae", methods=["POST"])
def etchouseimdae ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 주택임대차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"내용증명(주택임대차 계약해지-임대료 연체)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=946a6439c059438682db3aacc3cf8949&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 대항력
@application.route("/api/bighang", methods=["POST"])
def bighang ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"대항력",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"준비서면(건물인도, 피고)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=1f180279d663431488870a308afbce41&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소액임차인의 최우선변제권
@application.route("/api/littlemoney", methods=["POST"])
def littlemoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소액임차인의 최우선변제권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"해임차보증금반환채권 부존재확인의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=4666a423614148658c65e2139c10529d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 임차권등기명령
@application.route("/api/ordertoimcha", methods=["POST"])
def ordertoimcha ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"임차권등기명령",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"주택임차권등기명령(설명)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=8ab28448566947258db5b39cfcad2e12&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 임차보증금,차임증감
@application.route("/api/imchamoney", methods=["POST"])
def imchamoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"임차보증금, 차임 증감",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"임대료청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=e6d5a419255346eca0b2d5783adc0b7a&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 임차보증금반환
@application.route("/api/housearch", methods=["POST"])
def housearch ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"임차보증금반환",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTUy/MDAxNjUzMDMwODc5ODcw.EY3quvGq6MHJyHrcwtyHqBsYyO0YMjQgs2xLdTvi-Asg.lPA7dO-1Xc0TCYXICxf6SzkJK2q9em4Ie0rUqDM7Oo4g.JPEG.sjkor1005/KakaoTalk_20220520_143304994.jpg?type=w800",
          "description":"아파트, 맨션, 빌라 등 임대차계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=bfdad6bf254943f1b0fbbd19429f7c23&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

## 헌법 ##
# 헌법소원
@application.route("/api/constitutionappeal", methods=["POST"])
def constitutionappeal ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"헌법소원",
          "imageUrl":"data:image/png;base64,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",
          "description":"국선대리인 선임신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=7ae8b7b449724be9af42425a723195af&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=7ae8b7b449724be9af42425a723195af&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            }
          ]
        }
      ]
    },
    {
      "type":"card.image",
      "cards":[
        {
          "title":"헌법소원",
          "imageUrl":"data:image/png;base64,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",
          "description":"의견서 제출",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=7ae8b7b449724be9af42425a723195af&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=7ae8b7b449724be9af42425a723195af&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            }
          ]
        }
      ]
    }
        ]
    },
    {
      "type":"card.image",
      "cards":[
        {
          "title":"헌법소원",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MThfMTYy/MDAxNjUyODU0NDY0NzI5.i1LunqRLcMHkfVpV8j1tzGZQR-AjnE6JO-Gw3YC0gC4g.pkcpXr47IHWl0zTEhd4JRohvbSVbDRClCJL_wkZIOQ4g.JPEG.sjkor1005/%EC%9E%AC%ED%8C%90.jpg?type=w800",
          "description":"헌법소원의 종류와 그 성격",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=3e6583159a4141849945f8a41934ef7a&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=7ae8b7b449724be9af42425a723195af&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            }
          ]
        }
      ]
    }
    return jsonify(response)
    

# 위헌
@application.route("/api/unconstitutional", methods=["POST"])
def unconstitutional ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"위헌",
          "imageUrl":"data:image/png;base64,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",
          "description":"위헌법률심판제청신청",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=598153618587486184935970c51ab45b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
              {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=598153618587486184935970c51ab45b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            }
          ]
        }
      ]
    }
  ]
}
    return jsonify(response)    

################################################################################메뉴테스트으

# 헌법 메뉴
@application.route("/api/constitutionmenu", methods=["POST"])
def constitutionmenu():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "헌법 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "헌법소원",
        "action": "message",
        "label": "헌법소원",
       
      },
      {
        "messageText": "위헌법률심판",
        "action": "message",
        "label": "위헌법률심판"
      },
      {
        "messageText": "헌법재판소법",
        "action": "message",
        "label": "헌법재판소법"
      },
      {
        "messageText": "기타 헌법",
        "action": "message",
        "label": "기타 헌법"
      }
    ]  
  } 
}
    return jsonify(response)

# 채무자대리 메뉴
@application.route("/api/chmumenu", methods=["POST"])
def chmumenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "채무자 대리 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "채무자 대리",
        "action": "message",
        "label": "채무자 대리",
       
      }
    ]  
  } 
}    
    return jsonify(response)   


# 형사소송 메뉴
@application.route("/api/brothercowmenu", methods=["POST"])
def brothercowmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "형사소송 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "고소와 고발",
        "action": "message",
        "label": "고소와 고발",
       
      },
      {
        "messageText": "기타 형사절차",
        "action": "message",
        "label": "기타 형사절차"
      },
      {
        "messageText": "불기소처분 및 불복",
        "action": "message",
        "label": "불기소처분 및 불복"
      },
      {
        "messageText": "상소",
        "action": "message",
        "label": "상소"
      },
      {
        "messageText": "소년 및 가정보호사건",
        "action": "message",
        "label": "소년 및 가정보호사건"
      },
      {
        "messageText": "소송절차 및 증거",
        "action": "message",
        "label": "소송절차 및 증거"
      },
      {
        "messageText": "인신보호사건",
        "action": "message",
        "label": "인신보호사건"
      },
      {
        "messageText": "재심, 약식절차",
        "action": "message",
        "label": "재심, 약식절차"
      },
      {
        "messageText": "재판의 집행",
        "action": "message",
        "label": "재판의 집행"
      },
      {
        "messageText": "체포, 구속 및 석방, 보석",
        "action": "message",
        "label": "체포, 구속 및 석방, 보석"
      },
      {
        "messageText": "피해자변호(성폭력)",
        "action": "message",
        "label": "피해자변호(성폭력)"
      },
      {
        "messageText": "피해자변호(아동학대)",
        "action": "message",
        "label": "피해자변호(아동학대)"
      },
      {
        "messageText": "피해자변호(장애인학대)",
        "action": "message",
        "label": "피해자변호(장애인학대)"
      }
    ]  
  } 
}
    return jsonify(response)

# 행정메뉴
@application.route("/api/administrationmenu", methods=["POST"])
def administrationmenu():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "행정 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "건축 관련 행정",
        "action": "message",
        "label": "건축 관련 행정",
       
      },
      {
        "messageText": "교통 관련 행정",
        "action": "message",
        "label": "교통 관련 행정"
      },
      {
        "messageText": "기타 행정",
        "action": "message",
        "label": "기타 행정"
      },
      {
        "messageText": "난민 관련 행정",
        "action": "message",
        "label": "난민 관련 행정"
      },
      {
        "messageText": "부동산 관련 행정",
        "action": "message",
        "label": "부동산 관련 행정"
      },
      {
        "messageText": "산재 관련 행정",
        "action": "message",
        "label": "산재 관련 행정"
      },
      {
        "messageText": "영업 관련 행정",
        "action": "message",
        "label": "영업 관련 행정"
      },
      {
        "messageText": "유공자 관련 행정",
        "action": "message",
        "label": "유공자 관련 행정"
      },
      {
        "messageText": "조세 관련 행정",
        "action": "message",
        "label": "조세 관련 행정"
      },
      {
        "messageText": "행정소송일반",
        "action": "message",
        "label": "행정소송일반"
      },
      {
        "messageText": "행정 심판",
        "action": "message",
        "label": "행정 심판"
      }
    ]  
  } 
}
    return jsonify(response)

# 형법메뉴
@application.route("/api/brotherlawmenu", methods=["POST"])
def brotherlawmenu():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "행정 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "강간과 추행의 죄",
        "action": "message",
        "label": "강간과 추행의 죄",
       
      },
      {
        "messageText": "공무방해에 관한 죄",
        "action": "message",
        "label": "공무방해에 관한 죄"
      },
      {
        "messageText": "공무원의 직무에 관한 죄",
        "action": "message",
        "label": "공무원의 직무에 관한 죄"
      },
      {
        "messageText": "교통사고처리특례법 위반죄",
        "action": "message",
        "label": "교통사고처리특례법 위반죄"
      },
      {
        "messageText": "기타 범죄",
        "action": "message",
        "label": "기타 범죄"
      },
      {
        "messageText": "도로교통법 위반죄",
        "action": "message",
        "label": "도로교통법 위반죄"
      },
      {
        "messageText": "도박과 복표에 관한 죄",
        "action": "message",
        "label": "도박과 복표에 관한 죄"
      },
      {
        "messageText": "명예에 관한 죄",
        "action": "message",
        "label": "명예에 관한 죄"
      },
      {
        "messageText": "무고의 죄",
        "action": "message",
        "label": "무고의 죄"
      },
      {
        "messageText": "문서에 관한 죄",
        "action": "message",
        "label": "문서에 관한 죄"
      },
      {
        "messageText": "방화와 실화의 죄",
        "action": "message",
        "label": "방화와 실화의 죄"
      },
      {
        "messageText": "병역법 위반죄",
        "action": "message",
        "label": "병역법 위반죄"
      },
      {
        "messageText": "부정수표단속법 위반죄",
        "action": "message",
        "label": "부정수표단속법 위반죄"
      },
      {
        "messageText": "사기와 공갈의 죄",
        "action": "message",
        "label": "사기와 공갈의 죄"
      },
      {
        "messageText": "살인의 죄",
        "action": "message",
        "label": "살인의 죄"
      },
      {
        "messageText": "상해와 폭행의 죄",
        "action": "message",
        "label": "상해와 폭행의 죄"
      },
      {
        "messageText": "방화와 실화의 죄",
        "action": "message",
        "label": "방화와 실화의 죄"
      },
      {
        "messageText": "선고유예, 집행유예, 가석방",
        "action": "message",
        "label": "선고유예, 집행유예, 가석방"
      },
      {
        "messageText": "성풍속에 관한 죄",
        "action": "message",
        "label": "성풍속에 관한 죄"
      },
      {
        "messageText": "손괴의 죄",
        "action": "message",
        "label": "손괴의 죄"
      },
      {
        "messageText": "신용, 업무와 경매에 관한 죄",
        "action": "message",
        "label": "신용, 업무와 경매에 관한 죄"
      },
      {
        "messageText": "아편에 관한 죄",
        "action": "message",
        "label": "아편에 관한 죄"
      },
      {
        "messageText": "장물에 관한 죄",
        "action": "message",
        "label": "장물에 관한 죄"
      },
      {
        "messageText": "절도와 강도의 죄",
        "action": "message",
        "label": "절도와 강도의 죄"
      },
      {
        "messageText": "죄의 성립요건",
        "action": "message",
        "label": "죄의 성립요건"
      },
      {
        "messageText": "주거침입의 죄",
        "action": "message",
        "label": "주거침입의 죄"
      },
      {
        "messageText": "특정범죄가중처벌법 위반죄",
        "action": "message",
        "label": "특정범죄가중처벌법 위반죄"
      },
      {
        "messageText": "폭력행위등처벌에 관한 법률 위반죄",
        "action": "message",
        "label": "폭력행위등처벌에 관한 법률 위반죄"
      },
      {
        "messageText": "형벌",
        "action": "message",
        "label": "형벌"
      },
      {
        "messageText": "횡령과 배임의 죄",
        "action": "message",
        "label": "횡령과 배임의 죄"
      }
    ]  
  } 
}
    return jsonify(response)

# 개인회생, 파산 및 면책메뉴
@application.route("/api/personmenu", methods=["POST"])
def personmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "개인회생, 파산 및 면책 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "개인회생",
        "action": "message",
        "label": "개인회생",
       
      },
      {
        "messageText": "파산 및 면책",
        "action": "message",
        "label": "파산 및 면책",
       
      }
    ]  
  } 
}      
    return jsonify(response)  



# 보전처분 메뉴 
@application.route("/api/bojeonmenu", methods=["POST"])
def bojeonmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "보전처분 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "가압류일반",
        "action": "message",
        "label": "가압류일반",
       
      },
      {
        "messageText": "가처분",
        "action": "message",
        "label": "가처분",
       
      },
      {
        "messageText": "기타 보전처분",
        "action": "message",
        "label": "기타 보전처분",
       
      },
      {
        "messageText": "부동산가압류",
        "action": "message",
        "label": "부동산가압류",
       
      },
      {
        "messageText": "채권가압류",
        "action": "message",
        "label": "채권가압류",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 민사집행 메뉴 
@application.route("/api/minsagomenu", methods=["POST"])
def minsagomenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "민사집행 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "강제집행일반",
        "action": "message",
        "label": "강제집행일반",
       
      },
      {
        "messageText": "금전채권 강제집행",
        "action": "message",
        "label": "금전채권 강제집행",
       
      },
      {
        "messageText": "기타 강제집행",
        "action": "message",
        "label": "기타 강제집행",
       
      },
      {
        "messageText": "부동산강제집행",
        "action": "message",
        "label": "부동산강제집행",
       
      },
      {
        "messageText": "압류금지채권범위변경",
        "action": "message",
        "label": "압류금지채권범위변경",
       
      },
      {
        "messageText": "유체동산 강제집행",
        "action": "message",
        "label": "유체동산 강제집행",
       
      },
      {
        "messageText": "자동차 등 강제집행",
        "action": "message",
        "label": "자동차 등 강제집행",
       
      },
      {
        "messageText": "재산명시 및 조회 등",
        "action": "message",
        "label": "재산명시 및 조회 등",
       
      },
      {
        "messageText": "집행에 있어서 구제",
        "action": "message",
        "label": "집행에 있어서 구제",
       
      },
      {
        "messageText": "집행의 정지, 제한 및 취소",
        "action": "message",
        "label": "집행의 정지, 제한 및 취소",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 가족관계등록 메뉴 
@application.route("/api/familymenu", methods=["POST"])
def familymenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "민사집행 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "가족관계등록부정정",
        "action": "message",
        "label": "가족관계등록부정정",
       
      },
      {
        "messageText": "가족관계등록창설",
        "action": "message",
        "label": "가족관계등록창설",
       
      },
      {
        "messageText": "국적의 취득과 상실",
        "action": "message",
        "label": "국적의 취득과 상실",
       
      },
      {
        "messageText": "기타 가족관계등록",
        "action": "message",
        "label": "기타 가족관계등록",
       
      },
      {
        "messageText": "성본창설과 개명",
        "action": "message",
        "label": "성본창설과 개명",
       
      },
      {
        "messageText": "신고",
        "action": "message",
        "label": "신고",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 가사소송 메뉴 
@application.route("/api/familysomenu", methods=["POST"])
def familysomenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "가사소송 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "가,나,다류 가사소송",
        "action": "message",
        "label": "가,나,다류 가사소송",
       
      },
      {
        "messageText": "가사소송일반",
        "action": "message",
        "label": "가사소송일반",
       
      },
      {
        "messageText": "과태료와 감치",
        "action": "message",
        "label": "과태료와 감치",
       
      },
      {
        "messageText": "기타",
        "action": "message",
        "label": "기타",
       
      },
      {
        "messageText": "담보제공명령 등",
        "action": "message",
        "label": "담보제공명령 등",
       
      },
      {
        "messageText": "라,마류 가사비송",
        "action": "message",
        "label": "라,마류 가사비송",
       
      },
      {
        "messageText": "양육비직접지급명령",
        "action": "message",
        "label": "양육비직접지급명령",
       
      },
      {
        "messageText": "이행명령",
        "action": "message",
        "label": "이행명령",
       
      }
    ]  
  } 
}      
    return jsonify(response)


# 상속 메뉴 
@application.route("/api/sangsokmenu", methods=["POST"])
def sangsokmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "상속 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "기타상속",
        "action": "message",
        "label": "기타상속",
       
      },
      {
        "messageText": "상속분",
        "action": "message",
        "label": "상속분",
       
      },
      {
        "messageText": "상속순위",
        "action": "message",
        "label": "상속순위",
       
      },
      {
        "messageText": "상속일반",
        "action": "message",
        "label": "상속일반",
       
      },
      {
        "messageText": "상속재산분할",
        "action": "message",
        "label": "상속재산분할",
       
      },
      {
        "messageText": "유류분",
        "action": "message",
        "label": "유류분",
       
      },
      {
        "messageText": "유언",
        "action": "message",
        "label": "유언",
       
      },
      {
        "messageText": "한정승인 및 상속포기",
        "action": "message",
        "label": "한정승인 및 상속포기",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 친족 메뉴 
@application.route("/api/relationmenu", methods=["POST"])
def relationmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "친족 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "기타 친족",
        "action": "message",
        "label": "기타 친족",
       
      },
      {
        "messageText": "면접교섭권",
        "action": "message",
        "label": "면접교섭권",
       
      },
      {
        "messageText": "부양",
        "action": "message",
        "label": "부양",
       
      },
      {
        "messageText": "약혼",
        "action": "message",
        "label": "약혼",
       
      },
      {
        "messageText": "양육비",
        "action": "message",
        "label": "양육비",
       
      },
      {
        "messageText": "이혼 및 위자료",
        "action": "message",
        "label": "이혼 및 위자료",
       
      },
      {
        "messageText": "이혼 및 재산분할청구권",
        "action": "message",
        "label": "이혼 및 재산분할청구권",
       
      },
      {
        "messageText": "인지 등",
        "action": "message",
        "label": "인지 등",
       
      },
      {
        "messageText": "입양, 파양, 친양자",
        "action": "message",
        "label": "입양, 파양, 친양자",
       
      },
      {
        "messageText": "재판상이혼 등",
        "action": "message",
        "label": "재판상이혼 등",
       
      },
      {
        "messageText": "친권",
        "action": "message",
        "label": "친권",
       
      },
      {
        "messageText": "친생자",
        "action": "message",
        "label": "친생자",
       
      },
      {
        "messageText": "협의이혼",
        "action": "message",
        "label": "협의이혼",
       
      },
      {
        "messageText": "혼인의 성립, 무효, 취소",
        "action": "message",
        "label": "혼인의 성립, 무효, 취소",
       
      },
      {
        "messageText": "후견인",
        "action": "message",
        "label": "후견인",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 민사소송 메뉴 
@application.route("/api/minsasosongmenu", methods=["POST"])
def minsasosongmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "민사소송 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "간이소송절차",
        "action": "message",
        "label": "간이소송절차",
       
      },
      {
        "messageText": "관할",
        "action": "message",
        "label": "관할",
       
      },
      {
        "messageText": "기타 민사소송",
        "action": "message",
        "label": "기타 민사소송",
       
      },
      {
        "messageText": "당사자",
        "action": "message",
        "label": "당사자",
       
      },
      {
        "messageText": "상소",
        "action": "message",
        "label": "상소",
       
      },
      {
        "messageText": "소송비용",
        "action": "message",
        "label": "소송비용",
       
      },
      {
        "messageText": "소송비용상대방상환",
        "action": "message",
        "label": "소송비용상대방상환",
       
      },
      {
        "messageText": "소송절차",
        "action": "message",
        "label": "소송절차",
       
      },
      {
        "messageText": "재심",
        "action": "message",
        "label": "재심",
       
      },
      {
        "messageText": "증거",
        "action": "message",
        "label": "증거",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 상사 메뉴 
@application.route("/api/bossmenu", methods=["POST"])
def bossmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "상사 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "기타 상사",
        "action": "message",
        "label": "기타 상사",
       
      },
      {
        "messageText": "보험",
        "action": "message",
        "label": "보험",
       
      },
      {
        "messageText": "상사일반",
        "action": "message",
        "label": "상사일반",
       
      },
      {
        "messageText": "어음,수표",
        "action": "message",
        "label": "어음,수표",
       
      },
      {
        "messageText": "회사",
        "action": "message",
        "label": "회사",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 계약메뉴 
@application.route("/api/trademenu", methods=["POST"])
def trademenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "계약 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "계약금",
        "action": "message",
        "label": "계약금",
       
      },
      {
        "messageText": "계약의 해지 해제",
        "action": "message",
        "label": "계약의 해지 해제",
       
      },
      {
        "messageText": "계약 일반",
        "action": "message",
        "label": "계약 일반",
       
      },
      {
        "messageText": "기타 계약",
        "action": "message",
        "label": "기타 계약",
       
      },
      {
        "messageText": "대여금 등",
        "action": "message",
        "label": "대여금 등",
       
      },
      {
        "messageText": "도급",
        "action": "message",
        "label": "도급",
       
      },
      {
        "messageText": "매매",
        "action": "message",
        "label": "매매",
       
      },
      {
        "messageText": "부동산중개",
        "action": "message",
        "label": "부동산중개",
       
      },
      {
        "messageText": "여행계약",
        "action": "message",
        "label": "여행계약",
       
      },
      {
        "messageText": "위임",
        "action": "message",
        "label": "위임",
       
      },
      {
        "messageText": "임대차",
        "action": "message",
        "label": "임대차",
       
      },
      {
        "messageText": "조합과 계",
        "action": "message",
        "label": "조합과 계",
       
      },
      {
        "messageText": "할부거래 및 방문판매,신용카드",
        "action": "message",
        "label": "할부거래 및 방문판매,신용카드",
       
      },
      {
        "messageText": "화해",
        "action": "message",
        "label": "화해",
       
      }
    ]  
  } 
}      
    return jsonify(response)

#  채권메뉴 
@application.route("/api/chaemenu", methods=["POST"])
def chaemenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "채권 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "기타 채권",
        "action": "message",
        "label": "기타 채권",
       
      },
      {
        "messageText": "부당이득",
        "action": "message",
        "label": "부당이득",
       
      },
      {
        "messageText": "연대채무,보증채무",
        "action": "message",
        "label": "연대채무,보증채무",
       
      },
      {
        "messageText": "채권양도",
        "action": "message",
        "label": "채권양도",
       
      },
      {
        "messageText": "채권의 소멸(공탁 등)",
        "action": "message",
        "label": "채권의 소멸(공탁 등)",
       
      },
      {
        "messageText": "채권자대위권",
        "action": "message",
        "label": "채권자대위권",
       
      },
      {
        "messageText": "채권자취소권",
        "action": "message",
        "label": "채권자취소권",
       
      },
      {
        "messageText": "채무인수",
        "action": "message",
        "label": "채무인수",
       
      }
    ]  
  } 
}      
    return jsonify(response)


# 물권 메뉴 
@application.route("/api/mulmenu", methods=["POST"])
def mulmenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "물권 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "공동소유",
        "action": "message",
        "label": "공동소유",
       
      },
      {
        "messageText": "기타 물권",
        "action": "message",
        "label": "기타 물권",
       
      },
      {
        "messageText": "물권의 변동(부동산등기 등)",
        "action": "message",
        "label": "물권의 변동(부동산등기 등)",
       
      },
      {
        "messageText": "상린관계",
        "action": "message",
        "label": "상린관계",
       
      },
      {
        "messageText": "소유권",
        "action": "message",
        "label": "소유권",
       
      },
      {
        "messageText": "소유권에 기한 물권적 청구권",
        "action": "message",
        "label": "소유권에 기한 물권적 청구권",
       
      },
      {
        "messageText": "유치권과 질권",
        "action": "message",
        "label": "유치권과 질권",
       
      },
      {
        "messageText": "저당권",
        "action": "message",
        "label": "저당권",
       
      },
      {
        "messageText": "점유권",
        "action": "message",
        "label": "점유권",
       
      },
      {
        "messageText": "지상권과 전세권",
        "action": "message",
        "label": "지상권과 전세권",
       
      },
      {
        "messageText": "취득시효",
        "action": "message",
        "label": "취득시효",
       
      
      }
    ]  
  } 
}      
    return jsonify(response)


# 민사일반 메뉴 
@application.route("/api/minsa1menu", methods=["POST"])
def minsa1menu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "민사일반 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "대리",
        "action": "message",
        "label": "대리",
       
      },
      {
        "messageText": "법률행위일반",
        "action": "message",
        "label": "법률행위일반",
       
      },
      {
        "messageText": "부재, 실종",
        "action": "message",
        "label": "부재, 실종",
       
      },
      {
        "messageText": "소멸시효",
        "action": "message",
        "label": "소멸시효",
       
      },
      {
        "messageText": "제한능력자",
        "action": "message",
        "label": "제한능력자",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 손해배상 메뉴 
@application.route("/api/sonbaemenu", methods=["POST"])
def sonbaemenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "손해배상 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "공해",
        "action": "message",
        "label": "공해",
       
      },
      {
        "messageText": "국가배상",
        "action": "message",
        "label": "국가배상",
       
      },
      {
        "messageText": "기타 손해배상",
        "action": "message",
        "label": "기타 손해배상",
       
      },
      {
        "messageText": "범죄피해",
        "action": "message",
        "label": "범죄피해",
       
      },
      {
        "messageText": "불법사금융(보이스피싱)",
        "action": "message",
        "label": "불법사금융(보이스피싱)",
       
      },
      {
        "messageText": "산재사고",
        "action": "message",
        "label": "산재사고",
       
      },
      {
        "messageText": "성폭력피해(데이트)",
        "action": "message",
        "label": "성폭력피해(데이트)",
       
      },
      {
        "messageText": "성폭력피해(스토킹)",
        "action": "message",
        "label": "성폭력피해(스토킹)",
       
      },
      {
        "messageText": "성폭력피해(일반)",
        "action": "message",
        "label": "성폭력피해(일반)",
       
      },
      {
        "messageText": "소비자피해",
        "action": "message",
        "label": "소비자피해",
       
      },
      {
        "messageText": "손해배상 일반",
        "action": "message",
        "label": "손해배상 일반",
       
      },
      {
        "messageText": "아동학대",
        "action": "message",
        "label": "아동학대",
       
      },
      {
        "messageText": "의료과오",
        "action": "message",
        "label": "의료과오",
       
      },
      {
        "messageText": "자동차사고",
        "action": "message",
        "label": "자동차사고",
       
      },
      {
        "messageText": "지적소유권",
        "action": "message",
        "label": "지적소유권",
       
      },
      {
        "messageText": "학교폭력피해",
        "action": "message",
        "label": "학교폭력피해",
       
      }
    ]  
  } 
}      
    return jsonify(response)

# 상가임대차메뉴 
@application.route("/api/sanggamenu", methods=["POST"])
def sanggamenu ():
    response = {
    "version": "2.0",
        "template": {
            "outputs": [
            {
            "simpleText": {
                "text": "상가임대차 관련 정보입니다. 어떤정보가 필요하신가요?"
                        }
            }
        ],
     "quickReplies": [
      {
        "messageText": "계약갱신요구",
        "action": "message",
        "label": "계약갱신요구",
       
      },
      {
        "messageText": "권리금",
        "action": "message",
        "label": "권리금",
       
      },
      {
        "messageText": "기타 상가임대차",
        "action": "message",
        "label": "기타 상가임대차",
       
      },
      {
        "messageText": "대항력",
        "action": "message",
        "label": "대항력",
       
      },
      {
        "messageText": "상가임대차분쟁조정",
        "action": "message",
        "label": "상가임대차분쟁조정",
       
      },
      {
        "messageText": "소액임차인의 최우선변제권",
        "action": "message",
        "label": "소액임차인의 최우선변제권",
       
      },
      {
        "messageText": "우선변제권",
        "action": "message",
        "label": "우선변제권",
       
      },
      {
        "messageText": "임대차기간",
        "action": "message",
        "label": "임대차기간",
       
      },
      {
        "messageText": "임차권등기명령",
        "action": "message",
        "label": "임차권등기명령",
       
      },
      {
        "messageText": "임차보증금, 차임 증감",
        "action": "message",
        "label": "임차보증금, 차임 증감",
       
      },
      {
        "messageText": "임차보증금반환",
        "action": "message",
        "label": "임차보증금반환",
       
      },
      {
        "messageText": "적용범위",
        "action": "message",
        "label": "적용범위",
       
      }
    ]  
  } 
}      
    return jsonify(response)



## 상사 4개##
# 보험
@application.route("/api/insurance", methods=["POST"])
def insurance ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"보험",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjA2/MDAxNjUzMDMwODgwMTcx.HhfDspigEvB6ky1xD5RxziSXOTSM_TcWYTJ4QyJ6uHsg.ebAd2cZDyG93MCvCjMpKtcAytYC0mzPUAAkczGOiVAUg.JPEG.sjkor1005/KakaoTalk_20220520_151423054.jpg?type=w800",
          "description":"보험금청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=3056af8cbf5b453b87cf18a6135a81aa&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 상사일반
@application.route("/api/boss1ban", methods=["POST"])
def boss1ban ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상사일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjA2/MDAxNjUzMDMwODgwMTcx.HhfDspigEvB6ky1xD5RxziSXOTSM_TcWYTJ4QyJ6uHsg.ebAd2cZDyG93MCvCjMpKtcAytYC0mzPUAAkczGOiVAUg.JPEG.sjkor1005/KakaoTalk_20220520_151423054.jpg?type=w800",
          "description":"대리점계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a9a7f89d46ec4f618a245a22156fbf4b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 어음수표
@application.route("/api/umm", methods=["POST"])
def umm ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"어음, 수표",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjA2/MDAxNjUzMDMwODgwMTcx.HhfDspigEvB6ky1xD5RxziSXOTSM_TcWYTJ4QyJ6uHsg.ebAd2cZDyG93MCvCjMpKtcAytYC0mzPUAAkczGOiVAUg.JPEG.sjkor1005/KakaoTalk_20220520_151423054.jpg?type=w800",
          "description":"약속어음금청구의 소(백지어음)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=5c0c7e9a0036487d9dd018e86f84f3d5&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 회사
@application.route("/api/hell", methods=["POST"])
def hell ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"회사",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjA2/MDAxNjUzMDMwODgwMTcx.HhfDspigEvB6ky1xD5RxziSXOTSM_TcWYTJ4QyJ6uHsg.ebAd2cZDyG93MCvCjMpKtcAytYC0mzPUAAkczGOiVAUg.JPEG.sjkor1005/KakaoTalk_20220520_151423054.jpg?type=w800",
          "description":"주식회사 이사해임의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=c697b65e6b244867abcdf02431eebf48&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 채권 7개 ##
# 기타 채권
@application.route("/api/etcchaekwon", methods=["POST"])
def etcchaekwon ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 채권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"영농보상금수령권 확인의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=106e4a26c4304a6c9c1629d5e847db85&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)
  

# 부당이득
@application.route("/api/budang2", methods=["POST"])
def budang2 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부당이득",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"반소장(부당이득금 반환청구)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=c6642bd16d5a4059a32d2950873bcf6e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)
  

# 연대채무, 보증채무
@application.route("/api/imchaemu", methods=["POST"])
def imchaemu ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"연대채무, 보증채무",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"구상금청구의 소(물상보증인)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=42ba2c2ee62b450584c3d3821828689a&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 채권양도
@application.route("/api/sheepdo", methods=["POST"])
def sheepdo ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"채권양도",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"양수금청구의 소(공사대금 양수)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=2230876c63d4497a82d16c93d8f98d19&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 채권의 소멸(공탁 등)
@application.route("/api/chaekwonbye", methods=["POST"])
def chaekwonbye ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"채권의 소멸(공탁 등)",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"공탁금출급권자확인의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=af177e2f45e34ff2903b4fa2b6d4cfe0&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 채권자취소권
@application.route("/api/cancel", methods=["POST"])
def cancel ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"채권자취소권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"사해행위취소 및 원상회복청구",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=812c114274594a7a98d4fa89457dbef2&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

  
# 채무인수
@application.route("/api/getchaemu", methods=["POST"])
def getchaemu ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"채무인수",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTYy/MDAxNjUzMDMwODgwMDgw.SpODrctWrmDHis_fyHHsusm4fBwt2TqIpSgdsr9LHQEg.df0zpJdbNfZD7NWnKI2UgTFrpfCuI6G-MQZKQNROKwwg.JPEG.sjkor1005/KakaoTalk_20220520_150734939.jpg?type=w800",
          "description":"면책적 채무인수계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=86ebd0ff40ab4b8fb5d22229351d3229&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)



## 계약 12개 ##
# 계약금
@application.route("/api/cmoney", methods=["POST"])
def cmoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"계약금",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"준비서면(계약금 등 반환, 원고)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=63dc1783490d4f54948a9a9163d4068a&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 계약의 해지 해제
@application.route("/api/cbye", methods=["POST"])
def cbye ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"계약의 해지 해제",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"소유권이전등기말소청구의 소(교환계약 해제)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=79fd77050eb24b9b96dc52ac211b033c&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타계약
@application.route("/api/etccontract", methods=["POST"])
def etccontract ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 계약",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"특허궈늬 토상실시권 설정계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=d073959f5dcf4bbdb66fbd9d4d1613e1&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 대여금 등
@application.route("/api/loan", methods=["POST"])
def loan ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"대여금 등",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"대여금청구의 소(연대보증인이 있는 경우)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=59b8c03c78f54092bc2fa3ee895ca9ed&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 도급
@application.route("/api/subcontract", methods=["POST"])
def subcontract ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"도급",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"임가공료청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=ef25e8a71b554a4fa436f84b903f38ce&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 매매
@application.route("/api/dealing", methods=["POST"])
def dealing ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"매매",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"물품대금청구의 소(식료품)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=0fe786099b7948cbbd437d265529cf9f&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 부동산중개
@application.route("/api/mediation", methods=["POST"])
def mediation ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부동산중개",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"중개업자의 손해배상",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=85c3aaea03e24a90af02a4c96cbcd75e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 위임
@application.route("/api/mandate", methods=["POST"])
def mandate ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"위임",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"위임계약서(일반)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=d47d3e6476e443d88b67e43d96d5af0b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 임대차
@application.route("/api/imdaecar", methods=["POST"])
def imdaecar ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"임대차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"임대차계약서(자동차)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=caf2b60185e5456babacd3bd2cb6fdf3&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 조합과 계
@application.route("/api/johab", methods=["POST"])
def johab ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"조합과 계",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"계금청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=eb916a5069634445b8a01e06268c2ff4&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 할부거래 및 방문판매, 신용카드
@application.route("/api/credit", methods=["POST"])
def credit ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"할부,방문판매,신용카드",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"미성년자가 체결한 계약의 청약 철회 신고서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=1a7b9a3eb90543ab81c8bac67a764a6b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 화해
@application.route("/api/reconcilaition", methods=["POST"])
def reconciliation ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"화해",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjcg/MDAxNjUzMDMwODgwMTU5.1l_mDrtY9go2_fXu2ANXs18-v7xMrX_paFPOy9lRrd8g.2wBf9mPasQgjyeGUxUYhTSEFlwswCN2AysUTC5CVyCcg.JPEG.sjkor1005/KakaoTalk_20220520_150956609.jpg?type=w800",
          "description":"화해계약서(교통사고, 물적손해)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=d64d4b47a8fa47c8b3c2add0fddaac6a&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)



## 민사소송 9개 ##
# 간이소송절차
@application.route("/api/minsagan2", methods=["POST"])
def minsagan2 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"간이소송절차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"이행권고결정에 대한 이의신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a2a35250575a40649d40bc3c4d1cab99&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 관할
@application.route("/api/gwanhal", methods=["POST"])
def gwanhal ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"관할",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"관할합의서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=dee05a3678fb4b2e958e42ab37f45c46&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타민사소송
@application.route("/api/etcminsa1", methods=["POST"])
def etcminsa1 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 민사소송",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"법관기피신청 기각결정에 대한 즉시항고장",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=16821f48f7d6481b8154ec105b97e1c4&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 당사자
@application.route("/api/danglion", methods=["POST"])
def danglion ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"당사자",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"특별대리인 개임신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=59d4a3311b0945f5872f76fe82086cc5&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 상소
@application.route("/api/minsaupcow", methods=["POST"])
def minsaupcow ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상소",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"항소이유서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=3f1531d32c104a90a9e7f911d7a51ff4&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소송비용
@application.route("/api/sosongmoney", methods=["POST"])
def sosongmoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소송비용",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"소송비용액확정결정신청서(일부부담)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=dd532d971c3f46f6b0b5d51ffc846317&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소송절차
@application.route("/api/sosongmenual", methods=["POST"])
def sosongmenual ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소송절차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"공시송달신청서(소장제출과 함께)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=303afb98da0d4f58b22b61f84532f0ca&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 재심
@application.route("/api/againsim", methods=["POST"])
def againsim ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"재심",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"재심소장",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6e341607e4094388b3b90cfc1ad0319b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 증거
@application.route("/api/evidence", methods=["POST"])
def evidence ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"증거",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjIg/MDAxNjUzMDMwODgwMjE2.RqQvY3VzGJHDEqXaCg7jU38YyUfHCCZ4nIUwd1b1m1wg.NfuKVSzVeiLNA5eQ0uQxdMzXmam8rnC_vdjAdmS2_Gog.JPEG.sjkor1005/KakaoTalk_20220520_151958512.jpg?type=w800",
          "description":"사실조회신청서(노동청)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=afba03e0a5184e608b6f646373533bfd&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 물권 10개 ##
# 공동소유
@application.route("/api/togethermul", methods=["POST"])
def togethermul ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"공동소유",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"소유권이전등기(공유자전원 지분전부이전)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=8143c36542934ddfbf5fbc81acba3f7e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타물권
@application.route("/api/etcmulkwon", methods=["POST"])
def etcmulkwon ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 물권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"양도담보계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=69a02bf0301c4983a1bb0741c7f73e57&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 물권의 변동(부동산등기 등)
@application.route("/api/mulchange", methods=["POST"])
def mulchange ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"물권의 변동(부동산등기 등)",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"건물멸시등기신청",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=5871291ef3bb41eea60fcd5cf046ee4c&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 상린관계
@application.route("/api/sangrin", methods=["POST"])
def sangrin ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상린관계",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"대지경계확정의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=bb5fc18495624428baf3c6ddd4fb8cf2&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소유권
@application.route("/api/cowyou", methods=["POST"])
def cowyou ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소유권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"소유권보존등기(대위)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=f2e5074835d44f2199da9aad309050ac&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소유권에 기한 물권적 청구권
@application.route("/api/cowyoumul", methods=["POST"])
def cowyoumul ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소유권에 기한 물권적 청구권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"준비서면(건물 등 철거, 피고)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=fe294aa2e3b14e2a96a36a0ebfa866a3&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 저당권
@application.route("/api/jeodang", methods=["POST"])
def jeodang ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"저당권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"근저당권말소등기의 회복등기절차이행청구 등의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=f0341e53f91145a3bde72bb70c80e7d3&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 점유권
@application.route("/api/jeomu", methods=["POST"])
def jeomu ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"점유권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"점유보유의 소(점유권에 기한 방해배제청구)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=530bec9d1ef746f5879720a5df987d8d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

  
# 지상권과 전세권
@application.route("/api/onkwon", methods=["POST"])
def onkwon ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"지상권과 전세권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"전세권설정등기신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6b5c1e0024104c56a9c6b6a549ee5834&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

  
# 취득시효
@application.route("/api/sihyo", methods=["POST"])
def sihyo ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"취득시효",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDYg/MDAxNjUzMDMwODgwMDQz.ZEtfPtFJWuk8x2S5CJmzC4bKDq69JDLSCCAzsfCRMo0g.LXLYL_ULYoJK4dlRIMMV22ACLf-I4WDiCOt_8bbV0Rsg.JPEG.sjkor1005/KakaoTalk_20220520_150455625.jpg?type=w800",
          "description":"소우권이전등기청구의 소(국유 일반재산 점유취득)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=680c3a79f5d741ef905ed904b9bf29d1&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 형사소송 10개 ##
# 고소 고발
@application.route("/api/secret", methods=["POST"])
def secret ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"고소 고발",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"비밀침해죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=3065a00610474992afb8026fa8c98579&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타 형사절차
@application.route("/api/etcbrothersa", methods=["POST"])
def etcbrothersa ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 형사절차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"사건이송신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=fe603e0c56b243cf87aa81883594cd77&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 불기소처분 및 불복
@application.route("/api/firecow", methods=["POST"])
def firecow ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"불기소처분 및 불복",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"항고장(검사의 불기소처분)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=323fb110b58140b08785ddebca353891&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 상소
@application.route("/api/upso", methods=["POST"])
def upso ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상소",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"상고이유서(절도)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=ea42d1df5643497b8edccb448765e42e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소년 및 가정보호사건
@application.route("/api/boyand", methods=["POST"])
def boyand ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소년 및 가정보호사건",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"위탁변경신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=96689c6c47ca40e489e3c791a6299847&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 소송절차 및 증거
@application.route("/api/sosongevidence", methods=["POST"])
def sosongevidence ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소송절차 및 증거",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"증언거부사유서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=c32fd44538264ecb9d0a0c170c5dc39c&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 인신보호사건
@application.route("/api/insinboho", methods=["POST"])
def insinboho ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"인신보호사건",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"구제청구서(수용시설)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=d487c1185c6d46998bc4309bb1aecea2&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 재심, 약식절차
@application.route("/api/jaesimmanual", methods=["POST"])
def jaesimmanual ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"재심, 약식절차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"재심청구서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=db3c9dacff134600a961b3e6010a05c4&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 재판의 집행
@application.route("/api/jibhang", methods=["POST"])
def jibhang ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"재판의 집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"재판 집행에 관한 이의신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=b9531b7551254f44814d1d92017179db&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 체포구속및 석방 보석
@application.route("/api/arrest", methods=["POST"])
def arrest ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"체포,구속,석방,보석",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNjgg/MDAxNjUzMDMwODgwNzYy.JqA5JKUj0wdzNYRJmvANWzEIiUP22iXPuPImaV9GOUgg.ke6InpeEZd5hd5fWK-f1hKG7kg8kT4FpqphN6ufWwlQg.JPEG.sjkor1005/KakaoTalk_20220520_160327703.jpg?type=w800",
          "description":"보석조건변경신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=4f0e0ac50d33469bb16dd2ac823cbc19&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)




## 형법 12개 ##
# 강간과 추행의 죄
@application.route("/api/rape", methods=["POST"])
def rape ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"강간과 추행의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"강제추행죄(고소장)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=9b6e21f08b234ae3881f84ded8b05119&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 공무방해에 관한 죄
@application.route("/api/banghae", methods=["POST"])
def banghae ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"공무방해에 관한 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"공부상비밀표시무효죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=f8d92e85bad147b4ad85e3c7ba5565f2&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 공무원의 직무에 관한 죄
@application.route("/api/gongmu1", methods=["POST"])
def gongmu1 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"공무원의 직무에 관한 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"폭행가혹행위죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=fc69c4897e854f348deb4fa7e95dbd4b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 과실치사상의 죄
@application.route("/api/fruit", methods=["POST"])
def fruit ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"과실치사상의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"업무상과실치상죄(의료사고)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=8efc67a42e8144b8b1d6bcd2abd5746c&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 교통사고처리특례법 위반죄
@application.route("/api/gyotong", methods=["POST"])
def gyotong ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"교통사고처리특례법 위반죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"중앙선침범",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a9315a6e019f4f65b70829ca50c572fa&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 명예에 관한 죄
@application.route("/api/myungyeah", methods=["POST"])
def myungyeah ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"명예에 관한 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"명예훼손죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a5c6b090bf1b4aceb144c728ed6ea48e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 무고의 죄
@application.route("/api/mugo", methods=["POST"])
def mugo ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"무고의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"무고죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6750342bc2bc4cbebc611e66c4c1fd98&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 문서에 관한 죄
@application.route("/api/doorup", methods=["POST"])
def doorup ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"문서에 관한 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"사문서위조죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=3ae3437ed5aa4ef18647d7c2cd910f5a&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 방화와 실화의 죄
@application.route("/api/fire", methods=["POST"])
def fire ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"방화와 실화의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"방화죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=2879bc6143d64418b6c34314850fcd09&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 사기와 공갈의 죄
@application.route("/api/cheater", methods=["POST"])
def cheater ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"사기와 공갈의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"사기죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=4faa1fbc091440c7b6aa4e404eae1518&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 살인의 죄
@application.route("/api/murder", methods=["POST"])
def murder ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"살인의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"위계에 의한 살인미수죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=50ab631c1e214e9780a309f599101f0c&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 상해와 폭행의 죄
@application.route("/api/hit", methods=["POST"])
def hit ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상해와 폭행의 죄",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfNDkg/MDAxNjUzMDMwODgwNzY3.q2zxowJ7byvF3ZSN0Uj7WguAaP_-g-2brbLJdolaDlwg.-MTnx2yqFMDIjckwXpAqUsdMLBlwv7OiFfcMzDHMqJwg.JPEG.sjkor1005/KakaoTalk_20220520_160557016.jpg?type=w800",
          "description":"폭행죄",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=d9b6d04839054b7a9153567584ae0a38&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 손해배상 9개 ##
# 공해
@application.route("/api/gonghae", methods=["POST"])
def gonghae ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"공해",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(공)청구의 소(기름유출)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=1ca4d95e091048f88d3d89d77797854c&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 기타 손해배상
@application.route("/api/etccompensation", methods=["POST"])
def etccompensation ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타손해배상",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"반론보도청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=114a8ab958f74df59c5796668a30ef51&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 범죄피해
@application.route("/api/criminal", methods=["POST"])
def criminal ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"범죄피해",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(공)청구의 소(기름유출)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=b508eb76287e4cd3b3a37ed1927097a8&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 불법사금융(보이스피싱)
@application.route("/api/voice", methods=["POST"])
def voice ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"불법사금융(보이스피싱)",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(기) 청구의 소(보이스 피싱)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=98b1343a8c184250962e515526d07900&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 산재사고
@application.route("/api/accident", methods=["POST"])
def accident ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"산재사고",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(산)청구의 소(안전시설 미비, 공동불법행위)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=503222927ec04e3d994db89d9d8995a7&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 성폭력피해(일반)
@application.route("/api/violence", methods=["POST"])
def violence ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"성폭력피해(일반)",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":" 손해배상(기)청구의 소(강간)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=5de0c82c32744d468f2c8a11c001caad&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 의료과오
@application.route("/api/doctor", methods=["POST"])
def doctor ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"의료과오",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(의)청구의 소(출산 중 사고, 장해발생, 채무불이행책임)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=b8b795af34f14e1fa6b8d2d8ad77d92e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 자동차사고
@application.route("/api/car", methods=["POST"])
def car ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"자동차사고",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(자)청구의 소(미성년 남자고등학생, 부상)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=8c68bcf559604b98aabb56f8c7036f4a&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 지적소유권
@application.route("/api/ownership", methods=["POST"])
def ownership ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"지적소유권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjI1/MDAxNjUzMDMwODc5ODk1.MyrLpEd4CufvgwFR1E2c_zl34r8wxUz1bEvXvRvSKw4g.0KsSmolLQZ5DHjO3TrSW92WC2opmmnUGgcx0MhN-CwUg.JPEG.sjkor1005/KakaoTalk_20220520_145354742.jpg?type=w800",
          "description":"손해배상(의)청구의 소(출산 중 사고, 장해발생, 채무불이행책임)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6e3623012c174f578c6050a0f4d2b6a0&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)



## 친족 6개 ##
# 입양,파양,친양자 / 재판상이혼 / 친권 / 친생자 / 협의이혼 / 혼인의성립~/후견인 없음
# 면접교섭권
@application.route("/api/meetplz", methods=["POST"])
def meetplz ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"면접교섭권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"면접교섭허가 심판청구서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=ed45cc25fdda44e4a5cde8df9833ef9e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 부양
@application.route("/api/parent", methods=["POST"])
def parent ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부양",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"부양료청구 조정신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=290b1ad4b25d4d79a57a8c61b0224d50&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 약혼
@application.route("/api/yakkon", methods=["POST"])
def yakkon ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"약혼",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"약혼예물 반환 조정신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=863a8b3dbb4149b1845c0742f2b8f516&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 양육비
@application.route("/api/childmoney", methods=["POST"])
def childmoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"양육비",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"양육비 심판청구서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=555b0fc204824375b24a50c1a5e69f75&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 이혼및 위자료
@application.route("/api/devomoney", methods=["POST"])
def devomoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"이혼 및 위자료",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"이혼 및 위자료 조정신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=bb70c798c7bf40df8f812cc24c2a195f&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 이혼및 재산분할청구권
@application.route("/api/devoshare", methods=["POST"])
def devoshare ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"이혼 및 재산분할청구권",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjg2/MDAxNjUzMDMwODgwMjIz.evmsQvzTJJHw88iTdE4SDZp9XievJ6k1eZruPGcdhXQg.mZlyYt1WRcFovI8goChh2ilqjPibqlD4CCrlkGtQbMAg.JPEG.sjkor1005/KakaoTalk_20220520_152145221.jpg?type=w800",
          "description":"재산분할 심판청구서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=fe88f43be2b64f5397cf8c09e9e0867f&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)



## 가족관계등록 4개 ##
# 가족관계등록부정정
@application.route("/api/fchange", methods=["POST"])
def fchange ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가족관계등록부 정정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjE5/MDAxNjUzMDMwODgwNTE2.tCYAFhpraHU57yBETLnAF2SdM7_J7tGpTDN8Cin5RLMg.Nn_zF964R9YTUY1-_qvJ2h7XJpWIUiD6jQ1aztVXsCQg.JPEG.sjkor1005/KakaoTalk_20220520_153418176.jpg?type=w800",
          "description":"등록부정정허가신청서(성전환자)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=235720e1733642548825f7ff3de66af3&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 가족관계등록창설
@application.route("/api/fmake", methods=["POST"])
def fmake ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가족관계등록창설",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjE5/MDAxNjUzMDMwODgwNTE2.tCYAFhpraHU57yBETLnAF2SdM7_J7tGpTDN8Cin5RLMg.Nn_zF964R9YTUY1-_qvJ2h7XJpWIUiD6jQ1aztVXsCQg.JPEG.sjkor1005/KakaoTalk_20220520_153418176.jpg?type=w800",
          "description":"가족관계등록 창설허가신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=12386bdb7f6e4d51bf9d7fb99e8edd2e&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 국적의 취득과 상실
@application.route("/api/nation", methods=["POST"])
def nation ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"국적의 취득과 상실",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjE5/MDAxNjUzMDMwODgwNTE2.tCYAFhpraHU57yBETLnAF2SdM7_J7tGpTDN8Cin5RLMg.Nn_zF964R9YTUY1-_qvJ2h7XJpWIUiD6jQ1aztVXsCQg.JPEG.sjkor1005/KakaoTalk_20220520_153418176.jpg?type=w800",
          "description":"국적취득 신고서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=4c379d83a33246c783dabefd51bcaad0&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 신고
@application.route("/api/tell", methods=["POST"])
def tell ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"신고",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjE5/MDAxNjUzMDMwODgwNTE2.tCYAFhpraHU57yBETLnAF2SdM7_J7tGpTDN8Cin5RLMg.Nn_zF964R9YTUY1-_qvJ2h7XJpWIUiD6jQ1aztVXsCQg.JPEG.sjkor1005/KakaoTalk_20220520_153418176.jpg?type=w800",
          "description":"혼인신고서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=be2804c5d70a44a0bac42444b0bc3ff5&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)




## 가사소송 4개 ##
# 가,나,다류 가사소송
@application.route("/api/fsosong", methods=["POST"])
def fsosong ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가,나,다류 가사소송",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM0/MDAxNjUzMDI5NjMyODcz.4TEg-GKjBWl1vgbI0LPzPNUZYj2or1DOpZI1atSRCz4g.UPU82fFQ2VMXF9QJZ4lOBhNsXUJSmHRMDSqeVt7hJ9Mg.JPEG.sjkor1005/KakaoTalk_20220520_153001826.jpg?type=w800",
          "description":"친자 감정신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=ff068b02e97644aba8aef53bcc93f6e8&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}           
 
    return jsonify(response)


# 가사소송 일반
@application.route("/api/fsosong1ban", methods=["POST"])
def fsosong1ban ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가사소송 일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM0/MDAxNjUzMDI5NjMyODcz.4TEg-GKjBWl1vgbI0LPzPNUZYj2or1DOpZI1atSRCz4g.UPU82fFQ2VMXF9QJZ4lOBhNsXUJSmHRMDSqeVt7hJ9Mg.JPEG.sjkor1005/KakaoTalk_20220520_153001826.jpg?type=w800",
          "description":"불거주확인서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=fb7b61b987674c52a91469bf858df174&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 과태료와 감치
@application.route("/api/gamchi", methods=["POST"])
def gamchi ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"과태료와 감치",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM0/MDAxNjUzMDI5NjMyODcz.4TEg-GKjBWl1vgbI0LPzPNUZYj2or1DOpZI1atSRCz4g.UPU82fFQ2VMXF9QJZ4lOBhNsXUJSmHRMDSqeVt7hJ9Mg.JPEG.sjkor1005/KakaoTalk_20220520_153001826.jpg?type=w800",
          "description":"감치명령신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=cb3a8e0e03f346a28f12951a0903fafb&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타
@application.route("/api/etcfsosong", methods=["POST"])
def etcfsosong ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM0/MDAxNjUzMDI5NjMyODcz.4TEg-GKjBWl1vgbI0LPzPNUZYj2or1DOpZI1atSRCz4g.UPU82fFQ2VMXF9QJZ4lOBhNsXUJSmHRMDSqeVt7hJ9Mg.JPEG.sjkor1005/KakaoTalk_20220520_153001826.jpg?type=w800",
          "description":"유아인도 조정신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=ba3790215f434f41a3b85e06ce83f27d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)





## 행정 11개 ##
# 건축관련 행정
@application.route("/api/archhaeng", methods=["POST"])
def archhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"건축 관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"건축공사 중지명령처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=ee54a98ae08b41d9bd4663e86eb13aeb&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    },
    {
      "type":"card.image",
      "cards":[
        {
          "title":"건축 관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"건축 불허가처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=f252ab0af9f342c6a0a88a4433da0259&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
        ]
    }
    return jsonify(response)


# 교통관련 행정
@application.route("/api/carhaeng", methods=["POST"])
def carhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"교통 관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"자동차 운전면허취소처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=873af615f5b74926a7b5e7022e543647&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}    
    return jsonify(response)


# 기타행정
@application.route("/api/etchaeng", methods=["POST"])
def etchaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"해임처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=330034a7a382431da7300061bbf22c07&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    },
    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"부당해고 구제재심판정 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=330034a7a382431da7300061bbf22c07&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}
    return jsonify(response)


# 난민관련 행정
@application.route("/api/nanminhaeng", methods=["POST"])
def nanminhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"난민관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"난민불인정처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=7b78de1409604bd492c257aa174731ac&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
            
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 부동산 관련 행정
@application.route("/api/budongsanhaeng", methods=["POST"])
def budongsanhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부동산관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"손실보상금 청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=4112ed0b667a42ef987b8c1afbaf34db&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
            
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 산재 관련 행정
@application.route("/api/sanjaehaeng", methods=["POST"])
def sanjaehaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"산재관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"장해등급 결정처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=01cad21d29f74a7a8821c0dc34610318&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 영업관련 행정
@application.route("/api/up0haeng", methods=["POST"])
def up0haeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"영업관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"영업정지처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=bb634e95b0c644b1934aa33b11152b99&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 유공자관련 행정
@application.route("/api/honorhaeng", methods=["POST"])
def honorhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"유공자관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"전공상 불인정처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=960c1d0d7eb74cc982ae684248c2df28&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 조세관련 행정
@application.route("/api/jobirdhaeng", methods=["POST"])
def jobirdhaeng ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"조세관련 행정",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"양도소득세 부과처분 취소청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=4f0ceb1fe865455dbfb56ebf04a5d24b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 행정소송일반
@application.route("/api/haeng1ban", methods=["POST"])
def haeng1ban ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"행정소송 일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"행정소송의 관할",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=409f83265f1447b59b945ed9b2b833ca&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 행정심판
@application.route("/api/haengsimpan", methods=["POST"])
def haengsimpan ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"행정심판",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTM5/MDAxNjUzMDMwODgwOTA5.uXUwMxhaiAAZgM-gQswiIucIUn42L7ZMo_J53F0Zvcgg.8tXS2tRV4QPePUQ5ivRb1dC6EdRKlPawUT69Q7JSGtAg.JPEG.sjkor1005/KakaoTalk_20220520_160826196.jpg?type=w800",
          "description":"행정심판의 대상",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=46fb32db882d468bbb312f5ed9a635a4&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)






## 민사일반 4개 ##
# 대리
@application.route("/api/daeri", methods=["POST"])
def daeri ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"대리",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTU0/MDAxNjUzMDMwODc5OTA3.v9zTR-h9yigO1D0rbGoed9fsEtb5-NWuIU_3KSwCSR4g.bTsEYl7VXy-tHwh74Yz9P4sb2BYvarUndbuVbqlLTPMg.JPEG.sjkor1005/KakaoTalk_20220520_145831643.jpg?type=w800",
          "description":"소유권이전등기말소청구의 소(토지, 사실혼관계 처의 무권대리)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=5d3a8340bf954464bf7bbd636bb67a43&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 법률행위일반
@application.route("/api/legalact", methods=["POST"])
def legalact ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"법률행위일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTU0/MDAxNjUzMDMwODc5OTA3.v9zTR-h9yigO1D0rbGoed9fsEtb5-NWuIU_3KSwCSR4g.bTsEYl7VXy-tHwh74Yz9P4sb2BYvarUndbuVbqlLTPMg.JPEG.sjkor1005/KakaoTalk_20220520_145831643.jpg?type=w800",
          "description":"소유권이전등기말소청구의 소(토지, 제3자의 문서위조)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=3d06d353018d4898a412e7bf9f4682e9&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 소멸시효
@application.route("/api/somuel", methods=["POST"])
def somuel ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"소멸시효",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTU0/MDAxNjUzMDMwODc5OTA3.v9zTR-h9yigO1D0rbGoed9fsEtb5-NWuIU_3KSwCSR4g.bTsEYl7VXy-tHwh74Yz9P4sb2BYvarUndbuVbqlLTPMg.JPEG.sjkor1005/KakaoTalk_20220520_145831643.jpg?type=w800",
          "description":"소멸시효 일람표",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=a056d39ec9c54494abd62d3a437694e9&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 제한능력자
@application.route("/api/limitperson", methods=["POST"])
def limitperson ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"제한능력자",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMTU0/MDAxNjUzMDMwODc5OTA3.v9zTR-h9yigO1D0rbGoed9fsEtb5-NWuIU_3KSwCSR4g.bTsEYl7VXy-tHwh74Yz9P4sb2BYvarUndbuVbqlLTPMg.JPEG.sjkor1005/KakaoTalk_20220520_145831643.jpg?type=w800",
          "description":"내용증명(계약취소-미성년자 할부구입 책)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=380f5091e1f84e1bae1f08d7c5f1d889&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


## 민사집행 8개 ##
# 강제집행일반
@application.route("/api/must1", methods=["POST"])
def must1 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"강제집행일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"간접강제신청",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=0dea66c6160247f5aa46cb55258b74fe&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 금전채권 강제집행
@application.route("/api/moneymust", methods=["POST"])
def moneymust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"금전채권 강제집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"채권압류 및 전부명령신청",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=fea0855b66244f0aa9fceba966dbb700&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 기타강제집행
@application.route("/api/etcmust", methods=["POST"])
def etcmust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 강제집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"특별현금화 매각명령신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=bfe129d2e3664ceb86db11b932281eae&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 부동산강제집행
@application.route("/api/budongmust", methods=["POST"])
def budongmust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부동산 강제집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"배당요구신청서(임금채권)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=ccfb9c1030ed4be4abe7ec41b62343ab&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 압류금지채권범위변경
@application.route("/api/takemust", methods=["POST"])
def takemust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"압류금지채권범위변경",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"압류금지채권",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=592d95f14edf4762b175f2f202e9e49b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 유체동산 강제집행
@application.route("/api/ucmust", methods=["POST"])
def ucmust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"유체동산 강제집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"유체동산 강제집행신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=1864d15538f3451a81d0efcd6ee27e97&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 자동차 등 강제집행
@application.route("/api/carmust", methods=["POST"])
def carmust ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"자동차 등 강제집행",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM0/MDAxNjUzMDMwODgwNTY1.TDf0TP5ijzmF-3RJ8RIPuMUnM6H8jJspL7ZaoDUX35Yg.yWKCWZtgEgqpfBfhxqWBqTqeDp7zFM8tjYp0lmQjmVYg.JPEG.sjkor1005/KakaoTalk_20220520_153817905.jpg?type=w800",
          "description":"자동차강제경매신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=d758d8dd68614dd0aaa8e254d6a1658f&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)






## 개인회생, 파산 및 면책 1개 ##
# 개인회생
@application.route("/api/helpme", methods=["POST"])
def helpme ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"개인회생",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjM5/MDAxNjUzMDMwNDkxMzI2.mw9I9Yn8AMXIJC15zroBt8pDN1Te6ScBjvr7KfUdqtUg.G07FlXifiRFTI8cYA-QbrXtq_-dl1zgrhWRoNbvB6MEg.JPEG.sjkor1005/KakaoTalk_20220520_160122483.jpg?type=w800",
          "description":"회생채권확정의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=b66294524454458cbad8389613e3376d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)



## 보전처분 5개 ##
# 가압류 일반
@application.route("/api/ga1", methods=["POST"])
def ga1 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가압류일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjk0/MDAxNjUzMDI5NzczMTE0.3OdTgt-gnsE1CVodM3Q9Mevo4XEPOc2Uu1-Tu3n2FQQg.x5Dl1E1-r0Cx0Sd6cXYUqU5DUAhBxVoiQOQk3SnWfTMg.JPEG.sjkor1005/KakaoTalk_20220520_155419064.jpg?type=w800",
          "description":"제소신고서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=776ec8da030f4850aadbc443b3175943&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 가처분
@application.route("/api/gacheo", methods=["POST"])
def gacheo ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"가처분",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjk0/MDAxNjUzMDI5NzczMTE0.3OdTgt-gnsE1CVodM3Q9Mevo4XEPOc2Uu1-Tu3n2FQQg.x5Dl1E1-r0Cx0Sd6cXYUqU5DUAhBxVoiQOQk3SnWfTMg.JPEG.sjkor1005/KakaoTalk_20220520_155419064.jpg?type=w800",
          "description":"가처분취소신청서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=f37d911010bc4314910c6f28e68296ce&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)
  
# 기타 보전처분
@application.route("/api/etcbojeon", methods=["POST"])
def etcbojeon ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"기타 보전처분",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjk0/MDAxNjUzMDI5NzczMTE0.3OdTgt-gnsE1CVodM3Q9Mevo4XEPOc2Uu1-Tu3n2FQQg.x5Dl1E1-r0Cx0Sd6cXYUqU5DUAhBxVoiQOQk3SnWfTMg.JPEG.sjkor1005/KakaoTalk_20220520_155419064.jpg?type=w800",
          "description":"자동차가압류명령신청",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=3f7cfc4fa01b4ddba7ecd827a600d5e3&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 부동산가압류
@application.route("/api/budonggab", methods=["POST"])
def budonggab ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"부동산 가압류",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjk0/MDAxNjUzMDI5NzczMTE0.3OdTgt-gnsE1CVodM3Q9Mevo4XEPOc2Uu1-Tu3n2FQQg.x5Dl1E1-r0Cx0Sd6cXYUqU5DUAhBxVoiQOQk3SnWfTMg.JPEG.sjkor1005/KakaoTalk_20220520_155419064.jpg?type=w800",
          "description":"부동산가압류신청(대여금)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=77db759fa81d4db3943cf528632907a1&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 채권가압류
@application.route("/api/moneyab", methods=["POST"])
def moneyab ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"채권가압류 신청서",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjk0/MDAxNjUzMDI5NzczMTE0.3OdTgt-gnsE1CVodM3Q9Mevo4XEPOc2Uu1-Tu3n2FQQg.x5Dl1E1-r0Cx0Sd6cXYUqU5DUAhBxVoiQOQk3SnWfTMg.JPEG.sjkor1005/KakaoTalk_20220520_155419064.jpg?type=w800",
          "description":"임금채권으로 강제집행정지 담보의 공탁금 회수청구권",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=b7c980a2196a4ba984498ad02995a078&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

## 상가임대차 4개 
# 계약갱신요구
@application.route("/api/trade", methods=["POST"])
def trade ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"계약갱신요구",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjkx/MDAxNjUzMDMwODc5ODg3.3EVvHKAnyDlmCGm2n_NIXoF7wVdyM5al8r03NOY0Wgcg.0sIceL3Kx94iWUn3P_E60nI7G8TzxWxA4OLhY2_MraMg.JPEG.sjkor1005/KakaoTalk_20220520_143646617.jpg?type=w800",
          "description":"최고서(상가임대차계약 갱신권 요구 주장)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=5022727ee2af42248744d116d3c78721&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 권리금
@application.route("/api/premium", methods=["POST"])
def premium ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"권리금",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjkx/MDAxNjUzMDMwODc5ODg3.3EVvHKAnyDlmCGm2n_NIXoF7wVdyM5al8r03NOY0Wgcg.0sIceL3Kx94iWUn3P_E60nI7G8TzxWxA4OLhY2_MraMg.JPEG.sjkor1005/KakaoTalk_20220520_143646617.jpg?type=w800",
          "description":"권리금반환청구의 소(계약기간내 계약해지할 때 권리금반환특약)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=cdb849d1961a4f01b7c61025c96783ad&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 기타 상가임대차
@application.route("/api/etcsanga", methods=["POST"])
def etcsanga ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상가임대차",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjkx/MDAxNjUzMDMwODc5ODg3.3EVvHKAnyDlmCGm2n_NIXoF7wVdyM5al8r03NOY0Wgcg.0sIceL3Kx94iWUn3P_E60nI7G8TzxWxA4OLhY2_MraMg.JPEG.sjkor1005/KakaoTalk_20220520_143646617.jpg?type=w800",
          "description":"건물인도 등 청구의 소(월임차료 체불, 상가 일부)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=21c32d53ed4a4d639b3688572d13ab3d&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 임차보증금반환
@application.route("/api/lentfee", methods=["POST"])
def lentfee ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"임차보증금반환",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfMjkx/MDAxNjUzMDMwODc5ODg3.3EVvHKAnyDlmCGm2n_NIXoF7wVdyM5al8r03NOY0Wgcg.0sIceL3Kx94iWUn3P_E60nI7G8TzxWxA4OLhY2_MraMg.JPEG.sjkor1005/KakaoTalk_20220520_143646617.jpg?type=w800",
          "description":"일반점포의 임대차계약서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=5050d04f0f714e59ac042f414abf2e3a&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)



## 상속 5개 ##
# 상속분
@application.route("/api/sangsokbun", methods=["POST"])
def sangsokbun ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상속분",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfOTUg/MDAxNjUzMDI5NjMyODU3.1Dh9bxVQwl9deoON_ta_JchXrUz76KWAL3G390owC3kg.-iwx2S2SfxlyeiUzN-tgfz5UMybYWKlvXIUV9XCTjQcg.JPEG.sjkor1005/KakaoTalk_20220520_152344382.jpg?type=w800",
          "description":"소유권이전등기신청서(상속)",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=c07b6df1fcd2422eb81913f63f824cf2&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 상속일반
@application.route("/api/sangsok1", methods=["POST"])
def sangsok1 ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상속일반",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfOTUg/MDAxNjUzMDI5NjMyODU3.1Dh9bxVQwl9deoON_ta_JchXrUz76KWAL3G390owC3kg.-iwx2S2SfxlyeiUzN-tgfz5UMybYWKlvXIUV9XCTjQcg.JPEG.sjkor1005/KakaoTalk_20220520_152344382.jpg?type=w800",
          "description":"상속인수색의 공고청구서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6c1f3255693f48d4a427a95ef0f49754&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 상속재산분할
@application.route("/api/sangsokmoney", methods=["POST"])
def sangsokmoney ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"상속재산분할",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfOTUg/MDAxNjUzMDI5NjMyODU3.1Dh9bxVQwl9deoON_ta_JchXrUz76KWAL3G390owC3kg.-iwx2S2SfxlyeiUzN-tgfz5UMybYWKlvXIUV9XCTjQcg.JPEG.sjkor1005/KakaoTalk_20220520_152344382.jpg?type=w800",
          "description":"상속재산분할협의서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=8d4997b94f914571ac49045a1e525c7b&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)

# 유류분
@application.route("/api/uryu", methods=["POST"])
def uryu ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"유류분",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfOTUg/MDAxNjUzMDI5NjMyODU3.1Dh9bxVQwl9deoON_ta_JchXrUz76KWAL3G390owC3kg.-iwx2S2SfxlyeiUzN-tgfz5UMybYWKlvXIUV9XCTjQcg.JPEG.sjkor1005/KakaoTalk_20220520_152344382.jpg?type=w800",
          "description":"유류분반환청구의 소",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=6ccba14a0f424a2fa86b22ed7afed755&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)


# 유언
@application.route("/api/dietell", methods=["POST"])
def dietell ():
    response = {
        "contents" : [

    {
      "type":"card.image",
      "cards":[
        {
          "title":"유언",
          "imageUrl":"https://mblogthumb-phinf.pstatic.net/MjAyMjA1MjBfOTUg/MDAxNjUzMDI5NjMyODU3.1Dh9bxVQwl9deoON_ta_JchXrUz76KWAL3G390owC3kg.-iwx2S2SfxlyeiUzN-tgfz5UMybYWKlvXIUV9XCTjQcg.JPEG.sjkor1005/KakaoTalk_20220520_152344382.jpg?type=w800",
          "description":"자필증서에 의한 유언증서",
          "linkUrl": {},
          "buttons":[
            {
              "type":"url",
              "label":"법률서식",
              "data":{
                "url":"https://viewer.klac.or.kr/SynapDocViewServer/viewer/doc.html?key=bcafc09884714483a2e1d974ac3e9726&convType=img&convLocale=ko_KR&contextPath=/SynapDocViewServer"
              }
            },
            {
              "type":"url",
              "label":"법률상담/구조사례",
              "data":{
                "url":"https://casenote.kr/"
              }
            }
          ]
        }
      ]
    }
  ]
}  
    return jsonify(response)







if __name__ == "__main__":
    application.run(host='0.0.0.0', port = int(sys.argv[1]), debug = True)