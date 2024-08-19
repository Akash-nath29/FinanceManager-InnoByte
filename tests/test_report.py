from finance.report import Report
from finance.database import Database

def test_generate_monthly_report() -> None:
    db = Database()
    report = Report(db)
    monthly_report = report.generate_monthly_report(1, 2021, 1)
    assert monthly_report['income'] == 0
    assert monthly_report['expenses'] == 0
    assert monthly_report['savings'] == 0
    
def test_generate_yearly_report() -> None:
    db = Database()
    report = Report(db)
    yearly_report = report.generate_yearly_report(1, 2021)
    assert yearly_report['income'] == 0
    assert yearly_report['expenses'] == 0
    assert yearly_report['savings'] == 0