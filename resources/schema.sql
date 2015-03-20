drop table if exists demotable;
create table demotable (
  id integer primary key autoincrement,
  demotext text not null
);

drop table if exists todos;
create table todos (
  id integer primary key autoincrement,
  title text not null,
  completed integer not null
);
