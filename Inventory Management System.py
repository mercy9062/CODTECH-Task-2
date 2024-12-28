# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:56:05 2024

@author: harin
"""

import tkinter as tk
from tkinter import messagebox

class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, quantity, price):
        if product_id in self.products:
            return f"Product ID {product_id} already exists."
        self.products[product_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }
        return f"Product {name} added successfully."

    def edit_product(self, product_id, name=None, quantity=None, price=None):
        if product_id not in self.products:
            return f"Product ID {product_id} does not exist."
        if name:
            self.products[product_id]["name"] = name
        if quantity is not None:
            self.products[product_id]["quantity"] = quantity
        if price is not None:
            self.products[product_id]["price"] = price
        return f"Product ID {product_id} updated successfully."

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            return f"Product ID {product_id} deleted successfully."
        return f"Product ID {product_id} does not exist."

    def low_stock_alert(self, threshold=5):
        low_stock_items = {pid: details for pid, details in self.products.items() if details["quantity"] < threshold}
        return low_stock_items

    def generate_report(self):
        return self.products

class InventoryApp:
    def __init__(self, root):
        self.manager = InventoryManager()
        self.root = root
        self.root.title("Inventory Management System")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20, padx=20)

        self.label_product_id = tk.Label(self.frame, text="Product ID:")
        self.label_product_id.grid(row=0, column=0, padx=5, pady=5)
        self.entry_product_id = tk.Entry(self.frame)
        self.entry_product_id.grid(row=0, column=1, padx=5, pady=5)

        self.label_name = tk.Label(self.frame, text="Product Name:")
        self.label_name.grid(row=1, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.frame)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)

        self.label_quantity = tk.Label(self.frame, text="Quantity:")
        self.label_quantity.grid(row=2, column=0, padx=5, pady=5)
        self.entry_quantity = tk.Entry(self.frame)
        self.entry_quantity.grid(row=2, column=1, padx=5, pady=5)

        self.label_price = tk.Label(self.frame, text="Price:")
        self.label_price.grid(row=3, column=0, padx=5, pady=5)
        self.entry_price = tk.Entry(self.frame)
        self.entry_price.grid(row=3, column=1, padx=5, pady=5)

        self.button_add = tk.Button(self.frame, text="Add Product", command=self.add_product)
        self.button_add.grid(row=4, column=0, padx=5, pady=5)

        self.button_edit = tk.Button(self.frame, text="Edit Product", command=self.edit_product)
        self.button_edit.grid(row=4, column=1, padx=5, pady=5)

        self.button_delete = tk.Button(self.frame, text="Delete Product", command=self.delete_product)
        self.button_delete.grid(row=5, column=0, padx=5, pady=5)

        self.button_low_stock = tk.Button(self.frame, text="Low Stock Alert", command=self.show_low_stock)
        self.button_low_stock.grid(row=5, column=1, padx=5, pady=5)

        self.button_report = tk.Button(self.frame, text="Generate Report", command=self.generate_report)
        self.button_report.grid(row=6, column=0, columnspan=2, pady=10)

    def add_product(self):
        product_id = self.entry_product_id.get()
        name = self.entry_name.get()
        try:
            quantity = int(self.entry_quantity.get())
            price = float(self.entry_price.get())
        except ValueError:
            messagebox.showerror("Input Error", "Quantity must be an integer and price a number.")
            return
        message = self.manager.add_product(product_id, name, quantity, price)
        messagebox.showinfo("Add Product", message)

    def edit_product(self):
        product_id = self.entry_product_id.get()
        name = self.entry_name.get() or None
        try:
            quantity = int(self.entry_quantity.get()) if self.entry_quantity.get() else None
            price = float(self.entry_price.get()) if self.entry_price.get() else None
        except ValueError:
            messagebox.showerror("Input Error", "Quantity must be an integer and price a number.")
            return
        message = self.manager.edit_product(product_id, name, quantity, price)
        messagebox.showinfo("Edit Product", message)

    def delete_product(self):
        product_id = self.entry_product_id.get()
        message = self.manager.delete_product(product_id)
        messagebox.showinfo("Delete Product", message)

    def show_low_stock(self):
        low_stock_items = self.manager.low_stock_alert()
        if low_stock_items:
            alert_message = "\n".join([f"{details['name']} (ID: {pid}): {details['quantity']} in stock" for pid, details in low_stock_items.items()])
        else:
            alert_message = "No low-stock items."
        messagebox.showinfo("Low Stock Alert", alert_message)

    def generate_report(self):
        report = self.manager.generate_report()
        if report:
            report_message = "\n".join([f"{details['name']} (ID: {pid}): {details['quantity']} in stock at ${details['price']:.2f}" for pid, details in report.items()])
        else:
            report_message = "No products in inventory."
        messagebox.showinfo("Inventory Report", report_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
