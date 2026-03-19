import xml

from lxml import etree
ugly_xml='''
<?xml version='1.0' encoding='utf-8'?><Report xmlns="http://schemas.radixware.org/reports.xsd"><Band Type="Title"><Cell Name="FIExpr">Financial institution: 141) Sanima</Cell><Cell Name="BranchesExpr">Branches: &lt;all></Cell><Cell Name="AcctPlanItemsExpr">Chart of accounts items: &lt;all></Cell><Cell Name="AccountExpr">Account: &lt;all></Cell><Cell Name="ParamFinOperKindsStr">Types of financial operations: &lt;all></Cell><Cell Name="ParamEntryKindsStr">Entry types: &lt;all></Cell><Cell Name="PeriodExpr">from Mar 12, 2026 to Mar 12, 2026</Cell></Band><Band Type="GroupHeader" GroupLevel="4"><Cell Name="AcctHeader">Branch: AMARGADHI BRANCH
Chart of accounts item: CU-CR: Customer Credit Accounts
Currency: NPR
Account: ACC_100000259147</Cell></Band><Band Type="Detail"><Cell Name="TranId"></Cell><Cell Name="EntryKindExprOutput"></Cell><Cell Name="RowNumber">1</Cell><Cell Name="BalanceAfterPosting">0</Cell><Cell Name="CredAmtExprOutput">0</Cell><Cell Name="DebAmtExprOutput">0</Cell><Cell Name="OpBalanceExprOutput">0</Cell><Cell Name="TransTypeExprOuput"></Cell><Cell Name="CardNumAndExtRidExprOutput"> </Cell><Cell Name="OperDayOutput"></Cell></Band><Band Type="GroupFooter" GroupLevel="4"><Cell Name="EmptyStr"></Cell><Cell Name="AcctEndBalanceExprTotals">0</Cell><Cell Name="AcctSumCredExprTotals">0</Cell><Cell Name="AcctSumDebExprTotals">0</Cell><Cell Name="AcctOpBalanceExprTotals">0</Cell><Cell Name="CredAmtSum">0.0</Cell><Cell Name="DebAmtSum">0.0</Cell></Band><Band Type="GroupHeader" GroupLevel="4"><Cell Name="AcctHeader">Branch: AMARGADHI BRANCH
Chart of accounts item: CU-CR: Customer Credit Accounts
Currency: NPR
Account: ACC_100000260558</Cell></Band><Band Type="Detail"><Cell Name="TranId"></Cell><Cell Name="EntryKindExprOutput"></Cell><Cell Name="RowNumber">1</Cell><Cell Name="BalanceAfterPosting">0</Cell><Cell Name="CredAmtExprOutput">0</Cell><Cell Name="DebAmtExprOutput">0</Cell><Cell Name="OpBalanceExprOutput">0</Cell><Cell Name="TransTypeExprOuput"></Cell><Cell Name="CardNumAndExtRidExprOutput"> </Cell><Cell Name="OperDayOutput"></Cell></Band><Band Type="GroupFooter" GroupLevel="4"><Cell Name="EmptyStr"></Cell><Cell Name="AcctEndBalanceExprTotals">0</Cell><Cell Name="AcctSumCredExprTotals">0</Cell><Cell Name="AcctSumDebExprTotals">0</Cell><Cell Name="AcctOpBalanceExprTotals">0</Cell><Cell Name="CredAmtSum">0.0</Cell><Cell Name="DebAmtSum">0.0</Cell></Band><Band Type="GroupHeader" GroupLevel="4"><Cell Name="AcctHeader">Branch: AMARGADHI BRANCH
Chart of accounts item: CU-CR: Customer Credit Accounts
Currency: NPR
Account: ACC_100000260618</Cell></Band><Band Type="Detail"><Cell Name="TranId"></Cell><Cell Name="EntryKindExprOutput"></Cell><Cell Name="RowNumber">1</Cell><Cell Name="BalanceAfterPosting">-21373.73</Cell><Cell Name="CredAmtExprOutput">0</Cell><Cell Name="DebAmtExprOutput">0</Cell><Cell Name="OpBalanceExprOutput">-21,373.73</Cell><Cell Name="TransTypeExprOuput"></Cell><Cell Name="CardNumAndExtRidExprOutput"> </Cell><Cell Name="OperDayOutput"></Cell></Band><Band Type="GroupFooter" GroupLevel="4"><Cell Name="EmptyStr"></Cell><Cell Name="AcctEndBalanceExprTotals">-21,373.73</Cell><Cell Name="AcctSumCredExprTotals">0</Cell><Cell Name="AcctSumDebExprTotals">0</Cell><Cell Name="AcctOpBalanceExprTotals">-21,373.73</Cell><Cell Name="CredAmtSum">0.0</Cell><Cell Name="DebAmtSum">0.0</Cell></Band></Report>
'''


# Encode to bytes (UTF-8 is the most common)
root = etree.fromstring(ugly_xml.encode('utf-8'))

# Now you can pretty-print
pretty_xml = etree.tostring(root, pretty_print=True, encoding='unicode')
print(pretty_xml)