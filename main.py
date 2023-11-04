from re import S
from select import select
import tkinter as tk
import model as crud
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry

class MainBD():
    def __init__(self, win):
        self.objDB = crud.AppBD()
        self.janela = win

        self.text = tk.Label(self.janela, text = "EASY EXPENSE TRACKER", width=25, height = 1, relief = 'flat', padx = 3, pady = 10, anchor = 'center', font = ('Ivi 15 bold'), fg = '#53687E', background= '#E6EFE9')
        self.text.grid(row = 0, column = 0, columnspan = 5)
        
        self.frame_1 = tk.Frame(self.janela, width = 100, height = 100)
        self.frame_1.grid(row = 1, column = 2, padx = 25)
        
        self.treeProducts = ttk.Treeview(self.frame_1, columns = ("ID", "Name", "Price", "Date", "Payment", "Description", "Status", ), show = "headings")
        self.treeProducts.grid(row = 1, column = 0, columnspan = 6) 
        self.treeProducts.bind("<ButtonRelease-1>", self.LoadSelectedProduct)

        self.treeProducts.heading("ID", text = "ID")
        self.treeProducts.heading("Name", text = "NAME")
        self.treeProducts.heading("Price", text = "PRICE")
        self.treeProducts.heading("Date", text = "DATE")
        self.treeProducts.heading("Payment", text = "PAYMENT")
        self.treeProducts.heading("Description", text = "DESCRIPTION")
        self.treeProducts.heading("Status", text = "STATUS")
        
        self.treeProducts.column("ID", width = 50)
        self.treeProducts.column("Name", width = 130) 
        self.treeProducts.column("Price", width = 78) 
        self.treeProducts.column("Date", width = 100) 
        self.treeProducts.column("Payment", width = 122) 
        self.treeProducts.column("Description", width = 200) 
        self.treeProducts.column("Status", width = 80) 
        

        self.scrollbar = tk.Scrollbar(self.frame_1, orient = "vertical", command = self.treeProducts.yview)
        self.scrollbar.grid(row = 1, column = 6, sticky = "ns")
        self.treeProducts.configure(yscrollcommand = self.scrollbar.set)
        
        self.ShowScreen()
        
        self.frame = tk.Frame(self.janela, background= '#E6EFE9')
        self.frame.grid(row = 2, column = 0, columnspan = 3)
        
        self.lblID = tk.Label(self.frame, text="ID", background= '#E6EFE9', fg = '#53687E')
        self.lblID.grid(row = 0, column = 0)
        self.entryID = tk.Entry(self.frame, width = 10)
        self.entryID.grid(row = 1, column = 0, padx = 2, pady = 5)
        self.entryID.config(state = 'disabled')
        
        self.lblName = tk.Label(self.frame, text="NAME", background= '#E6EFE9', fg = '#53687E')
        self.lblName.grid(row = 0, column = 1)
        self.entryName = tk.Entry(self.frame, width = 20)
        self.entryName.grid(row = 1, column = 1, padx = 2, pady = 5)
        
        self.lblPryce = tk.Label(self.frame, text="PRYCE", background= '#E6EFE9', fg = '#53687E')
        self.lblPryce.grid(row = 0, column = 2)
        self.entryPryce = tk.Entry(self.frame, width = 10)
        self.entryPryce.grid(row = 1, column = 2, padx = 2, pady = 5)
        
        self.lblDate = tk.Label(self.frame, text="DATE", background= '#E6EFE9', fg = '#53687E')
        self.lblDate.grid(row = 0, column = 3)
        self.entryDate = DateEntry(self.frame, width=12, background='#FFFFFF', foreground='#000000', borderwidth=2)
        self.entryDate.grid(row=1, column=3, padx=2, pady=5)

        self.lblPayment = tk.Label(self.frame, text="PAYMENT", background= '#E6EFE9', fg = '#53687E')
        self.lblPayment.grid(row = 0, column = 4)
        self.entryPayment = tk.Entry(self.frame)
        self.entryPayment.grid(row = 1, column = 4, padx = 2, pady = 5)
        
        self.lblDescription = tk.Label(self.frame, text="DESCRIPTION", background= '#E6EFE9', fg = '#53687E')
        self.lblDescription.grid(row = 0, column = 5)
        self.entryDescription = tk.Entry(self.frame, width = 20)
        self.entryDescription.grid(row = 1, column = 5, padx = 2, pady = 5)
        
        status = ["-", "PAID OUT", "PENDING"]
        self.lblStatus = Label(self.frame, text="STATUS", background= '#E6EFE9', fg = '#53687E')
        self.lblStatus.grid(row = 0, column = 6)
        self.list = ttk.Combobox(self.frame, values = status, width = 12, state= "readonly")
        self.list.grid( row = 1, column = 6, padx = 2, pady = 5)
          
        self.frame_2 = tk.Frame(self.janela, width = 800, height = 100, background= '#E6EFE9')
        self.frame_2.grid(row = 3, column = 0, columnspan = 6)

        self.btnRegister = tk.Button(self.frame_2, text = "ADD PRODUCT", background = '#45BA60', fg='#030027', command = self.RegisterProduct)
        self.btnRegister.grid(row = 1, column = 3)

        self.btnUpdate = tk.Button(self.frame_2, text="UPDATE PRODUCT",background = '#F6AA1C', fg='#030027', command = self.UpdateProduct)
        self.btnUpdate.grid(row = 1, column = 4, padx = 20, pady = 20)

        self.btnDelete = tk.Button(self.frame_2, text="DELETE",background = '#CD4631', fg='#030027', command = self.DeleteProduct)
        self.btnDelete.grid(row = 1, column = 5)
        
    def ShowScreen(self):
        try:
            print("Available data")
            self.treeProducts.delete(*self.treeProducts.get_children())
            products = self.objDB.select_all_products()
            for products in products:
                self.treeProducts.insert("", tk.END, values = products)
        except:
            print("Unable to display fields.")

    def RegisterProduct(self):
        try:
            name = self.entryName.get()  
            print(type(name))
            price = float(self.entryPryce.get())
            print(type(price))
            date = str(self.entryDate.get())
            print(type(date))
            payment = str(self.entryPayment.get())
            print(type(payment))
            description = str(self.entryDescription.get())
            print(type(description))
            status = self.list.get()
            print(type(status))
            self.objDB.insert_data(name, price, date, payment, description, status)
            self.ShowScreen()

            self.entryName.delete(0, tk.END)
            self.entryPryce.delete(0, tk.END)
            self.entryDate.delete(0, tk.END)
            self.entryPayment.delete(0, tk.END)
            self.entryDescription.delete(0, tk.END)
            self.list.delete(0, tk.END)
            print("Product registered successfully.")
        except:
            print("Unable to register.")

    def UpdateProduct(self):
        try:
            select_item =  self.treeProducts.selection()
            if not select_item:
                return
            item = self.treeProducts.item(select_item)
            print(item)
            product = item["values"]
            product_id = product[0]
            name = self.entryName.get()
            pryce = float(self.entryPryce.get())
            payment = self.entryPayment.get()
            date = self.entryDate.get()
            description = self.entryDescription.get()
            status = self.list.get()
            self.objDB.update_products(product_id, name, pryce, payment, date, description, status)
            self.ShowScreen()

            self.entryName.delete(0, tk.END)
            self.entryPryce.delete(0, tk.END)
            self.entryDate.delete(0, tk.END)
            self.entryPayment.delete(0, tk.END)
            self.entryDescription.delete(0, tk.END)
            self.lblStatus.delete(0, tk.END)
        except:
            print("Unable to update.")

    def DeleteProduct(self):
        try:
            select_item = self.treeProducts.selection()
            if not select_item:
                return
            item = self.treeProducts.item(select_item)
            print(item)
            product = item['values']
            product_id = product[0]
            self.objDB.delete_products(product_id)
            self.ShowScreen()

            self.entryName.delete(0, tk.END)
            self.entryPryce.delete(0, tk.END)
            self.entryDate.delete(0, tk.END)
            self.entryPayment.delete(0, tk.END)
            self.entryDescription.delete(0, tk.END)
            self.list.delete(0, tk.END)
        except Exception as e:
            print("Unable to delete product", e)

    def LoadSelectedProduct(self, event):
        try:
            selected_item = self.treeProducts.selection()
            if not selected_item:
             return
            item = self.treeProducts.item(selected_item)
            product = item["values"]
            product_id, name, price, date, payment, description, status = product

            self.entryID.config(state='normal')
            self.entryID.delete(0, tk.END)
            self.entryID.insert(0, product_id)
            self.entryID.config(state='disabled')

            self.entryName.delete(0, tk.END)
            self.entryName.insert(0, name)

            self.entryPryce.delete(0, tk.END)
            self.entryPryce.insert(0, price)

            self.entryDate.delete(0, tk.END)
            self.entryDate.insert(0, date)

            self.entryPayment.delete(0, tk.END)
            self.entryPayment.insert(0, payment)

            self.entryDescription.delete(0, tk.END)
            self.entryDescription.insert(0, description)

            self.list.set(status)

        except Exception as e:
            print("Unable to load selected product.", e)


janela = tk.Tk()
product_app = MainBD(janela)
janela.title("WalletWizard")
janela.geometry("825x420")
janela.configure(background= '#E6EFE9')
janela.resizable(False,False)
janela.mainloop()