create table prices(
	`start_time` varchar(100)  not null,
    `end_time` varchar(100) not null,
    `electricity_id` int not null,
	foreign key(`electricity_id`) references `Electricity`(`id`),
    `price` float not null
);