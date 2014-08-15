DROP TABLE IF EXISTS SNPHistory;
CREATE TABLE SNPHistory (
       snp_id          integer  primary key,
       create_time     timestamp,
       last_updated_time        timestamp,
       history_create_time      timestamp,
       sometext1                 text,
       sometext2                 text
);

DROP TABLE IF EXISTS RsMergeArch;
CREATE TABLE RsMergeArch (
       rsHigh            integer        primary key,
       rsLow             integer,
       build_id          smallint,
       orien             smallint,
       create_time       timestamp,
       last_updated_time timestamp,
       rsCurrent         integer        not null,
       orien2Current     smallint,
       sometext1         text
);

DROP TABLE IF EXISTS b141_SNPChrPosOnRef;
CREATE TABLE b141_SNPChrPosOnRef (
       snp_id                    integer        primary key,
       chr                       varchar(32)    not null,
       pos                       integer,
       orien                     integer,
       neighbor_snp_list         integer,
       isPAR                     varchar(1)     not null
);
