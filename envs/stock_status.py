import win32com.client

# 연결체크
instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = instCpCybos.IsConnect
if bConnect == 0:
    print("Cybos Plus가 정상적으로 연결되지 않음")
    exit()

#######################################################################################################################
# function get_status(종목코드)
# 종목코드에 해당하는 주식 정보를 가져옴
#######################################################################################################################
# code : 종목코드
# name : 종목명
# time : 시간
# cprice : 종가
# diff : 대비
# open : 시가
# high : 고가
# low : 저가
# offer : 매도호가
# bid : 매수호가
# vol : 거래량
# vol_value : 거래대금
#######################################################################################################################

def get_status(stock_id):
    instStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
    instStockMst.SetInputValue(0, stock_id)
    instStockMst.BlockRequest()

    rqStatus = instStockMst.GetDibStatus()
    rqRet = instStockMst.GetDibMsg1()
    print("통신상태", rqStatus, rqRet)  # status 0 조회완료
    if rqStatus != 0:
        exit()

    stock_status_dict = {
        'code' : instStockMst.GetHeaderValue(0),
        'name' : instStockMst.GetHeaderValue(1),
        'time' : instStockMst.GetHeaderValue(4),
        'cprice' : instStockMst.GetHeaderValue(11),
        'diff' : instStockMst.GetHeaderValue(12),
        'open' : instStockMst.GetHeaderValue(13),
        'high' : instStockMst.GetHeaderValue(14),
        'low' : instStockMst.GetHeaderValue(15),
        'offer' : instStockMst.GetHeaderValue(16),
        'bid' : instStockMst.GetHeaderValue(17),
        'vol' : instStockMst.GetHeaderValue(18),
        'vol_value' : instStockMst.GetHeaderValue(19)
    }
    return stock_status_dict