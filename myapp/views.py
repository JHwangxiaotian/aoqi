import json

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt


# coding=utf-8
# Create your views here.

def hello(request):
    data = {}
    # 作为json 数组返回给客户端
    deviceID = request.GET.get('deviceId', '')
    print(deviceID)
    if deviceID == '':
        data['code'] = '401'
        data['msg'] = '输入的设备ID有误'
        str1 = json.dumps(data, ensure_ascii=False)
        return HttpResponse(str1)

    data['code'] = '200'
    data['msg'] = ''

    cursor = connection.cursor()
    cursor.execute("select * from datastatistic where 桩资产= %s" % (deviceID))
    # desc = cursor.description
    # print(desc)
    # cursor.execute("select * from datastatistic where 桩输出='60'")
    rows = cursor.fetchall()
    if len(rows) == 0:
        data['code'] = '201'
        data['msg'] = '输入的设备ID没有查询到'
        data['data'] = ''
        str1 = json.dumps(data, ensure_ascii=False)
        return HttpResponse(str1)
    for row in rows:
        body = {}
        body['桩资产'] = row[0]
        body['设备类'] = row[1]
        body['桩生产'] = row[2]
        body['充电标'] = row[3]
        body['桩设备'] = row[4]
        body['桩最大'] = row[5]
        body['桩输出'] = row[6]
        body['站名称'] = row[7]
        body['站地址'] = row[8]
        body['市运维'] = row[9]
        body['站维度'] = row[10]
        body['站经度'] = row[11]
        body['站点类'] = row[12]
        body['区'] = row[13]
        body['TCU版本'] = row[14]
        body['是否无'] = row[15]
        body['是否虚'] = row[16]
        body['备注'] = row[17]

        data['data'] = body

    # if request.method == 'GET':
    #     print('===当前是get请求')
    # 用get方式请求数据
    # username = request.GET.get('username', "")
    # password = request.GET.get('password', "")
    # print('==username:'+username)
    # print('==password:'+password)

    # devicesId = request.GET.get('devicesId', '')
    # if devicesId == '001':
    #     return HttpResponse('设备ID查询成功，xxx位置，xxx状态')
    # else:
    #     return HttpResponse('设备ID查找失败')

    str2 = json.dumps(data, ensure_ascii=False)
    return HttpResponse(str2)

# 默认开启了csrf保护机制，本服务仅作自测使用，加上csrf_exempt去除掉csrf保护
@csrf_exempt
def updata(request):
    print("=====update=====")
    print(request.method)
    if request.method == 'POST':
        print('===当前是Post请求')
    if request.POST:
        id = request.POST.get('id')
        shebeileixing = request.POST.get('shebeileixing', '')
        zhuangshengchan = request.POST.get('zhuangshengchan', '')
        chongdianbiao = request.POST.get('chongdianbiao', '')
        zhuangshebei = request.POST.get('zhuangshebei', '')
        zhuangzuida = request.POST.get('zhuangzuida', '')
        zhuangshuchu = request.POST.get('zhuangshuchu', '')
        zhanmingcheng = request.POST.get('zhanmingcheng', '')
        zhandizhi = request.POST.get('zhandizhi', '')
        shiyunwei = request.POST.get('shiyunwei', '')
        zhanweidu = request.POST.get('zhanweidu', '')
        zhanjingdu = request.POST.get('zhanjingdu', '')
        zhandianlei = request.POST.get('zhandianlei', '')
        qu = request.POST.get('qu', '')
        tcu = request.POST.get('tcu', '')
        shifouwu = request.POST.get('shifouwu', '')
        shifouxu = request.POST.get('shifouxu', '')
        beizhu = request.POST.get('beizhu', '')
        try:
            sqlstr = "update datastatistic set 设备类='%s'," \
                     "桩生产='%s',充电标='%s', 桩设备='%s'," \
                     "桩最大='%s',桩输出='%s',站名称='%s'," \
                     "站地址='%s',市运维='%s',站纬度='%s'," \
                     "站经度='%s',站点类='%s',区='%s'," \
                     "TCU版本='%s',是否无='%s',是否虚='%s',备注='%s'" \
                     "where 桩资产='%s'" % (
                shebeileixing,zhuangshengchan,chongdianbiao,zhuangshebei,
                zhuangzuida,zhuangshuchu,zhanmingcheng,zhandizhi,shiyunwei,
                zhanweidu,zhanjingdu,zhandianlei,qu,tcu,shifouwu,shifouxu,beizhu,id
            )
            print(sqlstr)
            cursor = connection.cursor()
            cursor.execute(sqlstr)
            # cursor.execute("update datastatistic set 设备类='交流设备' where 桩资产='1242690000000001'")
            rows = cursor.fetchall()
            data = {'code': '200', 'msg': '修改成功', 'data': ''}
            str1 = json.dumps(data, ensure_ascii=False)
            return HttpResponse(str1)
        except Exception as e:
            print(e)
            data = {'code': '400', 'msg': '修改失败', 'data': ''}
            str1 = json.dumps(data, ensure_ascii=False)
            return HttpResponse(str1)
    return HttpResponse('修改成功')