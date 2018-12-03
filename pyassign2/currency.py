#!/usr/bin/env python3

"""currency.py:change the currency
__author__ = "Changrui"
__pkuid__  = "1800011758"
__email__  = "706771104@qq.com"
"""

#调用函数
from urllib.request import urlopen
import json

#分解字符串函数
def before_space(s):
    l = s.split()
    s = l[0]
    return s

#访问URL函数
def get_from(b):
    doc = urlopen(b)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr = str(json.loads(jstr))
    c = eval(jstr)
    return c

#货币转换函数
def exchange(currency_from, currency_to, amount_from):
    d = get_from('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + currency_from + '&to=' + currency_to + '&amt=' + amount_from)
    amount_to = d['to']
    amount = before_space(amount_to)
    return(amount)

#分解字符串测试函数
def test_before_space():
    assert ('5' == before_space('5 CLP'))
    assert ('2.5' == before_space('2.5 XDR'))
    assert ('4.5' == before_space('4.5 XPD'))

#URL转化测试函数
def test_get_from():
    assert({ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : True, "error" : "" } == get_from(
        'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + 'USD' + '&to=' + 'EUR' + '&amt=' + '2.5'))
    assert ({ "from" : "4 Afghan Afghanis", "to" : "4.5521856290672 Bangladeshi Taka", "success" : True, "error" : "" }
             == get_from('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + 'AFN' + '&to=' + 'BDT' + '&amt=' + '4'))
    assert ({ "from" : "6 Bahraini Dinar", "to" : "28179.881157038 Burundian Francs", "success" : True, "error" : "" } == 
            get_from('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + 'BHD' + '&to=' + 'BIF' + '&amt=' + '6'))

#exchange测试函数
def test_exchange():
    assert(exchange('USD','EUR','2.5') == '2.1589225')
    assert(exchange('AFN','BDT','4') == '4.5521856290672')
    assert(exchange('BHD','BIF','6') == '28179.881157038')

#测试所有函数
def test_All():
    test_before_space()
    test_get_from()
    test_exchange()
    print("All tests passed")

#支持的货币类型
list = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
          'BSD', 'BTC', 'BTN', 'BWP', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP',
          'DZD', 'EEK', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG',
          'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK',
          'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MTL', 'MUR', 'MVR', 'MWK', 'MXN',
          'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 
          'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD',
          'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER',
          'ZAR', 'ZMK', 'ZMW', 'ZWL']
def main():
    currency_from = input('请输入源货币:')
    currency_to = input('请输入目标货币:')
    amount_from = input('请输入源货币数目:')
    test_All()
    if (currency_from in list) == False:
        print("源货币种类不正确")
    elif (currency_to in list) == False:
        print ("目标货币种类不正确")
    else:
        try:
            a = complex(amount_from)
        except ValueError:
            print ("货币数目不正确")
        else:
            print(exchange(currency_from, currency_to, amount_from))

if __name__  ==  '__main__':
    main()
