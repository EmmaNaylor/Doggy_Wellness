# id tinyint primary key auto_increment not null,
# dog_category tinyint not null,
# activity_recommendation tinyint not null,
# foreign key(dog_category) references dog_category(id),
# foreign key(activity_recommendation) references activity(id));