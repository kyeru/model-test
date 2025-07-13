#!/usr/bin/python3

import sys
import os
import time


# submodule 패키지를 인식하도록 sys path에 경로 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'ModelServerTemplate'))


from server_template import main


def code_fix_func(request_message):
    time.sleep(1)
    report = '''
    {
      "fixed_code": "def logout(request):\n    \"\"\" Clears the session and logs the current user out. \"\"\"\n    request.user_logout()\n    # FIXME(gabriel): we don't ship a view named splash\n    return shortcuts.redirect('splash')"
      }
    '''
    return 'success', '', report


if __name__ == '__main__':
    # 모델 실행 함수를 인자로 전달
    main.server_init(code_fix_func)
