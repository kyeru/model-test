#!/usr/bin/python3

import sys
import os
import time


# submodule 패키지를 인식하도록 sys path에 경로 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ModelServerTemplate'))


from server_template import main


def library_analyze_func(request_message):
    time.sleep(1)
    report = '''
    [
      { "key": "lib-a-1.0", "name": "lib-a", "version": "1.0", "status": "ok" },
      { "key": "lib-b-2.0", "name": "lib-b", "version": "2.0", "status": "vulnerable" }
    ]
    '''
    return 'success', '', report


if __name__ == '__main__':
    # 모델 실행 함수를 인자로 전달
    main.server_init(library_analyze_func)
