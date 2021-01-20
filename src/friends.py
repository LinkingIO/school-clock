# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 23:00
# @Author  : Leon
# @Email   : 1446684220@qq.com
# @File    : test.py
# @Desc    : 
# @Software: PyCharm

from WechatPCAPI import WechatPCAPI
import time
import logging
from queue import Queue
import threading


logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()


def on_message(message):
    print(message)
    queue_recved_message.put(message)


# 消息处理示例 仅供参考
def thread_handle_message(wx_inst):
    while True:
        message = queue_recved_message.get()
        print(message)
        # if 'msg' in message.get('type'):
        #     # 这里是判断收到的是消息 不是别的响应
        #     msg_content = message.get('data', {}).get('msg', '')
        #     send_or_recv = message.get('data', {}).get('send_or_recv', '')
        #     if send_or_recv[0] == '0':
        #         # 0是收到的消息 1是发出的 对于1不要再回复了 不然会无限循环回复
        #         wx_inst.send_text('filehelper', '收到消息:{}'.format(msg_content))


def main():
    wx_inst = WechatPCAPI(on_message=on_message, log=logging)
    wx_inst.start_wechat(block=True)

    while not wx_inst.get_myself():
        time.sleep(5)

    print('登陆成功')
    print(wx_inst.get_myself())

    threading.Thread(target=thread_handle_message, args=(wx_inst,)).start()

    time.sleep(10)
    wx_inst.send_text(to_user='13687903946@chatroom', msg='wechatpcapi')
    wx_inst.send_img(to_user='13687903946@chatroom', img_abspath=r'D:\project\WechatPCAPI-new\1.png')

    # {'user': 'wxid_fr8dgerdn87221', 'type': 'member::chatroom', 'data': {'chatroom_id': '19987403427@chatroom', 'wx_id': 'wxid_xg7e18am86wv32', 'wx_id_search': 'jcraftboy', 'wx_nickname': '张韬'}}
    # {'user': 'wxid_fr8dgerdn87221', 'type': 'msg::chatroom', 'data': {'data_type': '1', 'send_or_recv': '1+[Phone]', 'from_chatroom_wxid': '13687903946@chatroom', 'from_member_wxid': None, 'time': '2021-01-19 22:15:50', 'msg': 'aa', 'msg_byte_hex': '6161', 'from_chatroom_nickname': '川内四杰'}}
    # time.sleep(1)
    #
    # wx_inst.send_img(to_user='filehelper', img_abspath=r'C:\Users\Leon\Pictures\1.jpg')
    # time.sleep(1)
    #
    # wx_inst.send_file(to_user='filehelper', file_abspath=r'C:\Users\Leon\Desktop\1.txt')
    # time.sleep(1)
    #
    # wx_inst.send_gif(to_user='filehelper', gif_abspath=r'C:\Users\Leon\Desktop\08.gif')
    # time.sleep(1)
    #
    # wx_inst.send_card(to_user='filehelper', wx_id='gh_6ced1cafca19')

    # 这个是获取群具体成员信息的，成员结果信息也从上面的回调返回
    wx_inst.get_member_of_chatroom('13687903946@chatroom')

    # 新增@群里的某人的功能
    wx_inst.send_text(to_user='13687903946@chatroom', msg='等我来5杀, and @ you', at_someone='wxid_fr8dgerdn87221')
    wx_inst.send_text(to_user='13687903946@chatroom', msg='等我来5杀, and @ you', at_someone='wxid_vxn4qfzgqjv222')
    wx_inst.send_text(to_user='13687903946@chatroom', msg='等我来5杀, and @ you', at_someone='wxid_fwz9oshc4q6922')
    wx_inst.send_text(to_user='13687903946@chatroom', msg='等我来5杀, and @ you', at_someone='wxid_e8m8oe9trh7222')

    # 这个是更新所有好友、群、公众号信息的，结果信息也从上面的回调返回
    # wx_inst.update_frinds()


if __name__ == '__main__':
    main()
