{
    'name': "Deliveries labels printing",
    'version': '9.0.1.0',
    'depends': ['sale', 'report'],
    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Stock',
    'description': 
    """
    Print labels for deliveries.

    This modules also creates a paperreport adapted for AbAKUS labels.
    To use it, you have to set it for the given report (settings/reports/=>Labels set paperformat as "AbAkus Labels ...").

    We added a button in the sale order form to directly print the labels.	
    """,
    'data': [
             'reports/deliveries_labels.xml',
             'report_paperformat_data.xml'
             ],
}
