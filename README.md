# Django Invoicing API

This Django application provides a RESTful API for managing invoices and invoice details.

## Overview

The API allows users to perform CRUD (Create, Read, Update, Delete) operations on invoices and their associated details.
It includes endpoints for listing, creating, updating, and deleting both invoices and invoice details. The API also accepts invoice details in the payload for creation and updating.

## Features

- Create, read, update, and delete invoices
- Create, read, update, and delete invoice details
- Accept invoice details in the payload for creation and updating

## Django Models

### Invoice Model

The `Invoice` model represents an invoice and includes the following fields:

- `date`: Date of the invoice
- `customer_name`: Name of the customer associated with the invoice

### InvoiceDetail Model

The `InvoiceDetail` model represents details associated with an invoice and includes the following fields:

- `invoice`: Foreign key to the Invoice model
- `description`: Description of the item or service
- `quantity`: Quantity of the item or service
- `unit_price`: Unit price of the item or service
- `price`: Total price calculated based on quantity and unit price

## Technologies Used

- Django: Web framework for building the API
- Django Rest Framework: Toolkit for building Web APIs in Django
- Python: Programming language used for backend development

## Created By --[Shubham6914]
