create table electricity_connection(
	`start_time` datetime not null,
    `end_time` datetime not null,
    `price_kWH` varchar(45) not null,
    `electricity_id` int not null,
	foreign key(`electricity_id`) references `Electricity`(`id`)
);
insert into `prices` (`start_time`,`endt_time`,`electricity_id`,`price`) 
values (now(),now(),2,"0.16");