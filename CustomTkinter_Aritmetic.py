"""
==============
CustomTkinter upgraded version : Auto reload arithmetic equation
==============

This in- progress file for answering auto-reload equations of addition and substract  for specific time limit.( In-progress)


References:

https://www.youtube.com/watch?v=Jl1xsH6MR1g
`

"""
import csv
import tkinter as tk
import random
import time
from time import time
import customtkinter


#display  window
root = tk.Tk()

#set title to root window
root.title('Arithmetic')



# class for addition.
class in_addition:

    # initialize all instance variables for class instances
    def __init__(self,root):
       # Frame in root window with width of 300 ,height of 600, color black, with corner radius  of 10   
       self.mywindow = customtkinter.CTkFrame(root, width = 300, height = 600,fg_color='black',corner_radius=10)
       self.mywindow.place(relx=0.5,rely=0.05,anchor=tk.CENTER)
       self.mywindow.pack()
       
       # Main title using label with width of 250 and height 25
       label1 = customtkinter.CTkLabel(root, text='MENTAL ARITHMETIC PRACTICE',width=250,height=25,
                                       bg_color=('green','black'),corner_radius=15)
       label1.place(relx=0.5,rely=0.025,anchor=tk.CENTER)
       
       # Button to initialize in_additon function callback  with click 
       self.addition_button = customtkinter.CTkButton(master=root,text='Addition',
                                                      width=135,height=30,fg_color='blue',bg_color='black',corner_radius=15,text_font=('helvetica',12),
                                                      command=self.addition_algo)
       self.addition_button.place(relx=0.05,rely=0.56)
       
       # Button to initialize result checking aplication
       self.check_result_button = customtkinter.CTkButton(master=root,text='Check_Result',
                                                          width=135,height=30,fg_color='black',bg_color='black',corner_radius=15,text_font=('helvetica',12),
                                                          command=self.check_result)
       self.check_result_button.place(relx=0.05,rely=0.7)
       

       # Equation display box using entry box 
       self.entry_display = customtkinter.CTkEntry (root,
                                                    width=270,height=300,fg_color='white',bg_color='black',corner_radius=20)
       self.entry_display.place(relx=0.5,rely=0.3,anchor=tk.CENTER)              

       #entry box for range setting
       self.entry1 = customtkinter.CTkEntry (root,width=80,height=20,bg_color='gray',corner_radius=10)
       self.entry1.place(relx=0.2,rely=0.8,anchor=tk.CENTER)

       self.entry2 = customtkinter.CTkEntry (root,width=80,height=30,fg_color='gray',corner_radius=10)
       self.entry2.place(relx=0.5,rely=0.33,anchor=tk.CENTER) 

       # count displayed equations
       self.Count_1 = 0
       # count correct answers
       self.Count_OK= 0
       # count incorrect answers
       self.Count_NG = 0

       

    def addition_algo(self):

        self.x1 = self.entry1.get()
        
        
        # try and accept to test and handle errors
        try:
            # Randomly create numbers for addition
            self.Number_1 = random.randrange(float(self.x1))
            self.Number_2 = random.randrange(float(self.x1))

            # Summation of randomly created 2 numbers
            self.Sum_1    = self.Number_1 + self.Number_2
            
            self.Count_1 = self.Count_1 + 1

            # Display first number on display box
            self.label4 = customtkinter.CTkLabel(root,text= str(self.Number_1),fg_color='white',text_font=('helvetica',15))
            self.label4.place(relx=0.5,rely=0.2,anchor=tk.CENTER)
            
            
            # Display '+' addition symbol on display box
            self.label5 = customtkinter.CTkLabel(root, text='+',fg_color='white',text_font=('helvetica',15))
            self.label5.place(relx=0.37,rely=0.25,anchor=tk.CENTER)
            
            #Display 2nd number on display bo
            self.label5_1 = customtkinter.CTkLabel(root, text= str(self.Number_2),fg_color='white',
                                                   width=55,height=30,text_font=('helvetica',15, 'bold'))
            self.label5_1.place(relx=0.5,rely=0.25,anchor=tk.CENTER)
            
            
            self.label6 = customtkinter.CTkLabel(root,fg_color='white', text='---------',width=50,height=5)
            self.label6.place(relx=0.5,rely=0.3,anchor=tk.CENTER)

            
           
            #Display Equation number
            self.label6_1 = customtkinter.CTkLabel(root, text=str('Q.{}'.format(self.Count_1)),
                                                   width=35,height=30,fg_color='white',text_font=('Arial',12))
            self.label6_1.place(relx=0.15,rely=0.1,anchor=tk.CENTER)
            
           

            self.label4_11 = customtkinter.CTkLabel(root, text='',width=250,height=35,bg_color='black',corner_radius=10)
            self.label4_11.place(relx=0.5,rely=0.8,anchor=tk.CENTER)

        except:
            # check enter value integer or not.
            if not type(self.x1) is int:
                
                self.label4_11 = customtkinter.CTkLabel(root, text='Input Number Please!',
                                                        width=250,height=20,bg_color='green',corner_radius=10,text_font=('helvetica',12))
                self.label4_11.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
            
           
                

        # Set delay time of 5000ms for entry answer by user.
        self.check_result_button.after(5000,self.check_result)
        
        
    def check_result(self):

        
        self.x2 = self.entry2.get()

        try:
            if int(self.x2) == self.Sum_1:
                self.Count_OK = self.Count_OK + 1
                label8 = customtkinter.CTkLabel(root, text='Correct,Well Done',width=250,height=25,bg_color='green',corner_radius=15)
                label8.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
                
                label8_1 = customtkinter.CTkLabel(root, text= 'Correct:' + str(self.Count_OK),width = 80,height=25,fg_color='white')
                label8_1.place(relx=0.5,rely=0.12,anchor=tk.CENTER)


        
            else:
                self.Count_NG = self.Count_NG + 1
                
                
                
                label8_1 = customtkinter.CTkLabel(root, text= 'Wrong:' + str(self.Count_NG),width=80,height=25,fg_color='white')
                label8_1.place(relx=0.8,rely=0.12,anchor=tk.CENTER)

                label8 = customtkinter.CTkLabel(root, text='Wrong Try Again',width=250,height=25,bg_color='green',corner_radius=15)
                label8.place(relx=0.5,rely=0.75,anchor=tk.CENTER)

           
        except:
            
            if not type(self.x2) is int:
                
                self.label4_11 = customtkinter.CTkLabel(root, text='Input Number PLease!',
                                                        width=80,height=20,bg_color='green',corner_radius=10,text_font=('helvetica',12))
                self.label4_11.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
                
        if self.Count_1 <=10:
            self.addition_button.after(5000,self.addition_algo)


        else:
            self.Count_1=0 
            self.addition_button.after_cancel(self) 
                
            
class in_substract(in_addition):
    
    def __init__(self,root):
        
        self.substract_button = customtkinter.CTkButton(master=root,text='Substract',
                                                        width=135,height=30,fg_color='blue',bg_color='black',corner_radius=15,text_font=('helvetica',12),
                                                        command=self.addition_algo1)
        self.substract_button.place(relx=0.5,rely=0.56)

        self.check_result1_button = customtkinter.CTkButton(master=root,text='Check_Result',
                                                            width=135,height=30,fg_color='black',bg_color='black',corner_radius=15,text_font=('helvetica',12),
                                                            command=self.check_result1)
        self.check_result1_button.place(relx=0.05,rely=0.7)
        
        in_addition.__init__(self,root)

       
       
        self.Count_1=0
       
    
    def addition_algo1(self):
        self.x1 = self.entry1.get()
        try:
            self.Number_1 = random.randrange(float(self.x1))
            self.Number_2 = random.randrange(float(self.x1))
            self.Count_1 = self.Count_1 + 1
            if self.Number_1 > self.Number_2:
                self.Sum_1 = self.Number_1 - self.Number_2
        
                self.label4 = customtkinter.CTkLabel(root, text= str(self.Number_1),fg_color='white',text_font=('helvetica', 15, 'bold'))
                self.label4.place(relx=0.5,rely=0.2,anchor=tk.CENTER)
        
                self.label5 = customtkinter.CTkLabel(root, text=  '-',fg_color='white',text_font=('helvetica', 10, 'bold'))
                self.label5.place(relx=0.37,rely=0.25,anchor=tk.CENTER) 


                self.label5_1 = customtkinter.CTkLabel(root, text= str(self.Number_2),fg_color='white',text_font=('helvetica', 15, 'bold'))
                self.label5_1.place(relx=0.5,rely=0.25,anchor=tk.CENTER)
        

                self.label6 = customtkinter.CTkLabel(root, text='---------',fg_color='white')
                self.label6.place(relx=0.5,rely=0.3,anchor=tk.CENTER)
           
                self.label6_1=customtkinter.CTkLabel(root,text='Q.{}'.format(str(self.Count_1)),fg_color='white',text_font=('helvetica', 15, 'bold'))
                self.label6_1.place(relx=0.15,rely=0.1,anchor=tk.CENTER)


            else:
                self.Sum_1 = self.Number_2 - self.Number_1
            
                self.label4 = customtkinter.CTkLabel(root, text= str(self.Number_2),text_font=('helvetica', 15, 'bold'))
                self.label4.place(relx=0.5,rely=0.2,anchor=tk.CENTER) 
        
                self.label5 = customtkinter.CTkLabel(root, text=  '-',text_font=('helvetica', 15),fg_color='white')
                self.label5.place(relx=0.37,rely=0.25,anchor=tk.CENTER) 


                self.label5_1 = customtkinter.CTkLabel(root, text= str(self.Number_1),fg_color='white',text_font=('helvetica', 15))
                self.label5_1.place(relx=0.5,rely=0.25,anchor=tk.CENTER) 

                self.label6 = customtkinter.CTkLabel(root, text='---------',fg_color='white')
                self.label6.place(relx=0.5,rely=0.3,anchor=tk.CENTER)
           

                self.label6_1 = customtkinter.CTkLabel(root, text='Q.{}'.format(str(self.Count_1)),fg_color='white',text_font=('helvetica', 15))
                self.label6_1.place(relx=0.15,rely=0.1,anchor=tk.CENTER)

               
        except:
            if not type(self.x1) is int:
                self.label4_11 = customtkinter.CTkLabel(root, text='Input Number Please!',
                                                        width=250,height=20,bg_color='green',corner_radius=10,text_font=('helvetica',15))
                self.label4_11.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
            
         


        self.check_result1_button.after(5000,self.check_result1)
           
                
    def check_result1(self):

          self.x2 = self.entry2.get()
          
          try:
              if int(self.x2) == self.Sum_1:
                  self.Count_OK = self.Count_OK + 1
                  label8 = customtkinter.CTkLabel(root, text='Correct,Well Done',width=250,height=25,bg_color='green',corner_radius=15)
                  label8.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
                
                  label8_1 = customtkinter.CTkLabel(root, text= 'Correct:' + str(self.Count_OK),width = 80,height=30,fg_color='white')
                  label8_1.place(relx=0.5,rely=0.1,anchor=tk.CENTER)


        
              else:
                  self.Count_NG = self.Count_NG + 1
                
                
                
                  label8_1 = customtkinter.CTkLabel(root, text= 'Wrong:' + str(self.Count_NG),width=80,height=30,fg_color='white')
                  label8_1.place(relx=0.8,rely=0.1,anchor=tk.CENTER)

                  label8 = customtkinter.CTkLabel(root, text='Wrong Try Again',width=250,height=25,bg_color='green',corner_radius=15)
                  label8.place(relx=0.5,rely=0.75,anchor=tk.CENTER)

           
             
 
          except:
              if not type(self.x2) is int:
                  self.label4_11 = customtkinter.CTkLabel(root, text='Input Number PLease!',
                                                          width=80,height=20,bg_color='green',corner_radius=10,text_font=('helvetica',12))
                  self.label4_11.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
                
          if self.Count_1 <=10:
              self.substract_button.after(5000,self.addition_algo1)


          else:
              self.Count_1=0 
              self.substract_button.after_cancel(self)

              
                   
# instance for in_addition class
e=in_addition(root)

#instance for in_substract class
f=in_substract(root)
root.mainloop()

