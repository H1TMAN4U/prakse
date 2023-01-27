create table electricity_connection(
	`start_time` varchar(100)  not null,
    `end_time` varchar(100)  not null,
    `electricity_id` int not null,
    `saved_EUR` float not null,
	foreign key(`electricity_id`) references `Electricity`(`id`)
);