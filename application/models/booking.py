# id smallint primary key auto_increment not null,
# customer_id tinyint not null,
# dog_id tinyint not null,
# activity_id tinyint not null,
# event_id tinyint not null,
# foreign key(customer_id) references customer(id),
# foreign key(dog_id) references dog(id),
# foreign key(activity_id) references activity(id),
# foreign key(event_id) references event_info(id));