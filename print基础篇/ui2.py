
"""
python3 + uiautomator2 + weditor框架：
http://www.gaohaiyan.com/2338.html

"""
import uiautomator2 as u2

def send_gift():
    d = u2.connect('8CFX1NX8P')
    #d.app_stop_all()
    #d.app_start("lita.funbit_android")
    #app_info = d.app_info("lita.funbit.android")
    #点击进入聊天列表
    d.xpath('//*[@resource-id="com.funbit.android:id/tabFloatLayout"]/android.widget.RelativeLayout[1]').click_exists()
    #点击进入列表第一个convo的会话
    d.xpath('//*[@resource-id="com.funbit.android:id/message_list"]/android.widget.RelativeLayout[1]').click_exists()
    #点击打开送礼面板
    d.xpath('//*[@resource-id="com.funbit.android:id/input"]/android.widget.LinearLayout[1]/android.widget.ImageView[4]').click_exists()
    #点击选中面板第一个礼物
    d.xpath('//*[@resource-id="com.funbit.android:id/giftsViewPager"]/androidx.recyclerview.widget.RecyclerView[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]').click_exists()
    gift_price = d.xpath('//*[@text="199"]').get_text()
    balance = d.xpath('//*[@resource-id="com.funbit.android:id/sendGiftPriceTv"]').get_text()
    #点击送礼按钮
    d.xpath('//*[@resource-id="com.funbit.android:id/sendGiftSubmitTv"]').click_exists()
    balance_send_gift = d.xpath('//*[@resource-id="com.funbit.android:id/sendGiftPriceTv"]').get_text()
    if int(balance_send_gift) == int(balance)-int(gift_price):
        print("送礼成功，且扣款正确！")
    d.press("back")
    d.press("back")
    d.press("back")
