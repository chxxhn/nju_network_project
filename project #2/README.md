# Project #2 - ARP 요청 처리 라우터

이 프로젝트는 Python과 Switchyard 프레임워크를 사용하여 **ARP 요청을 처리하는 IPv4 라우터**를 구현한 것입니다.  
라우터는 ARP 요청을 처리하고 응답하며, 학습된 MAC 주소를 캐싱하여 성능을 향상시킵니다.

## 📌 프로젝트 개요
본 프로젝트는 Switchyard를 이용하여 네트워크 환경에서 동작하는 **ARP Request 처리 기능**을 갖춘 라우터를 개발하는 것입니다.  
라우터는 **정적 라우팅 기반**으로 동작하며, ARP 요청을 학습하여 **캐싱된 MAC 주소를 활용**할 수 있도록 설계되었습니다.

---

## ⚙️ 기능 설명

### 1️⃣ 기본 ARP 요청 처리 (`myrouter_handle_arp_req_local.py`)
- ARP 요청을 수신하면, 해당 요청이 **라우터 자신의 IP를 묻는 경우**에만 응답합니다.
- ARP Reply를 생성하여 요청을 보낸 단말에게 **MAC 주소를 알려줍니다**.

### 2️⃣ ARP 요청 + 캐싱 기능 (`myrouter_handle_arp_req_cache.py`)
- 기존 ARP 요청 처리 기능에 **MAC 주소 학습 기능을 추가**하였습니다.
- ARP 요청을 수신할 때마다 **송신자의 IP-MAC 주소를 저장**하여, 동일한 요청이 다시 들어오면 **빠르게 응답할 수 있습니다**.
- 저장된 MAC 주소는 ARP Reply 응답에 활용됩니다.

---

## 🛠️ 실행 방법

### 1️⃣ Mininet을 이용한 네트워크 환경 구성
```bash
$ sudo python ./start_mininet.py
```

### 2️⃣ 라우터 코드 실행
```bash
$ sudo python myrouter_handle_arp_req_local.py
```

### 3️⃣ 테스트 코드 실행
```bash
$ python router_tests_handle_arp_req_local.py
$ python router_tests_handle_arp_req_cache.py
```

---

## 📝 배운 점 

### ✅ 배운 점
- Switchyard 프레임워크를 활용하여 **네트워크 패킷을 직접 제어하는 경험**을 할 수 있었습니다.
- ARP 프로토콜의 동작 방식과 **IP-MAC 주소 변환 원리**를 실습을 통해 학습하였습니다.
- 캐싱을 활용하여 **라우터의 성능을 개선하는 방법**을 익혔습니다.

---

## 📚 참고 자료
- [Switchyard 공식 문서](https://jsommers.github.io/switchyard/)
- [ARP 프로토콜 설명](https://support.hpe.com/techhub/eginfolib/networking/docs/switches/5130ei/5200-3942_l3-ip-svcs_cg/content/483572224.htm)
- [Wisconsin 대학교 네트워크 프로젝트](https://pages.cs.wisc.edu/~seanm/projects/)
