from iFinDPy import *
def ths():
    THS_iFinDLogin('yrzc001','666888')
    thsData=THS_HistoryQuotes('601857.SH','close','period:D,pricetype:1,rptcategory:0,fqdate:1900-01-01,hb:YSHB','2017-01-01','2017-10-23')
    thsData=THS_Trans2DataFrame(thsData)
    history=list(thsData['close'])
    return history
# print(history)
# print(len(history))