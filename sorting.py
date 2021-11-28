from tkinter import *
from tkinter import ttk
# from tkinter import messagebox
from operator import itemgetter
import sqlite3

# aqui definimos la conexion a la base de datos

con = sqlite3.connect("data.db")
_cursor = con.cursor()

rows = _cursor.execute("""SELECT *FROM Inmuebles WHERE ID<=100 """).fetchall()


# aqui definimos la ventana principal

root = Tk()
root.title('visor de datos de busqueda')
root.geometry('500x500')

styleTtk = ttk.Style(root)
# root.tk.call('source', 'forest-dark.tcl')
# styleTtk.theme_use('forest-dark')

# aqui se declara las funciones que vamos a usar

reverseTable = [False, False, False, False, False, False, False, False]



def putClient():
   global rows
   tree.delete(*tree.get_children())
   for row in rows:
      tree.insert('', END, values=(row[0],
                                   row[2],
                                   row[3],
                                   row[4],
                                   row[5],
                                   row[6],
                                   row[7],))

def orderBy(criterio):
   global rows
   global reverseTable
   rows = sorted(rows, key=itemgetter(criterio), reverse= reverseTable[criterio])
   
   if reverseTable[criterio]==True:
      reverseTable[criterio] = False
   else:
      reverseTable[criterio] = True
   
   putClient()

# aqui vamos a configurar la ventana

# mainFrame = ttk.Frame(root)
# mainFrame.grid(row=0, column=0)


tree = ttk.Treeview(root)
tree['columns']=( 
                  # 'Fecha',
                  'ID',
                  'Tipo', 'Operacion', 'Provincia', 
                  'Superficie','Precio de Venta', 'Contrato')


tree.column('#0', width=0, stretch=NO)
tree.heading('#0', text= 'ID', command= lambda: orderBy('Tipo'))

# tree.column( 'Fecha' ,width=30)
# tree.heading('Fecha', text= 'Fecha', command= lambda: orderBy('Fecha'))

tree.column( 'ID' ,width=30)
tree.heading('ID', text= 'ID', command= lambda: orderBy(0))

tree.column( 'Tipo' ,width=30)
tree.heading('Tipo', text= 'Tipo', command= lambda: orderBy(2))

tree.column( 'Operacion' ,width=30)
tree.heading('Operacion', text= 'Operacion', command= lambda: orderBy(3))

tree.column( 'Provincia' ,width=30)
tree.heading('Provincia', text= 'Provincia', command= lambda: orderBy(4))

tree.column( 'Superficie' ,width=30)
tree.heading('Superficie', text= 'Superficie', command= lambda: orderBy(5))

tree.column( 'Precio de Venta' ,width=30)
tree.heading('Precio de Venta', text= 'Precio', command= lambda: orderBy(6))

tree.column( 'Contrato' ,width=30)
tree.heading('Contrato', text= 'Contrato', command= lambda: orderBy(7))


tree.grid(row=0, column=0, sticky= 'nsew', padx=(10,0), pady=10)

putClient()

scroll = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
scroll.grid(row=0, column=1, sticky= 'nsew', padx=(0,10), pady=10)
tree['yscrollcommand'] = scroll.set

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
print(root.winfo_height())
# print(rows)
root.mainloop()