import pandas as pd
from lxml import etree

def xml_report_to_excel(xml_file, excel_file):
    # Parse the XML file (handles encoding declaration automatically)
    tree = etree.parse(xml_file)


    root = tree.getroot()

    print(root)
    # List to hold all rows (each Band becomes a row)
    rows = []

    # Iterate over all <Band> elements
    for band in root.findall('.//Band', namespaces={'': 'http://schemas.radixware.org/reports.xsd'}):
        row = {'BandType': band.get('Type')}  # Get the Type attribute

        # If there's a GroupLevel attribute, include it
        group_level = band.get('GroupLevel')
        if group_level:
            row['GroupLevel'] = group_level

        # Extract all <Cell> elements
        for cell in band:
            cell_name = cell.get('Name')
            cell_text = cell.text.strip() if cell.text else ''
            row[cell_name] = cell_text

        rows.append(row)

    # Create DataFrame
    df = pd.DataFrame(rows)

    # Reorder columns to put BandType and GroupLevel first
    cols = ['BandType', 'GroupLevel'] + [c for c in df.columns if c not in ['BandType', 'GroupLevel']]
    df = df[cols]

    # Save to Excel
    df.to_excel(excel_file, index=False)
    print(f"✅ Converted {len(df)} bands to {excel_file}")

# Usage
xml_report_to_excel('my_report.xml', 'report_output.xlsx')