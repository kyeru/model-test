# 테스트 모델 실행

## code-fixer
- 사용자 코드 취약점을 수정하는 모델
- 실행 방법
  - code-fixer.conf에서 kafka 브로커 주소 설정
  - 별도 경로에 ModelServerTemplate 저장소를 clone하고, `ModelServerTemplate/server_template` 경로를 `code-fixer/server_template` 으로 심볼릭 링크함
  - start-code-fixer.sh 파일로 실행 (nohup 명령으로 백그라운드 실행됨)

## library-analyzer
- 라이브러리 취약점을 분석하는 모델
- 실행 방법
  - library-anaylizer.conf에서 kafka 브로커 주소 설정
  - 별도 경로에 ModelServerTemplate 저장소를 clone하고, `ModelServerTemplate/server_template` 경로를 `code-fixer/server_template` 으로 심볼릭 링크함
  - start-library-analyzer.sh 파일로 실행 (nohup 명령으로 백그라운드 실행됨)
