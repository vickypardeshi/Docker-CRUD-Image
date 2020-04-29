create database if not exists myUsers;

use myUsers;

drop table if exists users;

create table users(
	ID int primary key,
	Name char(25) not null,
	Age int not null,
	Department char(20),
	Subject char(10)
);

insert users values(1813618, "Vicky Pardeshi", 23, "PUSCD", "DevOps");
insert users values(18107, "Aniket Chavan", 28, "PUSCD", "OS");
insert users values(18208, "Bhavesh Nandurikar", 23, "Math", "TCS");
insert users values(18158, "Shubham Natekar", 22, "Stat", "DBMS");
insert users values(18141, "Akash Hiwale", 25, "Commerce", "Account");
insert users values(18166, "Ankush Zaware", 24, "PUMBA", "Network");
