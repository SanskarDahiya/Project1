import sqlite3 as sql
DB1 = 'database/e-learning.db'
con = sql.connect(DB1)
def exe(data):
   try:
      cur = con.cursor()
      cur.execute(data)
      con.commit()
      return True
   except:
      con.rollback
      return False

commands = [
   'create table userlogin(name varchar(100),mail varchar(100) primary key,pwd varchar(100),phno int(10))',
   'INSERT INTO userlogin VALUES ("Sanskar Dahiya","sanskardahiya98@gmail.com","Sanskar","9466150812");',
   ]
def main():
   print('Starting')
   i=1
   for x in commands:
      print(i,end=': ')
      i+=1
      if exe(x):
         print(x,'command is Sucessfull')
      else:
         print(x,'command is Unsucessfull')

   print('Done')

if __name__ == '__main__':
   main()
