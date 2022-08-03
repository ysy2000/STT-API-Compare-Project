# STT-API-Compare-Project

### repository 설명
 - 본 repo는 회의음성에 대해 어떤 STT API의 성능이 가장 좋을지에 대해 
 
### 실험에 사용한 open source STT API
 - 실험에는 총 5가지의 STT API가 사용했다.
 - Naver CLOVA Speech, Google Cloud, AWS Transcribe, KT 지니 Dictation, ETRI STT API

### 실험에 사용한 데이터
 - 3명의 화자가 회의를 하는 음성을 녹음하고 이중 일부 문장을 실험에 사용했다.
 - 회의 환경은 zoom을 이용한 온라인 회의 환경이다.
 - sampling rate: 16000Hz
 - file type: wav file
 
### 실험 결과
 - 실험 결과는 5가지 API비교.pdf와 최종 API비교.pdf에서 볼 수 있다.
 - 가장 성능이 좋은 open source API는 naver CLOVA로 판단할 수 있다.

### 가상환경
 - myenv 폴더에는 실험에 사용한 가상환경이 담겨있다.
