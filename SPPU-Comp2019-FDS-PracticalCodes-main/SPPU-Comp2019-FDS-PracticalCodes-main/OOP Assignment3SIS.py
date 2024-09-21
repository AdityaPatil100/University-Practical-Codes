//Student Information System
#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;
#define max 100;

class person
{
string lic, dob, bldgrp;
public:
person(); //Declaring Default constructor
person(person &);
~person()
{
cout<<"\n Person Destructor is called !"<<endl;
cout<<"Record Deleted Successfully.";
}
friend class student;
};
class student
{


string name, address, year;
char div;
int roll_no;
long long mob;
static int cnt;
public:
void create(person &); //Function declaration
void display(person &);

inline static void inccnt()
{
cnt++;
}
inline static void showcnt()
{
cout<<"\n Total no of records are :"<<cnt;
}
student(); //Declare default Constructor
student(student &);
~student()
{
cout<<"\n Student Destructor is called !"<<endl;
cout<<"......Record Deleted Successfully......"<<endl;
}
};


int student ::cnt;
student::student()
{
name="Ram";
address="Ayodhya";
year="SE Computer";
div='B';
roll_no=06;
mob=8057768733;
}
person::person()
{
lic="124523";
dob="01/01/2001";
bldgrp="O+";
}

//copy constructor
student::student(student &obj)
{
this->name=obj.name;
this->address=obj.address;
this->year=obj.year;
this->div=obj.div;


this->roll_no=obj.roll_no;
this->mob=obj.mob;
}

person::person(person &obj)
{
lic=obj.lic;
dob=obj.dob;
bldgrp=obj.bldgrp;
}

//Creating Database of student
void student::create(person &obj)
{
cout<<"\nEnter Student Name :"<<endl;
cin>>name;
cout<<"Enter student Address :"<<endl;
cin>>address;
cout<<"Enter student Date of Birth :"<<endl;
cin>>obj.dob;
cout<<"Enter student Course year :"<<endl;
cin>>year;
cout<<"Enter student Division :"<<endl;
cin>>div;
cout<<"Enter student Roll number :"<<endl;


cin>>roll_no;
cout<<"Enter student Blood Group :"<<endl;
cin>>obj.bldgrp;
cout<<"Enter student Licence number :"<<endl;
cin>>obj.lic;
cout<<"Enter student Phone number :"<<endl;
cin>>mob;
}

//To display Database
void student::display(person &obj)
{
cout<<"\n********************************************************"<<endl;
cout<<"\n Student Name :"<<name<<endl;
cout<<"\n Student Address :"<<address<<endl;
cout<<"\n Student Date of Birth :"<<obj.dob<<endl;
cout<<"\n Student Course Year :"<<year<<endl;
cout<<"\n Student Division :"<<div<<endl;
cout<<"\n Student Roll number :"<<roll_no<<endl;
cout<<"\n Student Blood Group :"<<obj.bldgrp<<endl;
cout<<"\n Student Licence Number :"<<obj.lic<<endl;
cout<<"\n Student Phone Number :"<<mob<<endl;


cout<<"\n********************************************************"<<endl;
}

int main()
{
int n;
int ch;
char ans;

cout<<"\n Enter no. of students :"<<endl;
cin>>n;
cout<<"\n***********************************************************"<<endl;
student *sobj=new student[n];
person *pobj=new person[n];

do
{
cout<<"\n Menu \n 1. Create Database \n 2. Display Database \n 3. Copy Constructor \n 4. Default Constructor";
cout<<"\n 5. Delete (Constructor) ";
cout<<"\n Enter your Choice";
cin>>ch;


switch(ch)
{
case 1:
{
for(int i=0;i<n;i++)
{

sobj[i].create(pobj[i]);
sobj[i].inccnt();

}
}
break;
case 2:
{
sobj[0].showcnt();
for(int i=0;i<n;i++)
{
sobj[i].display(pobj[i]);
}
}
break;
case 3:
{
student obj1;
person obj2;
obj1.create(obj2);



student obj3(obj1);
person obj4(obj2);

cout<<"\n Copy Constructor is called ";
obj3.display(obj4);
}
break;
case 4:
{
student obj1;
person obj2;
cout<<"\n Default Constructor ";
obj1.display(obj2);
}
break;
case 5:

delete [] sobj;
delete [] pobj;
}
cout<<"\n Wnts to continue :(Y/N)";
cin>>ans;

}while(ans=='Y');


return 0;
}

//Run This Code Easily in Dev C++ or Online gbd and Experience Self a very intresting and easy code practice it to be perfect
