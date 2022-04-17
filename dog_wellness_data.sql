create database dog_wellness_service;
use dog_wellness_service;


create table event_info(
id tinyint primary key auto_increment not null,
event_date date not null,
start_time time not null,
end_time time not null,
cost tinyint not null,
capacity tinyint not null);


create table activity(
id tinyint primary key auto_increment not null,
activity_name varchar(40) not null,
description varchar(500) not null,
activity_type enum("Group Class", "1 to 1") not null,
supervision enum("Stay and Play", "Drop and Go") not null);


create table upcoming_event(
id tinyint primary key auto_increment not null,
activity_id tinyint not null,
event_info tinyint not null,
foreign key(activity_id) references activity(id),
foreign key(event_info) references event_info(id));


create table full_address(
id smallint primary key auto_increment not null,
first_line varchar(100) not null,
second_line varchar(100),
town varchar(35) not null,
postcode varchar(12) not null);


create table customer(
id tinyint primary key auto_increment not null,
first_name varchar(100) not null,
last_name varchar(100) not null,
email varchar(100) not null,
telephone_number varchar(12) not null,
address smallint not null,
foreign key (address) references full_address(id));


create table dog_category(
id tinyint primary key auto_increment not null,
size enum("large", "medium", "small") not null,
energy_level enum("couch potato", "moderate", "energetic"));


create table activity_recommendation(
id tinyint primary key auto_increment not null,
dog_category tinyint not null,
activity_recommendation tinyint not null,
foreign key(dog_category) references dog_category(id),
foreign key(activity_recommendation) references activity(id));


create table dog(
id tinyint primary key auto_increment not null,
dog_name varchar(40) not null,
breed varchar(40) not null,
age tinyint not null,
weight tinyint not null,
energy_level enum("Couch Potato", "Moderate", "energetic"),
temperament tinyint not null,
dog_owner tinyint not null,
foreign key(temperament) references dog_category(id),
foreign key(dog_owner) references customer(id));


create table booking(
id smallint primary key auto_increment not null,
customer_id tinyint not null,
dog_id tinyint not null,
activity_id tinyint not null,
event_id tinyint not null,
foreign key(customer_id) references customer(id),
foreign key(dog_id) references dog(id),
foreign key(activity_id) references activity(id),
foreign key(event_id) references event_info(id));

