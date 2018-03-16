import requests
import ssl
ssl._create_default_https_context=ssl._create_unverified_context()
import urllib
from time import sleep
from requests.auth import HTTPBasicAuth
url = 'https://hl.cbss.10010.com/image?mode=validate&width=60&height=20&random=0.9268993696075565'
from urllib.request import urlopen
for i in range(577,10000):
    sleep(3)
    data = urllib.request.urlopen(url, context=ssl._create_unverified_context()).read()
    f = open("image/"+ str(i)+ '.png', 'wb')
    f.write(data)
    f.close()

url = 'https://hl.cbss.10010.com/image?mode=validate&width=60&height=20&random=0.9268993696075565'
data = urllib.request.urlopen(url,context=ssl._create_unverified_context()).read()
f = open('1.png','wb')
f.write(data)
f.close()
from bs4 import BeautifulSoup
import re
html = '''
<HTML xmlns="http://www.w3.org/1999/xhtml"><HEAD><TITLE></TITLE><!--头组件-->
<META content=IE=7 http-equiv=X-UA-Compatible><BASE href="https://hl.cbss.10010.com/">
<SCRIPT language=JavaScript src="component/scripts/public.js"></SCRIPT>
<SCRIPT language=JavaScript src="component/scripts/validate.js"></SCRIPT>
<SCRIPT language=JavaScript src="component/scripts/dragiframe.js"></SCRIPT>
<LINK rel=stylesheet type=text/css href="component/styles/public.css" media=screen><LINK rel=stylesheet type=text/css href="component/styles/calendar.css" media=screen><LINK rel=stylesheet type=text/css href="component/styles/tabset.css" media=screen><LINK rel=stylesheet type=text/css href="component/styles/editor.css" media=screen><LINK rel=stylesheet type=text/css href="component/styles/combobox.css" media=screen>
<SCRIPT language=JavaScript src="component/scripts/tabset.js"></SCRIPT>
<SCRIPT language=JavaScript src="component/scripts/tableedit.js"></SCRIPT>
<SCRIPT language=JavaScript src="component/scripts/print.js"></SCRIPT>
<SCRIPT language=JavaScript src="component/scripts/file.js"></SCRIPT>
<SCRIPT language=JavaScript src="component/scripts/lib/prototype.js"></SCRIPT>
<SCRIPT language=JavaScript src="component/scripts/lib/json.js"></SCRIPT>
<SCRIPT language=JavaScript src="component/scripts/ajax.js"></SCRIPT>
<META id=pagecontext subSysCode="acctmanm" version="BSS2plus" productMode="true" pagename="amlogquery.paylog.PayLog" loginProvinceId="97" loginCheckCode="201802129729137036" provinceId="97" loginEpachyId="97" epachyName=" 黑龙江 " epachyId="97" areaName=" 黑龙江 " areaCode="97" cityName=" 黑龙江 " cityId="97" deptName="黑龙江省分公司电子商务运营中心" deptCode="9722293" deptId="9722293" staffName="张欣媛" staffId="zhangxy355">
<META content="text/html; charset=gbk" http-equiv=Content-Type><!--样式文件-->
<SCRIPT language=JavaScript src="scripts-acctmanm/tableeditacctcore.js"></SCRIPT>
<SCRIPT language=JavaScript src="scripts-acctmanm/commonacctcore.js"></SCRIPT>
<SCRIPT language=JavaScript src="scripts-acctmanm/common/strtable.js"></SCRIPT>
<SCRIPT language=JavaScript src="scripts-acctmanm/common/tradectrl.js"></SCRIPT>
<SCRIPT language=JavaScript src="scripts-acctmanm/common/tradefee.js"></SCRIPT>
<SCRIPT language=JavaScript src="scripts-acctmanm/common/tradewin.js"></SCRIPT>
<SCRIPT language=JavaScript src="scripts-acctmanm/common/lookupcombo.js"></SCRIPT>
<SCRIPT language=JavaScript src="scripts-acctmanm/public/LodopFuncs.js"></SCRIPT>
<EMBED id=LODOP_EM type=application/x-print-lodop pluginspage=install_lodop.exe height=0 width=0 src=""></EMBED> <LINK rel=stylesheet type=text/css href="styles-acctmanm/lookupcombo.css" media=screen><LINK rel=stylesheet type=text/css href="component/styles/styles_base.css" media=screen><!-- 下面是copy长沙的样式，如果不需要，可以去掉 --><LINK rel=stylesheet type=text/css href="styles-acctmanm/acctmaintrade.css" media=screen><LINK rel=stylesheet type=text/css href="styles-acctmanm/tradestyle.css" media=screen>
<SCRIPT>
			Event.observe(window, 'load', initAcctInterface);
			Event.observe(window, 'load', dealTradeMsg);
			
		</SCRIPT>
<SCRIPT language=JavaScript src="scripts-acctmanm/app/amlogquery/paylog/paylog.js"></SCRIPT>
<LINK rel=stylesheet type=text/css href="styles-acctmanm/essNew.css" media=screen>
<SCRIPT language=JavaScript type=text/JavaScript>
	function onKeyPressEventByDefault() {onKeyPressEvent(null);}
	addObjEventListener("document", "keypress", onKeyPressEventByDefault);
	function onContextMenuEventByDefault() {window.event.returnValue = false;}
	addObjEventListener("document", "contextmenu", onContextMenuEventByDefault);
	var pagevisit = getPageVisit();
	completePageLoad();</SCRIPT>
<!--Body组件--></HEAD>
<BODY ondrag="return false" onkeydown=enter2Tab(event);>
<SCRIPT language=JavaScript type=text/javascript><!--
window.onload = function (){
addCalendar('cond_BEGIN_TIME');
addCalendar('cond_END_TIME');
showAllUserForAcct();
}
// --></SCRIPT>
<IFRAME id=wade_sbtframe class=c_sbtframe style="DISPLAY: none" frameBorder=no name=wade_sbtframe scrolling=no></IFRAME><SPAN id=_tradeGlobal style="DISPLAY: none"><INPUT id=_tradeGlobal_SERVLET_PATH type=hidden value=/acctmanm></INPUT> <INPUT id=_tradeGlobal_PAGE_NAME type=hidden value=amlogquery.paylog.PayLog></INPUT> <INPUT id=_tradeGlobal_TRADE_STATUS type=hidden value=querySuccess></INPUT> <INPUT id=_tradeGlobal_ERROR type=hidden value=false></INPUT> </SPAN><!-- ajax刷新后提示信息存放地 --><SPAN id=_messageGlobalAcct style="DISPLAY: none"></SPAN>
<DIV id=errorMsg class=popNote style="WIDTH: 280px; DISPLAY: none; TOP: 155px"></DIV><A id=lodopinstall style="DISPLAY: none" href="scripts-acctmanm/public/install_lodop.exe">执行安装</A> <!--如何需要post必须使用form-->
<FORM method=post name=Form0 action=/acctmanm><INPUT id=service type=hidden value=direct/1/amlogquery.paylog.PayLog/$Form name=service> <INPUT id=sp type=hidden value=S0 name=sp> <INPUT id=Form0 type=hidden value=EPARCHY_CODE,NET_TYPE_CODE,cond_BEGIN_TIME,cond_END_TIME,cond_DESIGNATE_PAY,bquerytopwithfee,daochu2 name=Form0> <INPUT id=EPARCHY_CODE type=hidden value=X name=EPARCHY_CODE> <INPUT id=NET_TYPE_CODE type=hidden value=X name=NET_TYPE_CODE> <INPUT id=cond_ACCT_ID type=hidden name=cond_ACCT_ID></INPUT> <INPUT id=cond_USER_ID type=hidden name=cond_USER_ID></INPUT> <!--css的样式-->
<DIV class=c_content>
<DIV class=c_search>
<DIV class=e_title>查找条件</DIV>
<TABLE class="threeCol QueryInfoMoreShow" cellSpacing=0 cellPadding=0 border=0><!--tr表示一行，td表示一列--><!--查询信息电信类型、业务号码和用户状态，无线账务自己的组件-->
<TBODY>
<TR>
<TD class=label><SELECT onchange=changeDesc(this) id=cond_ID_TYPE class=sel name=cond_ID_TYPE nullable="yes" desc="查询方式" _counted="undefined" whenWatch="querySuccess"> <OPTION selected value=1>按业务号码</OPTION> <OPTION value=2>按账户标识</OPTION> <OPTION value=3>按用户标识</OPTION> <OPTION value=4>按缴费流水号</OPTION> <OPTION value=5>按支票号</OPTION></SELECT> </TD>
<TD><INPUT onblur=changeNetCodeAfterSerialNumber(this) id=cond_SERIAL_NUMBER class=txt value=18545195599 name=cond_SERIAL_NUMBER nullable="no" desc="号码" maxsize="40" _counted="undefined" checkdata="checkspec,maxlength=40" whenWatch="querySuccess"><SPAN class=textred>*</SPAN> </TD>
<TD class=label>用户状态： </TD>
<TD><SELECT id=cond_REMOVE_TAG class=sel name=cond_REMOVE_TAG datatype="text" desc="用户状态" maxsize="1" _counted="undefined" whenWatch="querySuccess"> <OPTION selected value=0>未销号</OPTION> <OPTION value=1>已销号</OPTION></SELECT> </TD>
<TD class=label>电信类型： </TD>
<TD><SELECT id=cond_NET_TYPE_CODE class=sel name=cond_NET_TYPE_CODE nullable="yes" desc="电信类型" maxsize="4" _counted="undefined" whenWatch="querySuccess"> <OPTION value=""></OPTION> <OPTION value=XN>虚拟用户</OPTION> <OPTION selected value=50>4G</OPTION> <OPTION value=WV>集团业务</OPTION> <OPTION value=33>WCDMA</OPTION> <OPTION value=40>互联网接入业务</OPTION> <OPTION value=41>互联网应用业务</OPTION> <OPTION value=CP>组合业务</OPTION> <OPTION value=30>固话业务</OPTION></SELECT> </TD>
<TD class=noncont>&nbsp;</TD></TR>
<TR>
<TD class=label>开始时间： </TD>
<TD>
<SCRIPT language=JavaScript src="component/scripts/component/calendar.js"></SCRIPT>
<INPUT id=cond_BEGIN_TIME class=txt value=2018-02-01 name=cond_BEGIN_TIME datatype="date" nullable="no" desc="开始时间" maxName="cond_END_TIME" format="yyyy-MM-dd"><SPAN class=textred>*</SPAN><IMG id=IMG_CAL_cond_BEGIN_TIME class=c_imgtop_3 border=0 src="component/images/tapestry/form/cal.gif"> </TD>
<TD class=label>结束时间： </TD>
<TD><INPUT id=cond_END_TIME class=txt value=2018-02-11 name=cond_END_TIME datatype="date" nullable="no" desc="结束时间" format="yyyy-MM-dd" minName="cond_BEGIN_TIME"><SPAN class=textred>*</SPAN><IMG id=IMG_CAL_cond_END_TIME class=c_imgtop_3 border=0 src="component/images/tapestry/form/cal.gif"> </TD>
<TD class=label>所有账户：</TD>
<TD><INPUT onclick="" id=cond_DESIGNATE_PAY class=checkbox type=checkbox name=cond_DESIGNATE_PAY> </TD></TR>
<TR>
<TD class=btnArea colSpan=6><INPUT onclick="return query(this);" onmouseover="this.className='btn2 btnOver'" onmouseout="this.className='btn2 btnOff'" id=bquerytopwithfee class=btn2 type=submit value="查 询" name=bquerytopwithfee> </TD></TR></TBODY></TABLE></DIV><!-- 控制区 -->
<DIV style="DISPLAY: none"><!-- 为了处理多用户弹出，增加一个隐藏区域 --><INPUT id=cond_X_USER_COUNT type=hidden name=cond_X_USER_COUNT></INPUT> 
<DIV class=e_title>用户明细信息 </DIV>
<TABLE class=threeCol style="DISPLAY: block" cellSpacing=0 cellPadding=0 border=0>
<TBODY>
<TR>
<TD class=label>账户标识： </TD>
<TD>9716101868216189 </TD>
<TD class=label>客户名称： </TD>
<TD>司玉贵(后付费) </TD>
<TD class=label>用户状态： </TD>
<TD>开通 </TD></TR>
<TR>
<TD class=label>付费类型： </TD>
<TD>现金 </TD>
<TD class=label>产品名称： </TD>
<TD>4G主副卡业务-语音副卡基本套餐 </TD><!--<td class="label">
				用户积分：
			</td>
			<td>
				<input type="text" jwcid="@Insert"
					value="ognl:page.userInfo.SCORE_VALUE" />
			</td>-->
<TD class=label>开户时间： </TD>
<TD>2014-10-22 08:52:52 </TD></TR>
<TR>
<TD class=label>客户市县： </TD>
<TD>哈尔滨市区 </TD>
<TD class=label>信用额度： </TD>
<TD>0.00 </TD>
<TD class=label>设备数： </TD>
<TD>7 </TD></TR>
<TR>
<TD class=label>欠费： </TD>
<TD></TD>
<TD class=label>实时话费： </TD>
<TD></TD>
<TD class=label>
<DIV style="COLOR: red">实时结余： </DIV></TD>
<TD></TD></TR>
<TR><!-- <td class="label">
				<div style="color:red">
				一般纳税人：
				</div>
			</td>
			<td>
				<input type="text" jwcid="@Insert"
					value="ognl:page.userInfo.IDENTITY_CHECK_NAME" />
			</td> --><!--<td class="label">
				开户时间：
			</td>
			<td>
				<input type="text" jwcid="@Insert"
					value="ognl:page.userInfo.OPEN_DATE" />
			</td>-->
<TD class=label></TD>
<TD></TD>
<TD class=label></TD>
<TD></TD>
<TD class=label></TD>
<TD></TD><!-- <td class="label">
			</td>
			<td>
			</td> --></TR><!-- 
		<span jwcid="@Conditional" condition='ognl:withFee&&(!"0".equals(page.userInfo.PREPAY_TAG) && !"1".equals(page.userInfo.PREPAY_TAG) && !"".equals(page.userInfo.PREPAY_TAG) && page.userInfo.PREPAY_TAG != null)'>
		<tr>
			<td class="label">
				账户余额：
			</td>
			<td>
				<input type="text" jwcid="@Insert"
					value="ognl:page.acctBalanceInfo.TOTAL_FEE" />
			</td>
			<td class="label">
			</td>
			<td>
				
				<input type="hidden" name="cond_PRE_TOTAL_FEE" id="cond_PRE_TOTAL_FEE" jwcid="@Any" value="ognl:page.acctBalanceInfo.TOTAL_FEE" />
				
			</td>
			<td class="label">
			</td>
			<td>
			</td>
		</tr>
		</span>
		--></TBODY></TABLE></DIV><SPAN id=InfoPart><!--span表格外框样式-->
<DIV class="UITableBox topSpace">
<DIV class=tab_inbox>
<DIV class=topOperate><STRONG>交费记录</STRONG> <INPUT onclick="return beforeExportDatas();" onmouseover="this.className='btn2 btnOver'" onmouseout="this.className='btn2 btnOff'" id=daochu2 class=btn2 type=submit value="导 出" name=daochu2> </DIV>
<DIV class=UITable style="HEIGHT: 350px">
<TABLE id=PayLogTable>
<THEAD>
<TR style="POSITION: relative; TOP: 0px; ; TOP: expression(this.offsetParent.scrollTop)">
<TH id=col_ROWNUM style="BORDER-LEFT-WIDTH: 0px">序号 </TH>
<TH id=col_ACCT_ID>账户标识 </TH>
<TH id=col_PAY_NAME>付费名称 </TH>
<TH id=col_USER_ID>用户标识 </TH>
<TH id=col_SERVICE_CLASS_CODE>电信类型 </TH>
<TH id=col_AREA_CODE>长途区号 </TH>
<TH id=col_SERIAL_NUMBER>业务号码 </TH>
<TH id=col_CHANNEL_ID>渠道标识 </TH>
<TH id=col_PAYMENT_OP_DESC>储值操作类型 </TH>
<TH id=col_PAYMENT>交费方式 </TH>
<TH id=col_PAY_FEE_MODE>支付方式 </TH>
<TH id=col_RECV_FEE>收费金额 </TH>
<TH id=col_RECV_TIME>总部交易时间 </TH>
<TH id=col_RECV_EPARCHY_CODE>交易地市 </TH>
<TH id=col_RECV_CITY_CODE>交易业务区 </TH>
<TH id=col_RECV_DEPART_ID>交易部门 </TH>
<TH id=col_RECV_STAFF_ID>交易员工 </TH>
<TH id=col_STAFF_NAME>交易员工姓名 </TH>
<TH id=col_BANK_ACCT_NO>银行账号或支票号 </TH>
<TH id=col_BANK_CODE>银行名称 </TH>
<TH id=col_CHARGE_ID>省份BSS流水号 </TH>
<TH id=col_OUTER_TRADE_ID>交费流水号 </TH>
<TH id=col_ACTION_CODE>活动项目编码 </TH>
<TH id=col_ACTION_NAME>活动项目名称 </TH>
<TH id=col_CANCEL_TAG>返销标志 </TH>
<TH id=col_CANCEL_TIME>返销时间 </TH>
<TH id=col_CANCEL_CHARGE_ID>返销关联流水 </TH>
<TH id=col_REMARK>交费备注 </TH>
<TH id=col_SERIAL_NUMBER_OUT_B>被转号码 </TH>
<TH id=col_NP_FLAG>业务类型 </TH></TR></THEAD>
<TBODY>
<TR class=row_odd style="COLOR: black">
<TD style="BORDER-LEFT-WIDTH: 0px">1 </TD>
<TD>9716101868216189 </TD>
<TD>司玉贵 </TD>
<TD>9716090874312667 </TD>
<TD>4G </TD>
<TD>0451 </TD>
<TD>18604513001 </TD>
<TD>续费卡系统 </TD>
<TD>储值 </TD>
<TD>缴费卡收入_普通预存款 </TD>
<TD>现金 </TD>
<TD>100.00 </TD>
<TD>2018-02-02 17:31:03 </TD>
<TD>哈尔滨 </TD>
<TD>哈尔滨 </TD>
<TD>Z000YKC </TD>
<TD>Z000DZQD </TD>
<TD>黑龙江渠道工号 </TD>
<TD>981705087528232 </TD>
<TD></TD>
<TD>9718020274882604 </TD>
<TD>J9843015175638621731 </TD>
<TD>0 </TD>
<TD></TD>
<TD>未返销 </TD>
<TD>0000-00-00 00:00:00 </TD>
<TD></TD>
<TD>无 </TD>
<TD></TD>
<TD>普通缴费 </TD></TR>
<TR class=row_even style="COLOR: black">
<TD style="BORDER-LEFT-WIDTH: 0px">2 </TD>
<TD>9716101868216189 </TD>
<TD>司玉贵 </TD>
<TD>9716090874312667 </TD>
<TD>4G </TD>
<TD>0451 </TD>
<TD>18604513001 </TD>
<TD>续费卡系统 </TD>
<TD>储值 </TD>
<TD>缴费卡收入_普通预存款 </TD>
<TD>现金 </TD>
<TD>100.00 </TD>
<TD>2018-02-02 17:31:26 </TD>
<TD>哈尔滨 </TD>
<TD>哈尔滨 </TD>
<TD>Z000YKC </TD>
<TD>Z000DZQD </TD>
<TD>黑龙江渠道工号 </TD>
<TD>981705087994103 </TD>
<TD></TD>
<TD>9718020274884262 </TD>
<TD>J9843115175638812358 </TD>
<TD>0 </TD>
<TD></TD>
<TD>未返销 </TD>
<TD>0000-00-00 00:00:00 </TD>
<TD></TD>
<TD>无 </TD>
<TD></TD>
<TD>普通缴费 </TD></TR></TBODY></TABLE></DIV></DIV></DIV>
<DIV class=label style="TEXT-ALIGN: right; PADDING-RIGHT: 25px">查询期间内交费总额：200.00元</DIV></SPAN><!-- 查询的时候，选择了失效账户后，查询出的所有acct放在这里，是以json的形式放的 --><INPUT id=MULTI_ACCT_DATA type=hidden name=MULTI_ACCT_DATA></INPUT> </DIV><INPUT type=hidden name=X_CODING_STR></INPUT> </FORM>
<SCRIPT>Ajax.Responders.register(myGlobalHandlers);</SCRIPT>
</BODY></HTML>
'''
soup = BeautifulSoup(html, 'lxml')
PayLog = soup.select('#PayLogTable')
th = PayLog[0].find_all('th')
head = ''
for t in th:
    # print(t.get_text())
    head += t.get_text() + ','
print(head)
trs = PayLog[0].find_all('tr')

for tr in trs:
    tds = tr.find_all('td')
    for td in tds:
        print(td.get_text())
# print(soup.prettify())
# print(PayLog[0].select("#col_ROWNUM")[0].contents[0])
# print(PayLog[0].select("#col_ACCT_ID")[0].contents[0])
# print(PayLog[0].select("#col_PAY_NAME")[0].contents[0])
# print(PayLog[0].select("#col_USER_ID")[0].contents[0])
# print(PayLog[0].select("#col_SERVICE_CLASS_CODE")[0].contents[0])
# print(PayLog[0].select("#col_AREA_CODE")[0].contents[0])
# print(PayLog[0].select("#col_SERIAL_NUMBER")[0].contents[0])
# print(PayLog[0].select("#col_CHANNEL_ID")[0].contents[0])
# print(PayLog[0].select("#col_PAYMENT_OP_DESC")[0].contents[0])
# print(PayLog[0].select("#col_PAY_FEE_MODE")[0].contents[0])
# print(PayLog[0].select("#col_RECV_FEE")[0].contents[0])
# print(PayLog[0].select("#col_RECV_TIME")[0].contents[0])
# print(PayLog[0].select("#col_RECV_EPARCHY_CODE")[0].contents[0])
# print(PayLog[0].select("#col_RECV_CITY_CODE")[0].contents[0])
# print(PayLog[0].select("#col_RECV_DEPART_ID")[0].contents[0])
# print(PayLog[0].select("#col_RECV_STAFF_ID")[0].contents[0])
# print(PayLog[0].select("#col_STAFF_NAME")[0].contents[0])
# print(PayLog[0].select("#col_BANK_ACCT_NO")[0].contents[0])
# print(PayLog[0].select("#col_BANK_CODE")[0].contents[0])
# print(PayLog[0].select("#col_OUTER_TRADE_ID")[0].contents[0])
# print(PayLog[0].select("#col_ACTION_CODE")[0].contents[0])
# print(PayLog[0].select("#col_ACTION_NAME")[0].contents[0])
# print(PayLog[0].select("#col_CANCEL_TAG")[0].contents[0])
# print(PayLog[0].select("#col_CANCEL_TIME")[0].contents[0])
# print(PayLog[0].select("#col_CANCEL_CHARGE_ID")[0].contents[0])
# print(PayLog[0].select("#col_REMARK")[0].contents[0])
# print(PayLog[0].select("#col_SERIAL_NUMBER_OUT_B")[0].contents[0])
# print(PayLog[0].select("#col_NP_FLAG")[0].contents[0])
pattern = re.compile(r'查询期间内交费总额：(.*)元')
m = pattern.search(html)
print(m[1])