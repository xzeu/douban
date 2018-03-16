import requests
import json
def SanHu(number):
    u""" 三户查询接口
    :param number: 要查询手机号码
    :return:   0:CBSS  1:ESS  其它返回具体错误信息
    """
    url = 'http://m.hlj165.com/cp/aop/sanHu'
    postdata = {
        "user": "worp",
        "pwd": "worp",
        "number": str(number)
    }
    res =  requests.post(url,data=postdata)
    result = res.json()
    if result['success'] == True:
        result=json.loads(result['resultList'])
        return result['sysType']
    else:
        return result['message']

def ESS(phone, serviceID, enableTag="NOW", optType="O"):
    u""" ESS 流量充值接口
    :param phone:   要订购或退订流量的手机号码
    :param serviceID:   特服号码
    :param enableTag: 生效时间  NOW:立即生效  NEXTMONTH:次月生效
    :param optType:  操作类型  O:订购  C: 退订
    :return: 成功：充值成功 失败：错误信息
    """
    url = 'http://m.hlj165.com/cp/ess/traffic'
    postdata = {
        "user": "worp",
        "pwd": "worp",
        "phone": str(phone),
        "serviceID":str(serviceID),
        "enableTag":str(enableTag),
        "optType":str(optType)
    }
    res = requests.post(url,data=postdata)
    result = res.json()
    if result['success'] == True:
        # return result['resultList']
        return u'充值成功'
    else:
        return result['message']

def AOP(phone, productId, packageId, elementId, elementType='D', enableTag='1', optType='00'):
    u""" AOP充值接口
    :param phone: 手机号码
    :param productId: 产品ID
    :param enableTag: 	生效时间 1=立即生效 2=次月生效
    :param optType:    操作类型 00=订购 01=退订
    :param packageId: 套餐ID
    :param elementId: 资费ID
    :param elementType: D=资费 S=服务 A=活动 X=S服务
    :return:  成功：充值成功 失败：错误信息
    """
    url = 'http://m.hlj165.com/cp/aop/traffic'
    postdata= '{"user": "worp","pwd": "worp","phone":' +\
              str(phone)\
              +',"productInfo": [{"enableTag": '+\
              str(enableTag)\
              +',"optType": '+\
              str(optType)\
              +',"packageElement": [{"elementId": '+\
              str(elementId)\
              +',"packageId":'+ \
              str(packageId)\
              +',"elementType":"D"}],"productId":'+ \
              str(productId)\
              +'}]}'
    res = requests.post(url, data=postdata)
    result = res.json()
    if result['success'] == True:
        # return result['resultList']
        return u'充值成功'
    else:
        return result['message']

phoneNum = '15645101599'
# 调用三户查询手机号码网别
req = SanHu(phoneNum)

if req == str(1):
    # DQ20180116_0Y100MC 100M
    # DQ20180116_0Y200MB 200M
    # DQ20180116_0Y500MB 500M
    # DQ20180116_0Y1GJ  1G
    # DQ20180116_0Y2GJ  2G
    # ESS('手机号码', '特服号码')
    res = ESS(phoneNum, 'DQ20180116_0Y1GJ',optType='C')
    print(res)
elif req == str(2):
    # 套餐编码 51976612 2G
    # 产品编码 90343470 2G
    # 流量包编码 8291711 2G
    # AOP('手机号码', '产品ID', '套餐ID', '资费ID')
    res = AOP(phoneNum, '90343470', '51976612', '8291711')
    print(res)