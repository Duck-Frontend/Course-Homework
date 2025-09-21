begin;
create table event(
    id serial primary key,
    event_name varchar(256) not null,
    event_desc text,
    date date,
    time_start timestamp with time zone,
    tickers_sold int
);

create table place(
    id serial primary key,
    place_name varchar(256) not null,
    address text,
    max_visitors int not null
);

create table tickets(
    id serial primary key,
    event serial references event(id),
    place serial references place(id)
);
end;

-- Наполнение

begin;
    insert into place (place_name, address, max_visitors) values
('central hall', 'green street, 15', 300),
('star club', 'sunset boulevard, 42', 150),
('conference room a', 'business center "tower"', 50);

insert into event (event_name, event_desc, date, time_start, tickers_sold) values
('tech talk: python basics', 'introduction to python programming', '2024-03-15', '2024-03-15 18:30:00+03', 0),
('indie music night', 'live performances by local bands', '2024-03-20', '2024-03-20 20:00:00+03', 0),
('startup networking', 'meet fellow entrepreneurs and investors', '2024-03-25', '2024-03-25 19:00:00+03', 0);

insert into tickets (event, place) values
(1, 1),
(2, 2),
(3, 3);

end;

