# STT-API-Compare-Project

### repository 설명
 - 본 repo는 회의음성에 대해 어떤 STT API의 성능이 가장 좋을지에 대해 탐구한 결과다.
 
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
 - CER/result.csv에서 최종 API비교.pdf의 각 문장에 대한 cer결과를 확인할 수 있다.
 - 평균 CER과 만점(CER이 0인 경우)의 개수를 구한 결과는 CER/result_final.csv에서 확인할 수 있다.

### CER
 - CER은 Levenshtein거리를 이용하여 구했고 이 과정은 CER/CER.py에 담겨있다.
 - CER 계산 시 문장부호는 모두 제거한 후 계산했다.

### 가상환경
 - myenv 폴더에는 실험에 사용한 가상환경이 담겨있다.
