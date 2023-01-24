create table prices(
	`start_time` datetime not null,
    `end_time` datetime not null,
    `electricity_id` int not null,
	foreign key(electricity_id) references Electricity(id),
    `price` varchar(45) not null
);

insert into prices (`startime`,`endtime`,`electricity_id`,`price`)
values (now(),now(),2,"0.27");