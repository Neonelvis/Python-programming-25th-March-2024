import sqlite3 
import random
import string 
from fpdf import FPDF  



class User: 
    """"Represents a User that buys a cinema seat"""
    # constructor 
    def __init__(self, name):
        self.name = name
    
    def buy(self, seat, card):
        """Buys the seat if the card is valid"""
        if seat.is_free() == True:
            if card.validate(seat.get_price()):
                seat.occupy()
                # generate the PDF ticket 
                ticket = Ticket(user=self, price=seat.get_price(), seat_number= seat.seat_id)
                ticket.to_pdf()
                return "Purchase was Successful!!!"
            else:
                return "There was a problem with your card!!!" 
        else:
            return "Seat is Taken!!!"

class Seat:
    """Represents a cinema seat that can be purchased by the user """
    database = 'cinema.db'

    # constructor 
    def __init__(self, seat_id):
        self.seat_id = seat_id

    # method to get the price of the seat from the db 
    def get_price(self):
        """Get the price of a certain seat from the DB""" 
        connection = sqlite3.connect(self.database) 
        cursor = connection.cursor() 
        query = "SELECT price FROM seats WHERE seat_id = ?" 
        cursor.execute(query, [self.seat_id]) 
        price = cursor.fetchall()[0][0]  
        return price 

    # a method to check if a seat is free 
    def is_free(self):
        """Checks in the db if a seat is taken(free) or not """ 
        connection = sqlite3.connect(self.database) 
        cursor = connection.cursor() 
        query = "SELECT price FROM seats WHERE seat_id = ?" 
        cursor.execute(query, [self.seat_id]) 
        result = cursor.fetchall()[0][0] # 1 fpr taken or 0 for not taken 
        
        if result == 0:
            return
        else:
            return False 

    # a method to occupy a seat if it is free 
    def occupy(self): 
        """ Changes the value of taken in the DB from 0 to 1 if it is free""" 
        connection = sqlite3.connect(self.database) 
        cursor = connection.cursor() 
        query = "UPDATE seats SET taken = ? WHERE seat_id = ?" 
        cursor.execute(query, [1, self.seat_id]) 
        connection.commit()
        connection.close() 

class Card: 
    """Represents a bank card needed to finalize a seat purchase"""
    database = 'cinema.db' 

    # constructor 
    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number 
        self.cvc = cvc 
        self.holder = holder

    def validate(self, price): 
        """Checks if card is valid and has balance, subtract price of the seat from card balance"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        query = "SELECT balance FROM card WHERE number = ? AND cvc = ?" 
        cursor.execute(query, [self.number, self.cvc]) 
        result = cursor.fetchall() # [(2000,)] 
        
        if result: 
            balance = result[0][0]
            if balance >= price: 
                query = "UPDATE card SET balance = ? WHERE number = ? AND cvc = ?"
                cursor.execute(query, [(balance - price), self.number, self.cvc])
                connection.commit()
                connection.close()        
                return True 

class Ticket: 
    """Represents a cinema ticket purchased by a user"""
    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.seat_number = seat_number 
        self.id = "".join([random.choice(string.ascii_uppercase) for i in range (10)])

    
    # a method to generate the pdf 
    def to_pdf(self):
        """Creates a PDF Ticket"""
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        
        # Create the ticket title 
        pdf.set_font('Times', style='B', size=24)
        pdf.cell(w=0, h=80, txt='CPL Digital Cinema Ticket', border=1, ln=1, align='C')
        
        # create the username cell
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Name', border=1)
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=0, h=25, txt=self.user.name, border=1, ln=1)
        
        # create the ticket id cell
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Ticket ID', border=1)
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=0, h=25, txt=self.id, border=1, ln=1)
        
        # Create the price cell
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Price', border=1)
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=0, h=25, txt=f"{self.price}", border=1, ln=1)
        
        # Create the seat number cell
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Seat Nuber', border=1)
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=0, h=25, txt=self.seat_number, border=1, ln=1)

        
        # Output the pdf ticket
        pdf.output(f"{self.user.name}_{self.id}_{self.seat_number}.pdf")
        
                
    
# run the app here 
if __name__ == '__main__':
    name = input('Enter you Full Names: ')
    seat_id = input('Preffered Seat: ') 
    card_type = input('Your card type: ')
    card_number = input('Your card nuber: ')
    card_cvc = input('Your card cvc: ')
    card_holder = input('Card holdername: ') 
    
    # create objects here
    user = User(name)
    seat = Seat(seat_id)
    card = Card(card_type, card_number, card_cvc, card_holder) 
    
    # buy the seat 
    print(user.buy(seat, card)) 