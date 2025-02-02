# 🖧 Project #1 - 이더넷 러닝 스위치

## 📌 개요
이 프로젝트는 **Python과 Switchyard**를 활용하여 다양한 학습 방식의 이더넷 러닝 스위치를 구현하는 실습 프로젝트입니다.  
기본적인 러닝 스위치부터 **타임아웃(TimeOut), LRU(Least Recently Used), LTV(Least Traffic Volume)** 알고리즘을 적용한 네 가지 버전의 스위치를 개발하였습니다.  
이를 통해 네트워크 트래픽 최적화 및 패킷 전달 효율성을 학습할 수 있습니다.

---

## ⚙️ 기능 설명

### 1️⃣ 기본 러닝 스위치 (`myswitch-1-BasicSwitch.py`)
- 패킷의 **출발지 MAC 주소를 학습**하고 해당 포트를 저장.
- 목적지 MAC 주소를 기반으로 패킷을 전달하거나, 알 수 없는 경우 **브로드캐스트(플러딩)** 수행.
- **MAC 주소 테이블을 관리**하여 불필요한 패킷 전달을 최소화.

### 2️⃣ 타임아웃 적용 러닝 스위치 (`myswitch-2-TimeOut.py`)
- 기본 러닝 스위치 기능에 **MAC 주소 학습 정보를 일정 시간(10초) 후 자동 삭제**하는 기능 추가.
- **오래된 MAC 주소 제거**를 통해 불필요한 메모리 사용을 방지하고, 동적 네트워크 환경에서도 효율적인 운영 가능.

### 3️⃣ LRU 알고리즘 적용 러닝 스위치 (`myswitch-3-LRU.py`)
- **최대 MAC 주소 저장 개수를 2개**로 제한하고, **가장 오랫동안 사용되지 않은 MAC 주소를 삭제**하는 방식 적용.
- 자주 사용되는 MAC 주소를 유지하여 **네트워크 성능을 최적화**.

### 4️⃣ LTV 알고리즘 적용 러닝 스위치 (`myswitch-4-LTV.py`)
- **MAC 주소별 트래픽 볼륨을 저장**하고, 가장 적은 트래픽을 발생시킨 MAC 주소를 제거.
- **더 자주 사용되는 MAC 주소가 유지되도록 설계**, 효율적인 네트워크 트래픽 관리 가능.

---

## 🚀 실행 방법

Switchyard 환경에서 각 스크립트를 실행하여 테스트할 수 있습니다.

```bash
$ python3 myswitch-1-BasicSwitch.py  # 기본 러닝 스위치 실행
$ python3 myswitch-2-TimeOut.py      # 타임아웃 적용 러닝 스위치 실행
$ python3 myswitch-3-LRU.py          # LRU 알고리즘 적용 러닝 스위치 실행
$ python3 myswitch-4-LTV.py          # LTV 알고리즘 적용 러닝 스위치 실행
```

---

## 📝 배운 점
- 러닝 스위치의 **기본 개념 및 MAC 주소 학습 원리**를 이해하였습니다.
- 다양한 알고리즘 **(LRU, LTV 등)을 네트워크 환경에서 적용**하는 방법을 학습하였습니다.
- **Switchyard를 활용한 네트워크 패킷 처리 및 시뮬레이션 경험**을 쌓을 수 있었습니다.

---

## 📚 참고 자료
- Switchyard 공식 문서: [https://github.com/ustadmobile/switchyard](https://github.com/ustadmobile/switchyard)
- MAC 주소 학습 및 네트워크 스위칭 개념: [https://en.wikipedia.org/wiki/Learning_switch](https://en.wikipedia.org/wiki/Learning_switch)
- Least Recently Used (LRU) 캐싱 알고리즘: [https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU))
- Least Traffic Volume (LTV) 개념 및 적용 사례

