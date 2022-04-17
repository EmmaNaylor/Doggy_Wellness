# id tinyint primary key auto_increment not null,
# activity_id tinyint not null,
# event_info tinyint not null,
# foreign key(activity_id) references activity(id),
# foreign key(event_info) references event_info(id));