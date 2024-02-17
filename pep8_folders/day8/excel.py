# Create Excel file named my_first_excel_with_python.xlsx using Python and xlsxwriter package
# Add worksheet my_first_worksheet to workbook
# Create new formatting: bold, centralized, size 30, Calibri, bg color blue.
# Fill cell A1:1 with your name with created format
# Set column B width to 10
# Merge columns C1 - D4 and fill them with arbitrary text
# Create column chart
# Represent two lists by using column chart (write them somewhere in worksheet)
# Measured = [130,125,145,150,180]
# Budget = [120,140,150,200,200]
import xlsxwriter as xls

workbook = xls.Workbook("my_first_excel_with_python.xlsx")

worksheet = workbook.add_worksheet("my_first_woorksheet")

Format_text = workbook.add_format({'bold':True, 'align':'center','bg_color':'#0000FF','font_size':30, \
                                   'font_name':'Calibri'})

worksheet.write("A1", "josip", Format_text)

worksheet.set_column("B:B", 30)

worksheet.merge_range('C1:D4', "arbitrary text")

Chart = workbook.add_chart({'type': 'column'})

Measured = [130,125,145,150,180]
Budget = [120,140,150,200,200]

worksheet.write_column('A1', Measured)
worksheet.write_column('B1', Budget)


Chart.add_series({
    'name':'series name',
    'values':'=my_first_woorksheet!$A$1:$A$6',
    'border':{'color':'black'},
    'data_labels':{'value':True},
    })
Chart.add_series({
    'name':'series name',
    'values':'=my_first_woorksheet!$B$1:$B$6',
    'border':{'color':'black'},
    'data_labels':{'value':True},
    })

worksheet.insert_chart('A7', Chart)
# Set arbitrary axis’ names.
# Create pie chart.
# Set pie size 400/700.
# Add data to chart - 75% female, 25% male.
# Insert it into arbitrary field.

pie = workbook.add_chart({'type': 'pie'})
pie.set_size({'width': 400, 'height': 700})

pie.set_x_axis({
	'name': 'arbitrary x name'
})
pie.set_y_axis({
	'name': 'arbitrary y name'
})

ratio = [75, 25]
worksheet.write_column('G1', ratio)

pie.add_series({
    'name':'pie chart',
    'values':'=my_first_woorksheet!$G$1:$G$2',
    
})




worksheet.insert_chart('G7', pie)


workbook.close()



