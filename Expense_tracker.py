import  sqlite3
import datetime

class Mymain:

#defining the main function to operate other function in the body
 def main(self):
        while (True):
            print("=====================================================")
            print("   ....Welcome to the Expense Tracker system....   ")
            print("=====================================================")
            print("Enter 1. To enter expenses into your database")
            print("Enter 2. To view current expenses with date")
            print("Enter 3. To see total expending")
            print("Enter 4. To exit")
            print("=====================================================")
            try:
                self.a = int(input("Select a choice (1-3): "))
                print()
                if (self.a == 1):
                    d = Data_input()
                    d.data()

                elif (self.a == 2):
                    v = Data_input()
                    v.view_data()

                elif (self.a == 3):
                    t = Data_input()
                    t.total_amount()

                elif (self.a == 4):
                    print("Thank you for using Expense Tracker system")
                    break
                else:
                    print("Please enter a valid choice from 1-4")
            except ValueError:
                print("Please input as suggested.")


class Data_input:

# function for entering data into database

  def data(self):
        conn = sqlite3.connect('my_expns_database.db')
        cursor = conn.cursor()
        # creating the Expense table in the database
        cursor.execute('''
        create table if not exists expense(
                 item string, 
                   price number, 
                   date string )
        ''')

        i_item = str(input('Enter the item you purchased:'))
        i_price = float(input('Cost of item in Dollars:'))
        #i_date = datetime.strptime(input('Enter Start date in the format d/m/y'), '%d/%m/%Y')
        i_date = input("Please enter purchase date in the format dd/mm/yyyy: ")
        day, month, year = i_date.split('/')
        i_date = datetime.date(int(year), int(month), int(day))
        cursor.execute("""
                INSERT INTO expense(item, price, date)
                VALUES (?,?,?)
        """, (i_item, i_price, i_date))
        conn.commit()
        print('Data entered successfully.')

#function for viewing expense data from database

  def view_data(self):
        conn = sqlite3.connect('my_expns_database.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT * from expense
        """)
        rows = cursor.fetchall()
        print ('---Every Expense data you entered with date---')
        print()
        for r in rows:
            #list = ["Item","Price","Date"]
            #print (list)
            print("Item-Name:",r[0],"|","Price:",'$',r[1],"|","Date:",r[2])
            print ("---------------------------")

#Function for viewing total expense so far

  def total_amount(self):
        conn = sqlite3.connect('my_expns_database.db')
        cursor = conn.cursor()
        cursor.execute(""" SELECT sum(price) from expense
        """)
        total = cursor.fetchone()
        for row in total:
            print("Total Spending in Dollars:","$", row)

#calling the main Function

m = Mymain()
m.main()
