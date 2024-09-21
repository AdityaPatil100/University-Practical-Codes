#include<iostream>
#include<string>
using namespace std;
class publication// base class
{
     private: //acess specifier
     string title;
     float price;
     public:// acess specifier
     void getdata()
     {
         cout <<"|\n Enter the name of title:";
         cin>> title;
         cout<<"\n enter the Price of Book:"; 
         cin >> price;
    }
    void display ()
    {
        cout<<"\n The name of Title:"  << title;
        cout<<"\n The price of Book:" << price;
          
     }
};
 class Book: public publication // derived class 
 { 
     private:// acess specifier
     int page;
     public :// acess specifier
  void getdata()
  {
       publication :: getdata();// decleration of getdata()base class
       cout<<"\n Enter the Number of Pages:";
       cin >>page;
       
  }
  void display()
  {
        publication::display();// decleration of display() base class
        cout<< "\n The number of pages:"<<page;
  }
 };
class Tape :public publication
 {  
    private:
    float min;
    public:
    void getdata()
    {
        publication :: getdata();
        cout<<"\n Enter the playing time in minutes:"<<endl;
        cin >>min;
    }
    
    void display()
    {
        publication::display();
        cout<<"\n playing time in minutes:"<<min;
        
    }
};
int main()
{
    Book b1;// created object of derive classe Book
    Tape t1;// created object of derived class Tape
    b1.getdata();
    t1.getdata();
    cout<<"\a"<<endl;//'\a'produces the beep sound
    b1.display();
    cout<<endl;
    t1.display();
    cout<<endl;
    return 0;
    
}
    
OUTPUT:

 Enter the name of title:Raja_ShivChatrapti

 enter the Price of Book:1500

 Enter the Number of Pages:2500
|
 Enter the name of title:Chawa

 enter the Price of Book:2000

 Enter the playing time in minutes:
45


 The name of Title:Raja_ShivChatrapti
 The price of Book:1500
 The number of pages:2500

 The name of Title:Chawa
 The price of Book:2000
 playing time in minutes:45
