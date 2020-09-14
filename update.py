import xlwings as xw
from PIL import ImageGrab


app = xw.App(visible=True, add_book=False)
wb = app.books.open('Timetable.xlsx')     
sheet = wb.sheets[0]                      
all = sheet.used_range

print(all.value)

all.api.CopyPicture()                 
sheet.api.Paste()                     
img_name = 'img'
pic = sheet.pictures[0]               
pic.api.Copy()                        

img = ImageGrab.grabclipboard()       
img.save(img_name + ".png")           
pic.delete()                          
 
wb.close()                            
app.quit()                            