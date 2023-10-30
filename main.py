from re import S
from select import select
import tkinter as tk
import model as crud
from tkinter import ttk
from tkinter import *
from tkinter import font

# Colocar calendario
# Mudar button
# Finalizar traduções 

class MainBD():
    def __init__(self, win):
        self.objDB = crud.AppBD()
        self.janela = win
        self.janela.configure(bg="#FECE5E")
        self.custom_font = font.Font(family="Courierbold", size=20)
        self.custom_font2 = font.Font(family="Courierbold", size=10) 

        self.text = tk.Label(self.janela, text = "EASY EXPENSE TRACKER", height = 1, relief = 'flat', padx = 10, pady = 10, anchor = 'center', fg = '#166088', background= '#FECE5E', font = self.custom_font)
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
        
        self.frame = tk.Frame(self.janela, background= '#FECE5E')
        self.frame.grid(row = 2, column = 0, columnspan = 3)
        
        self.lblID = tk.Label(self.frame, text="ID", background= '#FECE5E', font = self.custom_font2, fg = '#166088')
        self.lblID.grid(row = 0, column = 0)
        self.entryID = tk.Entry(self.frame, width = 10)
        self.entryID.grid(row = 1, column = 0, padx = 2, pady = 5)
        self.entryID.config(state = 'disabled')
        
        self.lblName = tk.Label(self.frame, text="NAME", background= '#FECE5E', font = self.custom_font2, fg = '#166088')
        self.lblName.grid(row = 0, column = 1)
        self.entryName = tk.Entry(self.frame, width = 20)
        self.entryName.grid(row = 1, column = 1, padx = 2, pady = 5)
        
        self.lblPryce = tk.Label(self.frame, text="PRYCE", background= '#FECE5E', font = self.custom_font2, fg = '#166088')
        self.lblPryce.grid(row = 0, column = 2)
        self.entryPryce = tk.Entry(self.frame, width = 10)
        self.entryPryce.grid(row = 1, column = 2, padx = 2, pady = 5)
        
        self.lblDate = tk.Label(self.frame, text="DATE", background= '#FECE5E', font = self.custom_font2, fg = '#166088')
        self.lblDate.grid(row = 0, column = 3)
        self.entryDate = tk.Entry(self.frame, width = 10)
        self.entryDate.grid(row = 1, column = 3, padx = 2, pady = 5)
        
        self.lblPayment = tk.Label(self.frame, text="PAYMENT", background= '#FECE5E', font = self.custom_font2, fg = '#166088')
        self.lblPayment.grid(row = 0, column = 4)
        self.entryPayment = tk.Entry(self.frame)
        self.entryPayment.grid(row = 1, column = 4, padx = 2, pady = 5)
        
        self.lblDescription = tk.Label(self.frame, text="DESCRIPTION", background= '#FECE5E', font = self.custom_font2, fg = '#166088')
        self.lblDescription.grid(row = 0, column = 5)
        self.entryDescription = tk.Entry(self.frame, width = 20)
        self.entryDescription.grid(row = 1, column = 5, padx = 2, pady = 5)
        
        status = ["PAGO", "PENDENTE"]
        self.lblStatus = Label(self.frame, text="STATUS", background= '#FECE5E', font = self.custom_font2, fg = '#166088')
        self.lblStatus.grid(row = 0, column = 6)
        self.list = ttk.Combobox(self.frame, values = status, width = 12, state= "readonly")
        self.list.grid( row = 1, column = 6, padx = 2, pady = 5)
          
        self.frame_2 = tk.Frame(self.janela, width = 800, height = 100, background= '#FECE5E')
        self.frame_2.grid(row = 3, column = 0, columnspan = 6)

        self.btnRegister = tk.Button(self.frame_2, text = "ADD PRODUCT", background = '#4B809C', fg='#201335', command = self.RegisterProduct)
        self.btnRegister.grid(row = 1, column = 3)

        self.btnUpdate = tk.Button(self.frame_2, text="UPDATE PRODUCT",background = '#4B809C', fg='#201335', command = self.UpdateProduct)
        self.btnUpdate.grid(row = 1, column = 4, padx = 20, pady = 20)

        self.btnDelete = tk.Button(self.frame_2, text="DELETE",background = '#4B809C', fg='#201335', command = self.DeleteProduct)
        self.btnDelete.grid(row = 1, column = 5)
        
    def ShowScreen(self):
        try:
            print("Dados disponiveis")
            self.treeProducts.delete(*self.treeProducts.get_children())
            products = self.objDB.select_all_products()
            for products in products:
                self.treeProducts.insert("", tk.END, values = products)
        except:
            print("Não foi possiveel exibir os campos.")

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
            print("Produto cadastrado com sucesso.")
        except:
            print("Não foi possivel fazer o cadastro.")

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
            self.list.delete(0, tk.END)
        except:
            print("Não foi possivel fazer a atualização.")

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
        except Exception as e:
            print("Não foi possivel fazer a exclusão do produto", e)

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
            print("Não foi possível carregar o produto selecionado.", e)


janela = tk.Tk()
product_app = MainBD(janela)
janela.title("WalletWizard")
janela.geometry("825x420")
janela.mainloop()