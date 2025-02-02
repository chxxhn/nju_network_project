# nju_network_project - Project #1

## 개요
이 프로젝트는 Python과 Switchyard를 활용하여 다양한 학습 방식의 이더넷 러닝 스위치를 구현합니다. 기본적인 러닝 스위치부터 타임아웃, LRU(Least Recently Used), LTV(Least Traffic Volume) 알고리즘을 적용한 고급 스위치까지 네 가지 버전을 개발하였습니다.


## 기능 설명
### 1. 기본 러닝 스위치 (myswitch-1-BasicSwitch.py)
- 패킷의 출발지 MAC 주소를 학습하고 입력 포트를 기록함.
- 목적지 MAC 주소를 기반으로 패킷을 전달하거나 알 수 없는 경우 브로드캐스트(플러딩) 수행.
- MAC 주소 학습 테이블을 관리하여 네트워크 성능을 향상.

### 2. 타임아웃 적용 러닝 스위치 (myswitch-2-TimeOut.py)
- 기본 러닝 스위치 기능에 MAC 주소 학습 정보를 일정 시간(10초) 후 자동 삭제하는 기능 추가.
- 오래된 MAC 주소를 제거하여 불필요한 메모리 사용을 방지함.

### 3. LRU 알고리즘 적용 러닝 스위치 (myswitch-3-LRU.py)
- 최대 MAC 주소 저장 개수를 2개로 제한하고, 가장 오랫동안 사용되지 않은 MAC 주소를 삭제.
- 네트워크에서 자주 사용되는 MAC 주소가 유지되도록 하여 효율적인 패킷 전달을 가능하게 함.

### 4. LTV 알고리즘 적용 러닝 스위치 (myswitch-4-LTV.py)
- MAC 주소별 트래픽 볼륨을 저장하고, 가장 적은 트래픽을 발생시킨 MAC 주소를 삭제.
- 네트워크 내에서 더 자주 사용되는 MAC 주소가 유지되도록 함.

## 실행 방법
Switchyard 환경에서 각 스크립트를 실행하여 테스트할 수 있습니다.

```
$ python3 myswitch-1-BasicSwitch.py
$ python3 myswitch-2-TimeOut.py
$ python3 myswitch-3-LRU.py
$ python3 myswitch-4-LTV.py
```

## 배운 점
- 러닝 스위치의 기본 개념 및 MAC 주소 학습 원리 이해.
- 다양한 알고리즘(LRU, LTV 등)을 네트워크 환경에서 적용하는 방법 학습.
- Switchyard를 활용한 네트워크 패킷 처리 및 시뮬레이션 경험.


